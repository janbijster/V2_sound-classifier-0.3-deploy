#!/bin/bash
# Install the required packages and python environment for the audio classifier to work
set -e

echo "Installing encoders and audio drivers..."
sudo apt-get install ffmpeg libavcodec-extra libjpeg-dev zlib1g-dev

echo "Installing numba..."
conda install -c numba numba

echo "Installing scipy, numpy, matplotlib, scikit-learn and h5py..."
conda install scipy numpy scikit-learn matplotlib h5py

echo "Installing pip..."
conda install pip

echo "Installing python packages..."
pip install librosa Keras==2.2.4 tensorflow==1.13.1 Pillow pydub

echo "Installing portaudio and pyaudio"
sudo apt install portaudio19-dev
pip install pyaudio
