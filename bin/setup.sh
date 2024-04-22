#!/bin/bash

echo ""
echo "****************************************"
echo " Setting up TDD/BDD Environment"
echo "****************************************"
echo ""

echo "Configuring the developer environment..."
echo "# TDD/BDD Labs" >> ~/.bashrc
sudo apt update
sudo apt upgrade
echo "export PATH=$HOME/local/bin:$PATH" >> ~/.bashrc
echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc

echo "Setting up and running Chrome and Selenium for BDD on the ubuntu 22.04"
echo "# BDD Lab Additions" >> ~/.bashrc
echo "Download chrome stable package"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
echo "Install google-chrome"
sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt -f install && sudo dpkg -i google-chrome-stable_current_amd64.deb
echo ""
echo "Chrome Installed:"
google-chrome --version
echo ""

echo "Creating a Python virtual environment"
python3 -m venv ~/venv
echo "source ~/venv/bin/activate" >> ~/.bashrc
source ~/venv/bin/activate && pip install -r requirements.txt

echo ""
echo "Starting the Postgres Docker container..."
make app

echo ""
echo "****************************************"
echo " TDD/BDD Environment Setup Complete"
echo "****************************************"
echo ""
