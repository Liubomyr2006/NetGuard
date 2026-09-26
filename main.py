import socket
from concurrent.futures import ThreadPoolExecutor


COMMON_PORTS = {     
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy",
}  #List of common ports and their services


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

     print("HTTP Response:")
     print(response[:500]) # Print the first 500 characters of the response
    



def scan_port(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = COMMON_PORTS.get(port, 'Unknown')
            print(f"Port {port} is open -> Service: {service}")

            if port == 80:
                get_http_info(sock, ip)
                 

            try:
                banner = sock.recv(1024)
                print(f'Banner: {banner.decode(errors='ignore').strip()}')
            except socket.timeout:
                print("No banner received.")
        
            sock.close()


if __name__ == "__main__":                      #run the program
    target = input("enter host check:")

    start_port = int(input('enter start port:'))
    end_port = int(input('enter end port:'))

    ip = check_host(target)

    if ip:
        print("\nstart port scanning...\n")

with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):  # This is a list of common ports to scan
            executor.submit(scan_port, ip, port)