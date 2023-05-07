# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:10:50 2017

@author: CarlSouthall
"""



from . import utils
import os

"""
Parameters
----------
data : numpy array, str or file handle
    Signal data or file name or file handle.
sample_rate : int, optional
    Desired sample rate of the signal [Hz], or 'None' to return the
    signal in its original rate.
num_channels : int, optional
    Reduce or expand the signal to `num_channels` channels, or 'None'
    to return the signal with its original channels.
"""
def ADT(data, sample_rate=None, num_channels=1, text='no', tab='no', save_dir=None, output_act='no'):
    location=utils.location_extract()

    if output_act=='yes':
        acts=[]

    spec, sr = utils.spec(data, sample_rate, num_channels)
    AFs=utils.system_restore(spec,location)
    PP=utils.load_pp_param(location)    
    Peaks=[]
    for j in range(len(AFs)):
        Peaks.append(utils.meanPPmm(AFs[j][:,0], PP[j,0], PP[j,1], PP[j,2], sr))
    sorted_p=utils.sort_ascending(Peaks)
    if text=='yes':
        utils.print_to_file(sorted_p,data,save_dir)

    if tab=='yes':
        utils.tab_create([Peaks[2],Peaks[1],Peaks[0]],data,save_dir)

    Onsets = {'Kick':Peaks[0], 'Snare':Peaks[1], 'Hihat':Peaks[2]}

    if output_act=='yes':
        acts.append(AFs)
    if output_act=='yes':        
        return Onsets,acts
    else:
        return Onsets
            
        
    
