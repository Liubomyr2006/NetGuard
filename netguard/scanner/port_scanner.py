import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True 

    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def scan_ports(
        host: str,
        start_port: int,
        end_port: int,
        timeout: float = 1.0,
) -> list[int]:
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port, timeout=timeout):
            open_ports.append(port)


    return open_ports