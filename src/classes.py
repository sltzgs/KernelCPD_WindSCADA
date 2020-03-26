#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:09:19 2020

@author: sltzgs
"""

import numpy as np
from ruptures.base import BaseCost
from sklearn.metrics.pairwise import linear_kernel,rbf_kernel,laplacian_kernel
from scipy.spatial.distance import pdist
  
class data_samples:
    '''
    Helper class for loading data samples. Contains samples of SCADA signals
    which are pre-processed as described in [1], section 4.1. The samples 
    contain all 11 different signals from 10 different turbines, which are 
    displayed in the figures of [1]. In addition to the pre-processing, the 
    time-stamps were altered for anonymisation.
    
    Parameters
    ----------
    df_data (pd.DataFrame): df with signals in columns. Column names serve as
                            ids to link signal information to df_info
    df_info (pd.DataFrame): Containing additional information for each signal, 
                            namely turbine alias, signal name, location of CP-
                            annotations and figure reference in [1].
    '''
    def __init__(self, df_data, df_info):

        self.df_data = df_data  
        self.df_info = df_info    

class kernel_hyper(BaseCost):

    '''
    Kernel cost function class. Can be used as a costum-cost function in the 
    ruptures-library [2]. Calculates the kernel cost for a signal using 
    Linear, Gaussian, or Laplacian kernel configuration with three optional
    bandwidth selection  heuristics as described in [1]. 
    
    Parameters
    ----------
    kernel (string): spec of kernel-type ('gaussian'/'linear'/'laplace')
    bandwidth (string): spec of bw-heuristic ('median'/'sig_std'/
                                              'sig_std_batch_max') 
    
    '''
    def __init__(self, kernel, bandwidth):
        
        self.kernel = kernel
        self.bandwidth = bandwidth
        
    model = ""  # required by ruptures library
    min_size = 2  # required by ruptures library

    def fit(self, signal, n_batch=20):
        '''
        Computes the gram matrix on the given signal

        Parameters
        ----------
        signal (np.array): pre-processed signal for cp-detection
        n_batch (int): number of batches for batch-bandwidth calculation
       
        Returns
        -------
        self including self.gram
        
        Note: Can be computationally expensive for large signals, since the 
        gram matrix is computed.
        
        '''
        
        signal -= np.mean(signal)
        
        if signal.ndim == 1:
            signal = signal.reshape(-1, 1)
        
        if (self.bandwidth == 'median'):
            
            if (self.kernel == 'laplace'):
                sigma = np.median(pdist(signal, metric='cityblock'))
            elif (self.kernel == 'gaussian'):
                sigma = np.median(pdist(signal, metric="sqeuclidean"))
            
        elif (self.bandwidth == 'sig_std'):
            sigma =  np.std(signal)
        
        elif (self.bandwidth == 'sig_std_batch_max'): 
            n = int(signal.shape[0]/n_batch)
            batch_signal = [signal[i:i+n] for i in range(0,signal.shape[0],n)]
            std_ = [np.std(i) for i in batch_signal]
            sigma = np.max(std_)
      
    
        if (self.kernel == 'linear'):
            gram = linear_kernel(signal)
        elif (self.kernel == 'laplace'):
            gram = laplacian_kernel(signal, gamma=(1/sigma))
        elif (self.kernel == 'gaussian'):
            gram = rbf_kernel(signal, gamma=(1/sigma))
                                                     
                                                    
        self.gram = gram

        return self
     
      
    def error(self, start, end):
        '''
        Return the approximation cost on the segment [start:end].

        Parameters
        ----------
        start (int): start of the segment
        end (int): end of the segment

        Returns:
        cost(float): segment cost
        
        '''
        
        sub_gram = self.gram[start:end, start:end]
        cost = np.diagonal(sub_gram).sum()
        cost -= sub_gram.sum() / (end - start)

        return cost
    
'''
References and copyright:
    
    [1] Letzgus, S.: Change-point detection in wind turbine SCADA data for 
        robust condition monitoring with normal behaviour models, submitted to: 
        Wind Energy Science, Special Issue: WESC 2019
        
    [2] https://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html
        Copyright (c) 2017, ENS Paris-Saclay, CNRS
        All rights reserved.

<Kernel change-point detection for Wind SCADA data>
Copyright (C) <2020>  <Simon Letzgus>
Published under the GNU GENERAL PUBLIC LICENSE Version 3

contact: simon.letzgus@tu-berlin.de
'''
