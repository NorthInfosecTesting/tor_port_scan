# Tor Port Scan

For this script to work, you need to install some dependencies, the following is for kali linux.
  1. ```bash
     sudo apt install tor
     ```
  4. `nano /etc/tor/torrc` and uncomment '`ControlPort 9051`'
  5. `sudo systemctl restart tor`
  6. `sudo systemctl start tor`
  7. `pip3 install -r requirements.txt`
