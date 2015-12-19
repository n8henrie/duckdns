# [duckdns.py](https://github.com/n8henrie/duckdns)

A simple repo to set up my Raspberry Pi to use
[duckdns](https://www.duckdns.org).

## Dependencies

- Raspbian Jessie
- Python >= 3.4 (for `pyvenv`)

## Installation

1. `git clone`
1. `make`
1. Edit `config.ini`
1. `sudo make install`
1. Confirm the service file works: `sudo systemctl start duckdns.service && sudo
   journalctl -fx -b -u duckdns.service`
1. Confirm the timer works: `sudo journalctl -fx -b -u duckdns.timer`
    - Should run every hour by default
