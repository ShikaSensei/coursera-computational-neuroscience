"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""
#from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pickle
from compute_sta import compute_sta

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

# stimulus vector
stim = data['stim']
# spike/no spike vector
# 1 - spike
# 0 - no spike
rho = data['rho']

# Sampling rate in Hz
sampling_rate = 500
# Time before spike in ms
tbs = 300

# Time between adjacent samples
sampling_period = round(1/sampling_rate * 1000)
# sta vector dimension
num_timesteps = round(tbs/sampling_period)

# spike triggered average vector
sta = compute_sta(stim, rho, num_timesteps)
# time vector
time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
