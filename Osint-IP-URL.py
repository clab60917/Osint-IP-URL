import subprocess
import time
import socket

def ping(ip_address):
    res = subprocess.call(["ping", "-c", "1", "-t", "200", ip_address], stdout=subprocess.PIPE)
    return res == 0

def scan_ips(ip_addresses):
    while True:
        print("Scanning IPs...")
        for ip_address in ip_addresses:
            if ping(ip_address):
                print(f"{ip_address} is UP")
            else:
                print(f"{ip_address} is down")
        stop_input = input("Type 'stop' to exit the program, or press enter to continue.")
        if stop_input == "stop":
            break
        time.sleep(5)

def scan_urls(urls):
    while True:
        print("Scanning URLs...")
        for url in urls:
            try:
                ip_address = socket.gethostbyname(url)
                if ping(ip_address):
                    print(f"{url} ({ip_address}) is UP")
                else:
                    print(f"{url} ({ip_address}) is down")
            except socket.gaierror:
                print(f"Could not resolve hostname: {url}")
        stop_input = input("Type 'stop' to exit the program, or press enter to continue.")
        if stop_input == "stop":
            break
        time.sleep(5)

while True:
    print("Select an option:")
    print("1. Scan IP addresses")
    print("2. Scan URLs")
    option_input = input("Enter an option number: ")
    if option_input == "1":
        ip_addresses = input("Enter IP addresses to scan (separated by spaces): ").split()
        scan_ips(ip_addresses)
    elif option_input == "2":
        urls = input("Enter URLs to scan (separated by spaces): ").split()
        scan_urls(urls)
    else:
        print("Invalid option.")
