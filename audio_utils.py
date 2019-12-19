import sounddevice as sd
import os
import numpy as np

# default params
sample_rate = 22050
default_sample_length_sec = 4

# initialize
sd.default.samplerate = sample_rate
sd.default.channels = 1

# functions
def start_recording(trim_start_sec=0, sample_length_sec=default_sample_length_sec):
    recording = sd.rec(int((sample_length_sec + trim_start_sec) * sample_rate))
    return recording

def end_recording(recording, trim_start_sec):
    sd.wait()
    return recording[int(trim_start_sec * sample_rate):, :]

def get_recording(trim_start_sec=0, sample_length_sec=default_sample_length_sec):
    recording = start_recording(trim_start_sec, sample_length_sec)
    return end_recording(recording, trim_start_sec)

def test_recording():
    recording = get_recording()
    for val in recording:
        print('#' * int(val * 80))

def list_devices(return_list = False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\nAvailable audio devices:\n')
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print('{}: {}'.format(i, device['name']))
    if return_list:
        return devices
    else:
        print('\nFind the audio device you want to use in the list above\n(e.g. "USB PnP Sound Device")\nand write down the card number\n(e.g. "hw:1,0")')
    
def set_device():
    devices = list_devices(True)
    device_choice = input('\nSelect device number (0-{}): '.format(len(devices) - 1))
    try:
        sd.default.device = devices[int(device_choice)]['name']
    except Exception as e:
        print('Couldn\'t det device to {}'.format(device_choice))
        exit(e)

def overlap_recording(current_recording, recordings, sample_length_sec=default_sample_length_sec):
    # if there is already a recording, then store also the overlap with the previous one:
    if len(recordings) != 0:
        previous_recording = recordings[-1]
        overlap_samples = int(0.5 * sample_length_sec * sample_rate)
        overlap_recording = np.vstack((previous_recording[overlap_samples:], current_recording[:overlap_samples]))
        recordings = [overlap_recording, current_recording]
    else:
        recordings = [current_recording]
    return recordings

def end_recording_and_overlap(recording, recordings=[], trim_start_sec=0, sample_length_sec=default_sample_length_sec):
    current_recording = end_recording(recording, trim_start_sec)
    return overlap_recording(current_recording, recordings, sample_length_sec)

def add_recording_and_overlap(recordings=[], trim_start_sec=0, sample_length_sec=default_sample_length_sec):
    current_recording = get_recording(trim_start_sec, sample_length_sec)
    return overlap_recording(current_recording, recordings, sample_length_sec)