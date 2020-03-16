#!/usr/bin/env python3
#
# Plots CW TX power vs. gain setting
#

import sys
import numpy as np
import matplotlib.pyplot as plt


def make_plot(title, infile):
	data = np.loadtxt(infile, dtype=float)
	ncolumns = data.shape[1]
	plt.title(title)
	plt.xlabel('Gain setting')
	plt.plot(data[:,0], data[:,1], label='145.5 MHz')
	plt.plot(data[:,0], data[:,2], label='436.5 MHz')
	plt.plot(data[:,0], data[:,3], label='1280 MHz')
	if ncolumns > 4:
		plt.plot(data[:,0], data[:,4], label='2250 MHz')
	if ncolumns > 5:
		plt.plot(data[:,0], data[:,5], label='2425 MHz')
	if ncolumns > 6:
		plt.plot(data[:,0], data[:,6], label='5830 MHz')
	plt.grid(linestyle='--', linewidth=0.5)
	plt.legend()


if len(sys.argv) < 2:
    print('Usage: plot_rx_bdr.py <SDR>')
    sys.exit()


sdr = sys.argv[1]
plt.figure(num=1, figsize=(13, 14))

# Pin at 5 kHz
plt.subplot(321)
title = sdr + ' $P_{in}$ max at 5 kHz separation'
infile = sdr + '_Pin_5k.dat'
plt.ylabel('$P_{in}$ max (dBm)')
plt.ylim(-80, 0)
make_plot(title, infile)

# BDR at 5 kHz
plt.subplot(322)
title = sdr + ' Blocking dynamic range at 5 kHz separation'
infile = sdr + '_BDR_5k.dat'
plt.ylabel('BDR (dB)')
plt.ylim(0, 120)
make_plot(title, infile)

# Pin at 100 kHz
plt.subplot(323)
title = sdr + ' $P_{in}$ max at 100 kHz separation'
infile = sdr + '_Pin_100k.dat'
plt.ylabel('$P_{in}$ max (dBm)')
plt.ylim(-80, 0)
make_plot(title, infile)

# BDR at 100 kHz
plt.subplot(324)
title = sdr + ' Blocking dynamic range at 100 kHz separation'
infile = sdr + '_BDR_100k.dat'
plt.ylabel('BDR (dB)')
plt.ylim(0, 120)
make_plot(title, infile)

# Pin at 1 MHz
plt.subplot(325)
title = sdr + ' $P_{in}$ max at 1 MHz separation'
infile = sdr + '_Pin_1M.dat'
plt.ylabel('$P_{in}$ max (dBm)')
plt.ylim(-80, 0)
make_plot(title, infile)

# BDR at 1 MHz
plt.subplot(326)
title = sdr + ' Blocking dynamic range at 1 MHz separation'
infile = sdr + '_BDR_1M.dat'
plt.ylabel('BDR (dB)')
plt.ylim(0, 120)
make_plot(title, infile)


svgfile = sdr + '.svg'
plt.tight_layout()
plt.savefig(svgfile)#, bbox_inches='tight')

plt.show()



