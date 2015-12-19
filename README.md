# [duckdns.py](https://github.com/n8henrie/duckdns)

A simple repo to set up my Raspberry Pi to use
[duckdns](https://www.duckdns.org).

## Dependencies

- Raspbian Jessie
- Python >= 3.4 (for `pyvenv`)
    - May need to `sudo apt-get install python3-venv` on some systems

## Installation

1. `git clone`
1. Edit `Makefile`:
    - Change `PYTHON_VERSION` as needed if using [pyenv](https://github.com/yyuu/pyenv)
    - If not using `pyenv`, either change `PYTHON` or set it when calling
      `make`
1. `make` (or `PYTHON=/usr/bin/python3 make` if needed)
1. Edit `config.ini` with your duckdns info
1. `sudo make install`
1. Confirm the service file works: `sudo systemctl start duckdns.service && sudo
   journalctl -fx -b -u duckdns.service`
1. Confirm the timer works: `sudo journalctl -fx -b -u duckdns.timer`
    - Should run every hour by default
