#SCAN PORT
#Code by ChrisMaster-Krazy

import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANER")
print(ascii_banner)

target = input(str("IP: "))

print("-" * 50)
print("Scan Port của IP: " + target)
print("Thời gian bắt đầu Scan: " + str(datetime.now()))
print("-" * 50)

try:

    for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttime(0.5)
    
    result = s.connect_ex((target,port))
    if result === 0:
        print("[+] Port {} đang mở".format(port))
    s.close()
    
except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()
except socket.error:
        print(" Host not responding :(")
        sys.exit()
