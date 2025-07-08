#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Environment setup complete. Activate with 'source env/bin/activate'"
