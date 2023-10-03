# tor_port_scan

For this script to work, you need to install some dependencies, the following is for kali linux.
  1. sudo apt install tor
  2. nano /etc/tor/torrc
  2a. uncomment 'ControlPort 9051'
  3. sudo systemctl restart tor
  4. sudo systemctl start tor
  5. pip3 install -r requirements.txt
