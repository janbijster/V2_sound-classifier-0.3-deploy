#!/bin/bash
# Install berryconda
set -e

echo "Downloading Berryconda..."
wget -P ~/Downloads/ "https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh"
echo "Installing Berryconda..."
echo "You will first be asked to accept the terms."
echo "#################################################################################"
echo "## When prompted, choose to install in the default location and do add to PATH ##"
echo "#################################################################################"

sudo chmod +x ~/Downloads/Berryconda3-2.0.0-Linux-armv7l.sh
~/Downloads/Berryconda3-2.0.0-Linux-armv7l.sh
