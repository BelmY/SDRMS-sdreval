#!/usr/bin/env python3
#
# Plots CW TX power vs. gain setting
#

import sys
import numpy as np
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    print('Usage: plot_tx.power.py file.dat [title]')
    sys.exit()

title = 'CW Transmit Power'
if len(sys.argv) > 2:
    title = sys.argv[2]

infile = sys.argv[1]
#data = np.loadtxt(infile, usecols=range(0,7), dtype=float)
data = np.loadtxt(infile, dtype=float)
ncolumns = data.shape[1]

plt.figure(num=1, figsize=(10, 6))
plt.title(title)
plt.xlabel('Gain setting')
plt.ylabel('Power (dBm)')
plt.plot(data[:,0], data[:,1], label='145.5 MHz')
plt.plot(data[:,0], data[:,2], label='436.5 MHz')
plt.plot(data[:,0], data[:,3], label='1280 MHz')
plt.plot(data[:,0], data[:,4], label='2250 MHz')

if ncolumns > 5:
    plt.plot(data[:,0], data[:,5], label='2425 MHz')
if ncolumns > 6:
    plt.plot(data[:,0], data[:,6], label='5830 MHz')

plt.grid(linestyle='--', linewidth=0.5)
plt.legend()

svgfile = infile + '.svg'
plt.savefig(svgfile)

plt.show()
