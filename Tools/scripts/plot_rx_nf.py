#!/usr/bin/env python3
#
# Plots Receiver noise figure vs. gain setting
#

import sys
import numpy as np
import matplotlib.pyplot as plt


if len(sys.argv) < 3:
    print('Usage: plot_rx_nf.py mdsfile.dat yfile.dat [title]')
    sys.exit()

title = 'Receiver Noise Figure'
if len(sys.argv) > 3:
    title = sys.argv[3]

# MDS measurements
mdsfile = sys.argv[1]
#data = np.loadtxt(infile, usecols=range(0,7), dtype=float)
mdsdata = np.loadtxt(mdsfile, dtype=float)
ncolumns = mdsdata.shape[1]

# Y-factor measurements
yfile = sys.argv[2]
ydata = np.loadtxt(yfile, dtype=float)

plt.figure(num=1, figsize=(10, 6))
plt.title(title)
plt.xlabel('Gain setting')
plt.ylabel('Noise Figure (dB)')
plt.ylim(0, 60)

plt.plot(mdsdata[:,0], mdsdata[:,1], '-', label='145.5 MHz (MDS)')
plt.plot(ydata[:,0], ydata[:,1], '^', color='#1F77B4', label='145.5 MHz (Y-factor)')
plt.plot(mdsdata[:,0], mdsdata[:,2], '-', label='437.5 MHz (MDS)')
plt.plot(ydata[:,0], ydata[:,2], 's', color='#FF7F0E', label='437.5 MHz (Y-factor)')
plt.plot(mdsdata[:,0], mdsdata[:,3], '-', label='1280 MHz (MDS)')
plt.plot(ydata[:,0], ydata[:,3], 'o', color='#2CA02C', label='1280 MHz (Y-factor)')

if ncolumns > 4:
	plt.plot(mdsdata[:,0], mdsdata[:,4], '-', label='2250 MHz (MDS)')
	plt.plot(ydata[:,0], ydata[:,4], 'd', color='#D62728', label='2250 MHz (Y-factor)')
if ncolumns > 5:
    plt.plot(mdsdata[:,0], mdsdata[:,5], '-', label='2425 MHz (MDS)')
    plt.plot(ydata[:,0], ydata[:,5],'v', color='#9467BD', label='2425 MHz (Y-factor)')
if ncolumns > 6:
    plt.plot(mdsdata[:,0], mdsdata[:,6], '-', label='5830 MHz (MDS)')
    plt.plot(ydata[:,0], ydata[:,6], 'p', color='#8C564B', label='5830 MHz (Y-factor)')


plt.grid(linestyle='--', linewidth=0.5)
plt.legend()

svgfile = mdsfile + '.svg'
plt.savefig(svgfile)

plt.show()
