#!/bin/bash

echo ""
echo "****************************************"
echo " Setting up TDD/BDD Environment"
echo "****************************************"
echo ""

echo "Creating a Python virtual environment"
python3 -m venv ~/venv

echo "Configuring the developer environment..."
echo "# TDD/BDD Labs" >> ~/.bashrc
# sudo apt-get update
# sudo DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 chromium-chromedriver python3-selenium
echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc
echo "source ~/venv/bin/activate" >> ~/.bashrc

source ~/venv/bin/activate && pip install -r requirements.txt

echo ""
echo "****************************************"
echo " TDD/BDD Environment Setup Complete"
echo "****************************************"
echo ""
