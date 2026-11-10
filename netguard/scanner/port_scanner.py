import socket
import math

from concurrent.futures import ThreadPoolExecutor, as_completed


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
        max_workers: int = 100
) -> list[int]:

    if not host:
        raise ValueError("Host cannot be empty")

    if not (1 <= start_port <= end_port <= 65535):
        raise ValueError(f"Invalid port range")

    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("Timeout must be positive and finite")

    if not (1 <= max_workers <= 200):
        raise ValueError("Workers must be between 1 and 200")

    open_ports = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        futures = {
            executor.submit(scan_port, host, port, timeout): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port = futures[future]

            if future.result():
                open_ports.append(port)
    

    return sorted(open_ports)