SHELL := /bin/bash
PYTHON_VERSION = 3.5.1
PYTHON  = /opt/pyenv/versions/$(PYTHON_VERSION)/bin/python
PWD = $(shell pwd)

all: .python_version config.ini duckdns.service venv

.python_version:
	echo $(PYTHON_VERSION) > $@

venv: .python_version
	$(PYTHON) -m venv venv
	venv/bin/python -m pip install -r requirements.txt

config.ini: config-template.ini
	cp -i $< $@
	@echo "Make sure to set your values in config.ini"

/etc/systemd/system/duckdns.service: duckdns.service
	cp $< $@
	grep 'WorkingDirectory' $@ || \
		echo 'WorkingDirectory=$(PWD)' >> $@
	grep 'ExecStart' $@ || \
		echo 'ExecStart=/usr/bin/env "$(PWD)/venv/bin/python" duckdns.py' >> $@

/etc/systemd/system/duckdns.timer: duckdns.timer
	cp $< $@

install: config.ini /etc/systemd/system/duckdns.service /etc/systemd/system/duckdns.timer
	systemctl enable duckdns.timer
	systemctl start duckdns.timer

clean:
	$(RM) -r __pycache__

uninstall:
	$(RM) -r venv
	-systemctl stop duckdns.timer
	-systemctl disable duckdns.timer
	-systemctl stop duckdns.service
	-systemctl disable duckdns.service
	$(RM) /etc/systemd/system/duckdns.service
	$(RM) /etc/systemd/system/duckdns.timer


.PHONY: install all uninstall clean duckdns.service
