# NetGuard

**A Python-based network security and port scanning tool.**

NetGuard is an educational cybersecurity project designed to explore network scanning, TCP connections, security-oriented programming, and modular Python architecture.

The project focuses on building a reliable and maintainable port scanner with structured scan results, input validation, and automated testing.

## Features

- **TCP Port Scanning** — Scan a specified host across a configurable port range.
- **Concurrent Scanning** — Use Python's `ThreadPoolExecutor` for efficient port scanning.
- **Port Validation** — Validate port numbers and connection timeouts.
- **Structured Results** — Represent scan outcomes using dedicated `ScanResult` and `ScanState` models.
- **Scan States** — Distinguish between open, closed, and error states.
- **CLI Interface** — Interact with the scanner through a command-line interface.
- **Automated Testing** — Unit tests for scanner functionality and result handling.

## Project Structure

```text
NetGuard/
│
├── netguard/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── scan_result.py
│   │
│   ├── scanner/
│   │   └── port_scanner.py
│   │
│   └── cli.py
│
├── tests/
│   └── test_port_scanner.py
│
├── .gitignore
└── README.md
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Socket | TCP connection handling |
| ThreadPoolExecutor | Concurrent scanning |
| Dataclasses | Structured scan results |
| Enum | Scan state management |
| Unittest | Automated testing |
| Git | Version control |

## Installation

Clone the repository:

```bash
git clone https://github.com/Liubomyr2006/NetGuard.git
```

Navigate to the project directory:

```bash
cd NetGuard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

No external dependencies are currently required for the core scanner.

## Running Tests

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

Check the repository for whitespace errors:

```bash
git diff --check
```

## Architecture

NetGuard follows a modular architecture that separates scanning logic, data models, and user interaction.

**Models**

Responsible for representing scan results and their states.

- `ScanResult` — Stores information about an individual port scan.
- `ScanState` — Defines the possible outcomes of a scan.

**Scanner**

Responsible for TCP connection handling, port validation, and scanning operations.

**CLI**

Provides a command-line interface for interacting with the scanning functionality.

**Tests**

Verify scanner behavior, input validation, and correct handling of open and closed ports.

## Development Roadmap

- [x] Initial TCP port scanner
- [x] Concurrent port scanning
- [x] Structured scan result model
- [x] Scan state enumeration
- [x] Port and timeout validation
- [x] Unit tests for core scanning functionality
- [x] Modular project architecture
- [ ] Extended error handling
- [ ] Improved CLI experience
- [ ] Logging system
- [ ] JSON and structured scan reports
- [ ] Network discovery
- [ ] Service identification
- [ ] Security analysis and reporting

## Security & Ethical Use

NetGuard is intended for educational purposes and authorized security testing.

Only scan systems and networks that you own or have explicit permission to test.

Unauthorized scanning may violate applicable laws or organizational policies.

## Project Status

<ins>Active Development</ins>

NetGuard is currently undergoing core architecture improvements, with a focus on reliability, clean code organization, and test coverage.

New features will be introduced incrementally as the underlying components become stable.

## Author

**LiboDar**

GitHub: [@Liubomyr2006](https://github.com/Liubomyr2006)

---