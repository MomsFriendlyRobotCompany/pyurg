#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
import pyurg
import numpy as np
import matplotlib.pyplot as plt

def getData(urg):
	data =[]
	while len(data) == 0:
		data, timestamp = urg.capture()
		print('Data', len(data), timestamp)
	return data

def averageData(urg, cnt=5):
	sets = []
	num = 1000000
	for i in range(cnt):
		data = getData(urg)
		num = min(num, len(data))
		sets.append(data)

	data = []
	for i in range(num):
		d = 0
		for j in range(cnt):
			d += sets[j][i]
		data.append(d/cnt)
		
	return data

# For initializing.
urg = pyurg.UrgDevice()

# Connect to the URG device.
# If could not conncet it, get False from urg.connect()
ret = urg.connect(port='/dev/tty.usbmodem1451')
if not ret:
    print('Could not connect.')
    exit()

# Get length datas and timestamp.
# If missed, get [] and -1 from urg.capture()
data = getData(urg)
# data = averageData(urg)

# Compute pie slices
N = len(data)

# print('-------------------')
# print(' {} '.format(N))
# print('-------------------')

lim = 120 * np.pi / 180.0
theta = np.linspace(-lim, lim, N, endpoint=False)
radii = data

ax = plt.subplot(111, projection='polar')
c = ax.scatter(theta, radii)

plt.show()