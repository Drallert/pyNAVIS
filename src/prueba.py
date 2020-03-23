#################################################################################
##                                                                             ##
##    Copyright C 2018  Juan P. Dominguez-Morales                              ##
##                                                                             ##
##    This file is part of pyNAVIS.                                            ##
##                                                                             ##
##    pyNAVIS is free software: you can redistribute it and/or modify          ##
##    it under the terms of the GNU General Public License as published by     ##
##    the Free Software Foundation, either version 3 of the License, or        ##
##    (at your option) any later version.                                      ##
##                                                                             ##
##    pyNAVIS is distributed in the hope that it will be useful,               ##
##    but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the              ##
##    GNU General Public License for more details.                             ##
##                                                                             ##
##    You should have received a copy of the GNU General Public License        ##
##    along with pyNAVIS.  If not, see <http://www.gnu.org/licenses/>.         ##
##                                                                             ##
#################################################################################

## IMPORTS ##################################################################################################################
from classes.functions import Functions                                                                           #
from classes.generators import Generators                                                                         #
from classes.splitters import Splitters                                                                           #
from classes.dataset_gen import DatasetGenerators                                                                 #
from classes.loaders import SpikesFile, Loaders                                                                   #
from classes.plots import Plots                                                                                   #
from classes.utils import Utils                                                                                   #
from settings.main_settings import MainSettings                                                                     #
import matplotlib.pyplot as plt
#############################################################################################################################

## PARAMETERS ###############################################################################################################
num_channels = 32      # Number of NAS channels (not addresses but channels).                                               #
mono_stereo = 0        # 0 for a monaural NAS or 1 for a binaural NAS.                                                      #
address_size = 2       # 2 if .aedats are recorded with USBAERmini2 or 4 if .aedats are recorded with jAER.                 #
ts_tick = 0.2          # 0.2 if .aedats are recorded with USBAERmini2 or 1 if .aedats are recorded with jAER.               #
bin_size = 20000       # Time bin (in microseconds) used to integrate the spiking information.                              #
bar_line = 1           # 0 if you want the histogram to be a bar plot or 1 if you want the histogram to be a line plot.     #
spike_dot_freq = 1     # When plotting the cochleogram, it plots one spike for every spike_dot_frPeq spikes.                #
spike_dot_size = 1     # Size of the dots that are plotted on the spikegram                                                 #
#############################################################################################################################

path = 'C:\\Users\\juado\\Desktop'

# TEST GENERATORS
"""
#NOTE: Sweep
sweep_spikes = Generators.sweep(freq=5, cycles=5, num_ch=64, length=1000000, path='C:\\Users\\juado\\Desktop\\sweep', return_save_both=0)
sweep_settings = MainSettings(num_channels=64, mono_stereo=0, on_off_both=0, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
Plots.spikegram(sweep_spikes, sweep_settings)
Plots.sonogram(sweep_spikes, sweep_settings)
Plots.histogram(sweep_spikes, sweep_settings)
Plots.average_activity(sweep_spikes, sweep_settings)

#NOTE: Random addresses
random_spikes = Generators.random_addrs(freq=5400, num_ch=64, length=1000000, path='C:\\Users\\juado\\Desktop\\sweep', return_save_both=0)
random_settings = MainSettings(num_channels=64, mono_stereo=0, on_off_both=0, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
Plots.spikegram(random_spikes, random_settings)
Plots.sonogram(random_spikes, random_settings)
Plots.histogram(random_spikes, random_settings)
Plots.average_activity(random_spikes, sweep_settings)

#NOTE: Shift
shift_spikes = Generators.shift(freq=100, num_ch=64, length=1000000, path='C:\\Users\\juado\\Desktop\\shift', return_save_both=0)
shift_settings = MainSettings(num_channels=64, mono_stereo=0, on_off_both=0, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
Plots.spikegram(shift_spikes, shift_settings)
Plots.sonogram(shift_spikes, shift_settings)
Plots.histogram(shift_spikes, shift_settings)
Plots.average_activity(shift_spikes, shift_settings)
"""



#NOTE: Loading a stereo file
"""
settings = MainSettings(num_channels=16, mono_stereo=1, on_off_both=1, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
stereo_file = Loaders.loadAERDATA('D:\\Repositorios\\GitHub\\pyNAVIS\\src\\stereoPS.aedat', settings)
stereo_file = Functions.adapt_SpikesFile(stereo_file, settings)
#Functions.check_SpikesFile(stereo_file, settings)
Plots.spikegram(stereo_file, settings)
#Plots.sonogram(stereo_file, settings)
#Plots.histogram(stereo_file, settings)
#Plots.average_activity(stereo_file, settings)
#Plots.difference_between_LR(stereo_file, settings)
"""
"""
#NOTE: Manual split over a stereo file
manual_split_spikes = Splitters.manual_splitter(stereo_file, init=0, end=1000000, settings=settings, return_save_both=0 )
Plots.spikegram(manual_split_spikes, settings, graph_tile='Splitted SpikesFile', verbose=True)
Plots.sonogram(manual_split_spikes, settings, verbose=True)
"""
"""
#NOTE: Test Phaselock
stereo_file = Utils.order_timestamps(stereo_file)
phaseLocked_spikes = Functions.phase_lock(stereo_file, settings)
settings = MainSettings(num_channels=16, on_off_both=0, mono_stereo=1, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
Plots.spikegram(phaseLocked_spikes, settings, graph_tile='phaseLock', verbose=True)
"""


"""
#NOTE: Loading a mono file
settings = MainSettings(num_channels=32, mono_stereo=0, on_off_both=1, address_size=address_size, ts_tick=ts_tick, bin_size=bin_size, bar_line=bar_line, spikegram_dot_freq=spike_dot_freq, spikegram_dot_size=spike_dot_size)
mono_file = Loaders.loadAERDATA('D:\\Repositorios\\GitHub\\pyNAVIS\\src\\0a2b400e_nohash_0.wav.aedat', settings)
mono_file = Functions.adapt_SpikesFile(mono_file, settings)
Functions.check_SpikesFile(mono_file, settings)
Plots.spikegram(mono_file, settings)
Plots.sonogram(mono_file, settings)
Plots.histogram(mono_file, settings)
Plots.average_activity(mono_file, settings)
"""
"""
#NOTE: Manual split over a mono file
manual_split_spikes = Splitters.manual_splitter(mono_file, init=0, end=300000, settings=settings, return_save_both=0 )
Plots.spikegram(manual_split_spikes, settings, graph_tile='Splitted SpikesFile', verbose=True)
Plots.sonogram(manual_split_spikes, settings, verbose=True)
"""


plt.show()