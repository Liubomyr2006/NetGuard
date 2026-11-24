import socket
import unittest

from unittest.mock import patch
from netguard.models import ScanResult, ScanState
from netguard.scanner.port_scanner import scan_port, scan_ports


class ScanPortTests(unittest.TestCase):

    
    def test_returns_open_for_open_local_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0)) 
            server.listen()

            port = server.getsockname()[1]

            result = scan_port("127.0.0.1", port)

            self.assertIsInstance(result, ScanResult)
            self.assertEqual(result.state, ScanState.OPEN)
            self.assertEqual(result.port, port)
            self.assertIsNotNone(result.response_time)


    def test_returns_closed_for_closed_local_port(self):
        with patch(
            "netguard.scanner.port_scanner.socket.create_connection",
            side_effect=ConnectionRefusedError
        ):
            result = scan_port("127.0.0.1", 12345)

        self.assertEqual(result.state, ScanState.CLOSED)
        self.assertIsNone(result.error)


    def test_scan_ports_returns_scan_results(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen()

            port = server.getsockname()[1]

            results = scan_ports("127.0.0.1", port, port)

            self.assertEqual(len(results), 1)
            self.assertIsInstance(results[0], ScanResult)
            self.assertEqual(results[0].state, ScanState.OPEN)


    def test_scan_ports_returns_sorted_results(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen()

            port = server.getsockname()[1]

            results = scan_ports("127.0.0.1", port, port + 1)

            ports = [result.port for result in results]

            self.assertEqual(ports, sorted(ports))


    def test_invalid_port_raises_value_error(self):
        with self.assertRaises(ValueError):
            scan_port("127.0.0.1", 0)


    def test_invalid_timeout_raises_value_error(self):
        with self.assertRaises(ValueError):
            scan_port("127.0.0.1", 80, timeout=0)


    def test_scan_ports_rejects_invalid_workers(self):
        with self.assertRaises(ValueError):
            scan_ports("127.0.0.1", 80, 80, max_workers=0)


if __name__ == "__main__":
    unittest.main()