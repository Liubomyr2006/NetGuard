# NetGuard

A lightweight Python network security scanner.

## Features

* Check whether a host is reachable
* Resolve hostnames to IP addresses
* Scan network ports
* Display open ports
* Generate scan results

* NetGuard can currently in 0.6 version:

- Check whether a host is reachable
- Resolve hostnames to IP addresses
- Scan TCP ports
- Scan custom port ranges
- Scan ports using multithreading
- Detect HTTP services by sending an HTTP request
- Parse HTTP response information
- Detect services independently from the port number
- Save scan results to JSON

## Technologies

* Python
* Git
* GitHub
* Networking
* TCP/IP

## Installation

Clone the repository:

```bash
git clone https://github.com/Liubomyr2006/NetGuard.git
cd NetGuard
```

Run the scanner:

```bash
python main.py
```

## Project Status

Currently in development.

The first version can resolve a hostname and check whether it is reachable.

## Roadmap

- [x] Basic host check
- [x] TCP port scanner
- [x] Custom port range
- [x] Multithreading
- [x] HTTP service detection
- [x] HTTP response parsing
- [x] JSON reports
- [ ] SSH detection
- [ ] FTP detection
- [ ] SMTP detection
- [ ] Generic service detection
- [ ] CLI arguments
- [ ] Logging
- [ ] Unit tests
- [ ] Docker
- [ ] CI/CD with GitHub Actions

## Disclaimer

This project is intended for educational purposes and authorized security testing only.
