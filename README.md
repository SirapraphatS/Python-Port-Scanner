# PortScanner: A Python Network Security Scanner

SecuScan is a robust command-line utility built in Python to perform fast and informative port scanning and service detection, leveraging the power of the industry-standard **Nmap** tool.

This project showcases clean **Software Engineering** principles (CLI utility, robust error handling) and generates structured **JSON data**, making it ideal for immediate **Data Science** analysis of security posture.

## Key Features

* **Service & Version Detection:** Uses Nmap's `-sV` and `-sC` flags to identify running services and their versions—critical data for vulnerability assessment.
* **Command Line Interface (CLI):** Built with `argparse` for professional and easy command-line usage.
* **Robust Error Handling:** Includes checks for the Nmap binary and handles network scanning failures gracefully.
* **Structured Data Output:** Ability to save all scan results to a **JSON file** (`-o` flag) for subsequent data analysis and reporting.

## Prerequisites

Before running SecuScan, ensure you have the following installed:

1.  **Nmap Binary:** The core Nmap program must be installed on your operating system (e.g., via `apt-get`, `brew`, or Nmap installer).
2.  **Python 3.14**
3.  **`python-nmap` Library**

## Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR REPO URL HERE]
    cd [YOUR REPO FOLDER NAME]
    ```

2.  **Install Python Dependency:**
    ```bash
    python3.14 -m pip install -r requirements.txt
    ```
    *(Note: Ensure your `requirements.txt` only contains `python-nmap`)*

## Usage Examples

PortScanner requires a target IP address, IP range (CIDR), or domain name as the first argument.

### 1. Basic Scan (Display Results Only)

Run a basic scan and view the results directly in the console:

```bash
python SecuScan.py 45.33.32.156
```

### 2. Scan and Save Data (For Data Analysis)

Run the scan and save the detailed, machine-readable results into a JSON file for later processing (e.g., using Pandas or other Data Science tools):

```bash
python SecuScan.py 192.168.1.0/24 -o network_report_q4_2025.json
```

## Example

Here is a snippet of the console output when scanning a single host:

```bash
----------------------------------------------------------------------
[*] Starting up SecuScan on target: 45.33.32.156 (Options: -sV -sC -T4)
----------------------------------------------------------------------
HOST: 45.33.32.156 (Alias: scanme.nmap.org)
STATUS: UP
  --> PROTOCOL: TCP
    PORT: 22   STATE: *** OPEN ***
      SERVICE: ssh     VERSION: OpenSSH 7.9p1 Debian 10+deb10u2
    PORT: 80   STATE: *** OPEN ***
      SERVICE: http    VERSION: Apache httpd 2.4.38
----------------------------------------------------------------------
[*] Scan on 45.33.32.156 is DONE! Time to analyze the data.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
