import sys
import argparse
import socket
from ipaddress import ip_address
import threading
import stem
from stem import Signal
from stem.control import Controller

# List of the top 100 ports to scan
TOP_100_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
    143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080,
    1720, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668,
    6669, 1433, 3128, 3306, 3389, 5432, 5900, 5901, 5902, 5903,
    5904, 5905, 5906, 5907, 5908, 5909, 6379, 8080, 8081, 8082,
    8083, 8084, 8085, 8086, 8087, 8088, 8089, 9090, 9091, 9092,
    9093, 9094, 9095, 9096, 9097, 9098, 9099, 9100, 9101, 9102,
    9103, 9104, 9105, 9106, 9107, 9108, 9109, 9110, 9111, 9112,
    9113, 9114, 9115, 9116, 9117, 9118, 9119, 9120, 9121, 9122,
    9123, 9124, 9125, 9126, 9127, 9128, 9129, 9130, 9131, 9132,
    9133, 9134, 9135, 9136, 9137, 9138, 9139, 9140, 9141, 9142,
]

def connScan(host, port, wait, openports):
    try:
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.settimeout(wait)
        sckt.connect((host, port))
        sckt.close()
        openports.append(port)
    except (ConnectionRefusedError, socket.timeout):
        pass

def change_tor_address():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
        print("Tor address changed successfully.")
    except Exception as e:
        print("Error changing Tor address:", e)

def portScan(host, wait, jobs, tor_change_interval):
    openports = []
    threads = []

    for p in TOP_100_PORTS:
        while threading.active_count() >= jobs + 1:
            pass

        thread = threading.Thread(target=connScan, args=(host, p, wait, openports))
        threads.append(thread)
        thread.start()

        # Change Tor address every tor_change_interval ports
        if p % tor_change_interval == 0:
            change_tor_address()


    for thread in threads:
        thread.join()

    return openports

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="IP address or domain to scan")
    parser.add_argument("-t", "--timeout", metavar="TIMEOUT", type=int, help="seconds to wait before connection timeout for each port", default=3)
    parser.add_argument("-j", "--jobs", metavar="JOBS", type=int, help="maximum number of open connections at the same time", default=10)
    parser.add_argument("--tor-interval", metavar="TOR_INTERVAL", type=int, help="change Tor address every N ports", default=5)

    args = parser.parse_args()

    host = args.host
    wait_time = args.timeout
    jobs = args.jobs
    tor_change_interval = args.tor_interval

    open_ports = portScan(host, wait_time, jobs, tor_change_interval)

    if open_ports:
        print("Open ports on {}: {}".format(host, open_ports))
    else:
        print("No open ports found on {}".format(host))

if __name__ == "__main__":
    main()
