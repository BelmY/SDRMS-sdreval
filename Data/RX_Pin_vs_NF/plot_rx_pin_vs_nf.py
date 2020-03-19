#!/usr/bin/env python3
#
# Plots max RX input power vs NF for all devices
#

import sys
import numpy as np
import matplotlib.pyplot as plt



def plot_data(filename, column, plot_label):
	data = np.loadtxt(filename, dtype=float)
	plt.plot(data[:,1], data[:,column], label=plot_label)


# 5 kHz separation
title = 'Max RX input power at 437 MHz, 5 kHz separation'
plt.figure(num=1, figsize=(10, 6))
plt.title(title)
plt.xlabel('Noise figure (dB)')
plt.ylabel('Max input power (dBm)')
plot_data('RTL-SDR.dat', 2, 'RTL-SDR V3')
plot_data('Airspy-Mini.dat', 2, 'Airspy Mini')
plot_data('SDRplay.dat', 2, 'SDRplay RSPduo')
plot_data('LimeSDR-Mini.dat', 2, 'LimeSDR Mini')
plot_data('BladeRF.dat', 2, 'BladeRF 2.0 micro')
plot_data('USRP-B210.dat', 2, 'USRP B210')
plot_data('PlutoSDR.dat', 2, 'PlutoSDR')
plt.ylim(-100, 10)
plt.grid(linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('RX_Pin_vs_NF-5k.svg')
plt.show()

# 100 kHz separation
title = 'Max RX input power at 437 MHz, 100 kHz separation'
plt.figure(num=2, figsize=(10, 6))
plt.title(title)
plt.xlabel('Noise figure (dB)')
plt.ylabel('Max input power (dBm)')
plot_data('RTL-SDR.dat', 3, 'RTL-SDR V3')
plot_data('Airspy-Mini.dat', 3, 'Airspy Mini')
plot_data('SDRplay.dat', 3, 'SDRplay RSPduo')
plot_data('LimeSDR-Mini.dat', 3, 'LimeSDR Mini')
plot_data('BladeRF.dat', 3, 'BladeRF 2.0 micro')
plot_data('USRP-B210.dat', 3, 'USRP B210')
plot_data('PlutoSDR.dat', 3, 'PlutoSDR')
plt.ylim(-100, 10)
plt.grid(linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('RX_Pin_vs_NF-100k.svg')
plt.show()

# 1 MHz separation
title = 'Max RX input power at 437 MHz, 1 MHz separation'
plt.figure(num=2, figsize=(10, 6))
plt.title(title)
plt.xlabel('Noise figure (dB)')
plt.ylabel('Max input power (dBm)')
plot_data('RTL-SDR.dat', 4, 'RTL-SDR V3')
plot_data('Airspy-Mini.dat', 4, 'Airspy Mini')
plot_data('SDRplay.dat', 4, 'SDRplay RSPduo')
plot_data('LimeSDR-Mini.dat', 4, 'LimeSDR Mini')
plot_data('BladeRF.dat', 4, 'BladeRF 2.0 micro')
plot_data('USRP-B210.dat', 4, 'USRP B210')
plot_data('PlutoSDR.dat', 4, 'PlutoSDR')
plt.ylim(-100, 10)
plt.grid(linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('RX_Pin_vs_NF-1M.svg')
plt.show()
