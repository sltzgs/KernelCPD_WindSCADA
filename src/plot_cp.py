#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:26:43 2020

@author: sltzgs
"""

import matplotlib.pyplot as plt
from itertools import cycle
from ruptures.utils import pairwise

def plot_cp(df_signal, lst_cp_true, lst_cp_det=None, title=False):
    '''
    Visualisation of signal and cps. True cps are represented by change in 
    background color, detected ones as dashed lines. Visualisation was created
    by altering ruptures.show [1]

    Parameters
    ----------
    df_signal (pd.DataFrame): signal in df form - index can be timestamp
    lst_cp_true (list): list of ints representing true cp-locations
    lst_cp_det (list): optional list of ints representing detected cp-locations
    title (string): optional figure title

    Returns
    -------
    none


    '''
    
    font = {'size'   : 12}
    plt.rc('font', **font)
    color_cycle = cycle(["silver", [.65,0,0]])
    alpha = 0.2

    fig, ax = plt.subplots(figsize=(10,2.25)) 
    
    if type(title)==str:
        ax.set_title(title)
    
    ax.plot(df_signal, c='k')
    ax.set_xlim(df_signal.index[0], df_signal.index[-1])
    

    bkps = [0]+lst_cp_true
    bkps[-1] = bkps[-1]-1
    index = df_signal.index
    
    for (start, end), col in zip(pairwise(bkps), color_cycle):
        ax.axvspan(index[start], index[end], facecolor=col, alpha=alpha)

    if type(lst_cp_det)==list:
        bkps = lst_cp_det[:-1]
        
        for bkp_det in bkps:
            ax.axvline(index[bkp_det], c='darkred', lw=3, ls='--')
    
        plt.legend(['signal (pre-processed)', 'CP detected'])

'''
References and copyright:
    
    [1] https://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html
        Copyright (c) 2017, ENS Paris-Saclay, CNRS
        All rights reserved.
        
<Kernel change-point detection for Wind SCADA data>
Copyright (C) <2020>  <Simon Letzgus>
Published under the GNU GENERAL PUBLIC LICENSE Version 3

contact: simon.letzgus@tu-berlin.de
'''