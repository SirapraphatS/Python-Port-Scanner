# PortScanner: A Friendly Python Network Explorer

Hey there! This **PortScanner** is a simple and reliable tool built with Python to help you check networks and find out what services are running. It uses the powerful **Nmap** tool quietly in the background.

---

## What This Tool Does (Key Features)

* **Finds Services & Versions:** It uses Nmap flags (`-sV`, `-sC`) to identify the exact service (like 'Apache') and its version. This is the first step in any security check!
* **Simple Command Line Use (CLI):** It uses `argparse` so you can run it easily without changing the code.
* **Built-in Safety Checks:** It checks for common errors (like missing Nmap) so the program doesn't crash.
* **Data Ready:** You can save the full report to a **JSON file** (`-o` flag) for easy data processing.

---

## Get Ready (Prerequisites)

Before you start scanning, please make sure you have these installed:

1.  **Nmap Binary:** You need the main Nmap program on your system (get it via `apt-get`, `brew`, or the Nmap installer).
2.  **Python 3.14** (or any 3.x version you use).
3.  **`python-nmap` Library:** This is the Python code that talks to Nmap.

### Installation & Setup

1.  **Get the Code:**
    ```bash
    git clone [YOUR REPO URL HERE]
    cd [YOUR REPO FOLDER NAME]
    ```

2.  **Install the Library:**
    ```bash
    python3.14 -m pip install -r requirements.txt
    ```

---

## How to Use It (Usage Examples)

You just need to tell the PortScanner what IP or domain you want to check.

### 1. Simple Check (View on Screen)

Just run the scan and see the results right away in your terminal:

```bash
python PortScanner.py 45.33.32.156
````

### 2\. Scan and Save (Data Science Prep)

If you want the data for later analysis (maybe with Pandas\!), use the `-o` flag:

```bash
python PortScanner.py 192.168.1.0/24 -o network_report_2025.json
```

-----

## Example Output (What You See)

This is what a successful scan looks like when you run it:

```bash
----------------------------------------------------------------------
[+] Starting the scan on 45.33.32.156 now.
----------------------------------------------------------------------
HOST IP: 45.33.32.156 (Name: scanme.nmap.org)
STATUS: UP (The host is reachable)
  -> Checking PROTOCOL: TCP
    PORT: 22   STATE: *** OPEN ***
      SERVICE: ssh     VERSION: OpenSSH 7.9p1 Debian 10+deb10u2
    PORT: 80   STATE: *** OPEN ***
      SERVICE: http    VERSION: Apache httpd 2.4.38
----------------------------------------------------------------------
[*] Scan finished for 45.33.32.156. Have a good day! 👋
```

-----

## 📜 License

This project is open source and uses the **MIT License**. Feel free to use and build upon it\! (See the `LICENSE` file for full details.)
