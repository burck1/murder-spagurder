#!/usr/bin/env bash

if [ ! -d "env" ]; then
  /usr/local/bin/python3 -m venv env
  source env/bin/activate
  python -m pip install -U pip
  python -m pip install -r requirements.txt
fi
