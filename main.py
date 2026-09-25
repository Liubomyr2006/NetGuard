import socket


def check_host(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"Host: {host}")
        print(f"IP Address: {ip}")
        print("status: ONLINE")
    except socket.gaierror:
        print(f"Host: {host}")
        print("status: OFFLINE")


if __name__ == "__main__":
    target = input("enter host check:")
    check_host(target)