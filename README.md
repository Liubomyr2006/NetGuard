# NetGuard

NetGuard is a command-line TCP port scanner written in Python. It checks a specified port range and reports ports where a TCP connection succeeds.

## Current features

- Scans a user-specified TCP port range on a hostname or IP address.
- Supports IPv4 and IPv6 addresses resolved by the operating system.
- Configurable connection timeout.
- Reports open ports in the terminal.
- Includes local unit tests for open and closed ports.

NetGuard currently checks TCP connectivity only. It does **not** identify services or versions, scan UDP ports, or guarantee that a failed connection means a port is closed; firewalls and network conditions can affect results. Scanning is sequential.

## Requirements

- Python 3.14

## Usage

Run commands from the project root.

On Windows, if Python is not available as `python`, use its full path:

```powershell
& "C:\Users\lolk1\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m netguard localhost --ports 8000-9000
```

Scan a specific authorized host and port range:

```powershell
& "C:\Users\lolk1\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m netguard 192.0.2.10 --ports 20-100 --timeout 1.0
```

Replace `192.0.2.10` with a host you own or are explicitly authorized to test. The example address is reserved for documentation and is not a real target.

Show available options:

```powershell
& "C:\Users\lolk1\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m netguard --help
```

`--ports` is required. Port ranges must be between 1 and 65535, with the start port less than or equal to the end port. `--timeout` is a positive number of seconds and defaults to `1.0`.

## Run the tests

From the project root:

```powershell
& "C:\Users\lolk1\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m unittest discover -s tests -v
```

## Project structure

```text
netguard/
    __main__.py
    cli.py
    scanner/
        port_scanner.py
tests/
    test_port_scanner.py
```

## Authorized use

Use NetGuard only on systems and networks you own or have explicit permission to test. You are responsible for following applicable laws, policies, and rules of engagement.
