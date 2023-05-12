#SCAN PORT
#Code by ChrisMaster-Krazy

import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("SCAN PORT")
print(ascii_banner)

target = input(str("[-] IP: "))

print("-" * 50)
print("Scanning Ports of IP: " + target)
print("Starting Scanning at: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(10000 ,20000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[-] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

except socket.error:
        print("Can't connect to host :(")
        sys.exit()
