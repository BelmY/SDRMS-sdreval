#!/usr/bin/env python3
#
# Plots RX BDR and max Pin vs. gain setting
#

import sys
import numpy as np
import matplotlib.pyplot as plt


def make_plot(title, infile):
	data = np.loadtxt(infile, dtype=float)
	ncolumns = data.shape[1]
	plt.title(title)
	plt.xlabel('Gain setting')
	plt.plot(data[:,0], data[:,1], label='Aluminum case')
	plt.plot(data[:,0], data[:,2], label='Board only')
	plt.grid(linestyle='--', linewidth=0.5)
	plt.legend()


plt.figure(num=1, figsize=(6, 9))

# 145 MHz
plt.subplot(311)
title = 'LimeSDR Mini Noise Figure at 145 MHz'
infile = 'NF_Lime-Mini_case_145.dat'
plt.ylabel('Noise Figure (dB)')
plt.ylim(0, 30)
make_plot(title, infile)

# 437 MHz
plt.subplot(312)
title = 'LimeSDR Mini Noise Figure at 437 MHz'
infile = 'NF_Lime-Mini_case_437.dat'
plt.ylabel('Noise Figure (dB)')
plt.ylim(0, 30)
make_plot(title, infile)

# 1280 MHz
plt.subplot(313)
title = 'LimeSDR Mini Noise Figure at 1280 MHz'
infile = 'NF_Lime-Mini_case_1280.dat'
plt.ylabel('Noise Figure (dB)')
plt.ylim(0, 40)
make_plot(title, infile)

svgfile = 'NF_Lime-Mini_case.svg'
plt.tight_layout()
plt.savefig(svgfile)#, bbox_inches='tight')

plt.show()



