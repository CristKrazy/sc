import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from termcolor import colored
import pyfiglet
import socket
import itertools
import time

ascii_banner = pyfiglet.figlet_format('SCANER - PORT')
colored_banner = colored(ascii_banner, color='red')
author_info = colored('version 0.1', color='cyan')
version_info = colored('Code by Krazy', color='blue')
print(f"{colored_banner}{author_info.rjust(len(colored_banner) - len(author_info))}")
print(f"{version_info.center(len(colored_banner))}\n")

scanning_text = colored('TOOLS SCANNING PORT', color='green')
print(scanning_text)

target = input('[-] IP: ')

print('-' * 50)
print(f'Scanning Ports of IP: {target}')
print(f'Starting Scanning at: {str(datetime.now())}')
print('-' * 50)

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 40960)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 40960)
        s.settimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'[-] Port {port} is open')
            counter = itertools.cycle(['[+] W..', '[-] Wa...', '[+] Wai....', '[-] Wait.....'])
            while True:
                print(next(counter), end='\r')
                time.sleep(1)
        s.close()

try:
    with ThreadPoolExecutor(max_workers=50000) as executor:
        futures = [executor.submit(scan_port, port) for port in range(1, 65536)]
        for future in as_completed(futures):
            pass

except KeyboardInterrupt:
    print('\nExiting program.')
    sys.exit()

except socket.error:
    print('Can\'t connect to host :(')
    sys.exit()

print('[-] End scanning.')