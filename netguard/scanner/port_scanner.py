import socket
import time
import math

from concurrent.futures import ThreadPoolExecutor, as_completed

from ..models import ScanResult, ScanState


def scan_port(
        host: str,
        port: int,
        timeout: float = 1.0,
    ) -> ScanResult:

    if not host:
        raise ValueError("Host Cannot be empty")

    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError("Port must be between 1 and 65535")

    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be positive and f")

    start_time = time.perf_counter()

    try:
        with socket.create_connection((host, port), timeout=timeout):
            state = ScanState.OPEN
            error = None

    except ConnectionRefusedError:
        state = ScanState.CLOSED
        error = None

    except TimeoutError:
        state = ScanState.FILTERED
        error = "Connection timed out"

    except OSError as exc:
        state = ScanState.ERROR
        error = f"{type(exc).__name__}: {exc}"

    response_time = time.perf_counter() - start_time

    return ScanResult(
        host=host,
        port=port,
        state=state,
        response_time=response_time,
        error=error,
    )



def scan_ports(
        host: str,
        start_port: int,
        end_port: int,
        timeout: float = 1.0,
        max_workers: int = 100
) -> list[ScanResult]:

    if not host:
        raise ValueError("Host cannot be empty")

    if not (1 <= start_port <= end_port <= 65535):
        raise ValueError(f"Invalid port range")

    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("Timeout must be positive and finite")

    if not (1 <= max_workers <= 200):
        raise ValueError("Workers must be between 1 and 200")

    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        futures = {
            executor.submit(scan_port, host, port, timeout): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port = futures[future]

            try:
                result = future.result()

            except Exception as exc:
                result = ScanResult(
                    host=host,
                    port=port,
                    state=ScanState.ERROR,
                    error=f"{type(exc).__name__}: {exc}",
                )

            results.append(result)
    
    return sorted(results, key=lambda result: result.port)