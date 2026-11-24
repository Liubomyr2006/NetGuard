import argparse
import socket
import math

from .scanner.port_scanner import scan_ports
from .models import ScanState


def resolve_addresses(target: str) -> list[str]:
    try:
        records = socket.getaddrinfo(target, 0, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise ValueError(f"Could not resolve target {target!r}: {exc}") from exc

    addresses = []
    for record in records:
        address = record[4][0]
        if address not in addresses:
            addresses.append(address)

    if not addresses:
        raise ValueError(f'No IP addresses found for target {target!r}')

    return addresses



def main():
    parser = argparse.ArgumentParser(
        prog='NetGuard',
        description='Network scanning and service detection tool!'
    )

    parser.add_argument(
        "target",
        help="target hostname or ip address"
    )

    parser.add_argument(
        "--ports",
        required=True,
        help="Port range to scan e.g 1-1000" 
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="connection timeout in seconds (default 1.0)",
    )

    args = parser.parse_args()

    try:
        start_port, end_port = map(int, args.ports.split('-', maxsplit=1))
        if not (1 <= start_port <= end_port <= 65535):
            raise ValueError
    except ValueError:
        parser.error('Invalid port range. Example: --ports 1-1000')

    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error('--timeout must be a positive number')

    try:
        addresses = resolve_addresses(args.target)
    except ValueError as exc:
        parser.error(str(exc))

    open_ports = set()

    for address in addresses:
        results = scan_ports(
            address,
            start_port,
            end_port,
            timeout=args.timeout,
        )

        open_ports.update(
            result.port
            for result in results
            if result.state == ScanState.OPEN
        )

    print(f'target: {args.target}')
    print(f'ports: {start_port}-{end_port}')

    if open_ports:
        print(f'open ports: {",".join(map(str, sorted(open_ports)))}')
    else:
        print('NO OPEN ports found')

if __name__ == "__main__":
    main() 