import socket
import unittest

from netguard.scanner.port_scanner import scan_port, scan_ports


class ScanPortTests(unittest.TestCase):
    def test_returns_true_for_open_local_port(self):
        # This test assumes that port 80 is open on localhost. Adjust as needed.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0)) #bind to an available port
            server.listen()
            port = server.getsockname()[1]

            self.assertTrue(
                scan_port("127.0.0.1", port, timeout=1.0)
            )

    def test_returns_false_for_closed_local_port(self):
        # this test assumes that port 9999 is closed on localhost,adjust as needed
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as reservation:
            reservation.bind(("127.0.0.1", 0))
            port = reservation.getsockname()[1]

            self.assertFalse(scan_port("127.0.0.1", port, timeout=1.0)
            )

    def test_scan_ports_returns_open_ports(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))  # Bind to an available port
            server.listen()
            port = server.getsockname()[1]

            self.assertEqual(
                scan_ports("127.0.0.1", port, port, timeout=1.0),
                [port],
            )


if __name__ == "__main__":
    unittest.main()