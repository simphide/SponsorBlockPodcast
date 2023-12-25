#!/bin/bash

if [[ $(pgrep -f 'python3 main.py') ]]; then
	exit 0
else
	exit 1
fi
