import nmap
import argparse
import sys
import json 
from typing import Dict, Any

# --- Project Settings ---
# We use these settings for the Nmap tool. -sV helps find service versions.
# -T4 makes the scan faster.
NMAP_OPTIONS = "-sV -sC -T4" 

def save_data_to_json(data: Dict[str, Any], filename: str) -> None:
    """
    This function writes the scan results into a JSON file.
    It helps you keep your data organized for later study.
    """
    try:
        with open(filename, 'w') as f:
            # We save the data with spaces (indent=4) so it's easy to read.
            json.dump(data, f, indent=4) 
        print(f"\n[+] Success! The scan report is saved in: {filename}")
    except Exception as e:
        print(f"\n[!] Sorry, there was an issue saving the file. Error: {e}")

def run_scan(target_ip: str, output_file: str = None) -> None:
    """
    This function starts the port scanning job.
    """
    
    # Create the Nmap scanner object. This is our main tool.
    nm = nmap.PortScanner()
    
    print(f"\n[+] Starting the scan on {target_ip} now. Options used: {NMAP_OPTIONS}")
    print("-" * 70)
    
    try:
        # Run the scan command. We add a timeout so the program doesn't freeze.
        nm.scan(target_ip, arguments=NMAP_OPTIONS + " --host-timeout 15m --max-retries 1")
    except nmap.PortScannerError as e:
        print(f"[!!!] Scan Failed. Did you install Nmap correctly? Problem: {e}")
        sys.exit(1) 
    except Exception as e:
        print(f"[!!!] An unexpected problem happened. Error: {e}")
        sys.exit(1)
        
    # --- Reading the Scan Results ---
    for host in nm.all_hosts():
        
        # Get the hostname; use 'No name' if it's not found.
        hostname = nm[host].hostname() if nm[host].hostname() else "No name"
        
        print(f"\n----------------------------------------------------------------------")
        print(f"HOST IP: {host} (Name: {hostname})")
        print(f"STATUS: {nm[host].state().upper()} (The host is reachable)")
        
        for protocol in nm[host].all_protocols():
            print(f"  -> Checking PROTOCOL: {protocol.upper()}")
            port_info = nm[host][protocol]
            
            # Look at each port one by one.
            for port, data in port_info.items():
                
                service = data.get('name', 'Unknown')
                version_raw = data.get('product', '') + ' ' + data.get('version', '')
                state = data['state'].upper()
                
                # Highlight if the port is OPEN. This is important information.
                display_state = f"*** {state} ***" if state == 'OPEN' else state
                
                print(f"    PORT: {port:<5}\tSTATE: {display_state}")
                print(f"      SERVICE: {service:<10}\tVERSION: {version_raw.strip()}")
                
                # If Nmap scripts ran, print the extra details.
                if 'script' in data and data['script']:
                    print("      [+] Extra Script Info:")
                    for script_name, script_output in data['script'].items():
                         print(f"        -> {script_name}: {script_output}")
    
    # --- Saving the Data ---
    if output_file:
        # Get all the data from the scanner for the final report.
        full_json_data = nm.analyse_nmap_xml_scan()
        save_data_to_json(full_json_data, output_file)

    print("\n" + "=" * 70)
    print(f"[*] Scan finished for {target_ip}. Have a good day! 👋")


def main():
    """Sets up how you use the program from the command line."""
    parser = argparse.ArgumentParser(
        description="PortScanner: A simple, quiet tool for checking network ports.",
        epilog="Use: python PortScanner.py 45.33.32.156 -o report.json"
    )
    
    # This is the required target IP or domain.
    parser.add_argument(
        "target", 
        help="The IP address or domain name you want to scan (e.g., 8.8.8.8)."
    )
    
    # This is the optional file name for saving the results.
    parser.add_argument(
        "-o", "--output", 
        help="Optional: Filename to save the results in JSON format.", 
        required=False
    )
    
    args = parser.parse_args()
    
    run_scan(args.target, args.output)

if __name__ == "__main__":
    # Check: We need the Nmap program on the system to run this script.
    try:
        nmap.PortScanner() 
    except nmap.PortScannerError:
        print("[!] ERROR: The Nmap program is missing! Please install it first.")
        sys.exit(1)
        
    main()