# Tor Port Scan

For this script to work, you need to install some dependencies, the following is for kali linux.
  1. ```bash
     sudo apt install tor
     ```
  2. ```bash
     nano /etc/tor/torrc
     ```
  3.    uncomment '`ControlPort 9051`'
  4. ```bash
     sudo systemctl restart tor
     ```
  5. ```bash
     sudo systemctl start tor
     ```
  6. ```bash
      pip3 install -r requirements.txt
     ```


### Usage
  1. `python3 scan.py -h` # help and more information
  2. `python3 scan.py <TARGET>` # standard port scan, changing IP address every 5 ports scaned
  3. `python3 scan.py --tor-interval <TARGET>` # default is 5. The number of ports scanned before the TOR IP address is changed
  4. `-t` TIMEOUT, `--timeout` TIMEOUT seconds to wait before connection timeout for each port
  5. `j` JOBS, `--jobs` JOBS  maximum number of open connections at the same time
