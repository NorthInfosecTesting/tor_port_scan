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
