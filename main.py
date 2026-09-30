import socket
import json
import os
from concurrent.futures import ThreadPoolExecutor


COMMON_PORTS = {     
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "Microsoft RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    5432: "PostgreSQL",
    8000: "HTTP",
    8080: "HTTP-Proxy",
}  #List of common ports and their services

scan_results = []


def save_results():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "scan_results.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(scan_results, file, indent=4)

    print(f"\nScan results saved to: {file_path}")


def check_host(host):                            #Check if the host is online or offline
    try:
        ip = socket.gethostbyname(host)
        print(f"Host: {host}")
        print(f"IP Address: {ip}")
        print("status: ONLINE")       
        return ip                      
    except socket.gaierror:
        print(f"Host: {host}")
        print("status: OFFLINE")
        return None


def get_http_info(sock, host):
     request = (
          f'GET / HTTP/1.1\r\n'
          f'Host: {host}\r\n'
          f'Connection: close\r\n'
          f'\r\n'
     )

     sock.sendall(request.encode())

     response = sock.recv(4096).decode(errors='ignore')

     headers = response.split('\r\n\r\n')[0]  # Get the headers part of the response
     lines = headers.splitlines()

     http_info = {
            'status_code': None,
            'status_message': None,
            'server': None,
            'content_type': None,  
            'content_length': None
        }

     print('\nHTTP Information:')

     if lines:
         status_parts = lines[0].split(' ', 2)

         if len(status_parts) >= 3:         #for the case where the status line is malformed
             http_info['status_code'] = status_parts[1]
             http_info['status_message'] = status_parts[2]

         print(f'   Status Code: {http_info["status_code"]}')
         print(f'   Status Message: {http_info["status_message"]}')


     for line in lines[1:]:
         if ':' in line:
             name, value = line.split(':', 1)

             if name.lower() == 'server':
                 http_info['server'] = value.strip()

             elif name.lower() == 'content-type':
                 http_info['content_type'] = value.strip()

             elif name.lower() == 'content-length':
                 http_info['content_length'] = value.strip()

             if name.lower() in ['server', 'content-type', 'content-length']:
                 print(f'   {name}: {value.strip()}')
                 
     return http_info      
                 
      


def scan_port(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)           # Set a timeout for the connection attempt

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = COMMON_PORTS.get(port, 'Unknown')
            print(f"Port {port} is open -> Service: {service}")
            
            result_data = {
            'port': port,
            'service': service
        }

        if port in [80, 8000, 8080]:
            http_info = get_http_info(sock, ip)
            result_data['http'] = http_info

        scan_results.append(result_data)

        sock.close()


if __name__ == "__main__":                      #run the program
    target = input("enter host check:")

    start_port = int(input('enter start port:'))
    end_port = int(input('enter end port:'))

    ip = check_host(target)

    if ip:
        print("\nstart port scanning...\n")

        with ThreadPoolExecutor(max_workers=50) as executor:
             for port in range(start_port, end_port + 1):        # This is a list of common ports to scan
                executor.submit(scan_port, ip, port)

        save_results()