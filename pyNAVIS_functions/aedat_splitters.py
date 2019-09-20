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


from pyNAVIS_functions.utils import *
from bisect import bisect_left, bisect_right
from pyNAVIS_functions.aedat_functions import *
from pyNAVIS_functions.savers import save_AERDATA


def manual_aedat_splitter(allAddr, allTs, init, end, path, settings):

    #THIS IS NOT NEEDED IF TS ARE SORTED
    aedat_addr_ts = zip(allAddr, allTs)
    aedat_addr_ts = sorted(aedat_addr_ts, key=getKey)
    allAddr, allTs = extract_addr_and_ts(aedat_addr_ts)

    a =  bisect_left(allTs, init)
    b =  bisect_right(allTs, end)

    blockAddr = allAddr[a:b]
    blockTs = allTs[a:b]

    save_AERDATA(blockAddr, blockTs, path, settings)

"""
def automatic_aedat_splitter(allAddr, allTs, noiseTolerance, noiseThreshold, settings, path):
    #THIS IS NOT NEEDED IF TS ARE SORTED
    aedat_addr_ts = zip(allAddr, allTs)
    aedat_addr_ts = sorted(aedat_addr_ts, key=getKey)
    allAddr, allTs = extract_addr_and_ts(aedat_addr_ts)

    total_time = max(allTs) - min(allTs)
    last_time = min(allTs)
    its = int(math.ceil(total_time/settings.bin_size))
    numb_spikes_file = len(allAddr)

    hasEntered = 0
    times_entered = 0
    current_split = []
    splitted_aedat = []
    split_index = 0


    for i in range(its):

        a =  bisect_left(allTs, last_time)
        b =  bisect_right(allTs, last_time + settings.bin_size)
        blockAddr = allAddr[a:b]
        blockTs = allTs[a:b]

        #print len(blockAddr)
        #print noiseThreshold * numb_spikes_file
        if len(blockAddr) < noiseThreshold * numb_spikes_file:
            if hasEntered:
                hasEntered = 0
                current_split = []
                split_index += 1

                if times_entered < noiseTolerance:
                    splitted_aedat[split_index-1] = []
                times_entered = 0
        else:
            current_split.append([blockAddr, blockTs])
            splitted_aedat.append(current_split)
            hasEntered = 1
            times_entered += 1

        last_time += settings.bin_size

    cont  = 0
    for i in range(len(splitted_aedat)):
        if len(splitted_aedat[i]) > 1:
            cont += 1
            print len(splitted_aedat[i])
        #save_AERDATA(splitted_aedat[i][0], splitted_aedat[i][1], str(i) +".aedat", settings)
    print cont
"""

def stereoToMono(allAddr, allTs, left_right, path, settings): # NEEDS TO BE TESTED
    if settings.mono_stereo:
        aedat_addr_ts = zip(allAddr, allTs)
        aedat_addr_ts = [x for x in aedat_addr_ts if x[0] >= left_right*settings.num_channels*2 and x[0] < (left_right+1)*settings.num_channels*2]
        #print len(aedat_addr_ts)

        allAddr_mono, allTs_mono = extract_addr_and_ts(aedat_addr_ts)
        if left_right:
            allAddr_mono = [x-left_right*settings.num_channels*2 for x in allAddr_mono]
        save_AERDATA(allAddr_mono, allTs_mono, path, settings)
    else:
        print "StereoToMono: this functionality cannot be performed over a mono aedat file."

def monoToStereo(allAddr, allTs, delay, path, settings): # NEEDS TO BE TESTED
    if settings.mono_stereo == 0:
        allAddr = allAddr.extend(allAddr)
        newTs = allTs + delay
        allTs = allTs.extend(newTs)
        
        aedat_addr_ts = zip(allAddr, allTs)
        aedat_addr_ts = sorted(aedat_addr_ts, key=getKey)

        allAddr, allTs = extract_addr_and_ts(aedat_addr_ts)
        save_AERDATA(allAddr, allTs, path, settings)
    else:
        print "MonoToStereo: this functionality cannot be performed over a stereo aedat file."

    