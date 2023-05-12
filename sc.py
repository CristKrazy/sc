#TOOL SCAN PORT
#Code by Krazy

import pyfiglet
import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

ascii_banner = pyfiglet.figlet_format("SCAN PORT")
print(ascii_banner)

target = input(str("[-] IP: "))

print("-" * 50)
print("Scanning Ports of IP: " + target)
print("Starting Scanning at: " + str(datetime.now()))
print("-" * 50)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[-] Port {port} is open")
    s.close()

try:
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(scan_port, port) for port in range(10000, 20000)]
        for future in as_completed(futures):
            # wait for all tasks to finish
            pass

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.error:
    print("Can't connect to host :(")
    sys.exit()
