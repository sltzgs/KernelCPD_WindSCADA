#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:49:13 2020

@author: sltzgs
"""

import math
import numpy as np
import scipy.special
from sklearn import linear_model

def slope_heur(T, C_d, alpha, D_max, D_min=None):
    
    '''
    Implementation of the slope heuristic as described in [1]
    
    Parameters
    ----------
    T (int): number of signal time-steps
    C_d (np.array): cost with respect to number of cps starting form D=0
    alpha (float): penalty factor alpha_slope
    D_max (int): upper limit of D for stlope-heur calculation
    D_min (int): recomended to be chosen as D_max*0.6


    Returns
    -------
    ar_cost_pen (np.array): penalised cost according to the slope heuristec
    D_slope_opt (int): opt number of segments according to the slope heuristic
    
    '''
    
    if D_min==None:
        D_min = math.floor(0.6*D_max)
    
    x1 = np.array(np.log([scipy.special.binom(T-1, D-1) 
                          for D in range(D_min, D_max)]))
    x2 = np.array([D/T for D in range(D_min, D_max)])
    y = C_d[D_min:D_max]
    
    lm = linear_model.LinearRegression()
    lm_s1 = lm.fit(x1.reshape(-1, 1), y.reshape(-1, 1))
    lm_s2 = lm.fit(x2.reshape(-1, 1), y.reshape(-1, 1))
    
    c1 = -alpha*lm_s1.coef_[0][0]
    c2 = -alpha*lm_s2.coef_[0][0]

    pen_ = [(1/T)*(c1*np.log(scipy.special.binom(T-1,D-1))+(c2*D)) 
            for D in range(1,D_max)]

    ar_cost_pen = C_d[:D_max-1] + np.array(pen_)
    D_slope_opt = np.argmin(ar_cost_pen)
    
    return ar_cost_pen, D_slope_opt


def cost_heur(T, C_d, alpha, D_max):
    '''
    Implementation of the cost heuristic as described in [2]
    
    Parameters
    ----------
    T (int): number of signal time-steps
    C_d (np.array): cost with respect to number of cps starting form D=0
    alpha (float): penalty factor alpha_cost
    D_max (int): maximum number of CPs considered

    Returns
    -------
    ar_cost_pen (np.array): penalised cost according to the cost heuristec
    D_slope_opt (int): opt number of segments according to the cost heuristic
    
    '''

    pen_ = [alpha*D*(C_d[0]**2)/(T**2) for D in range(D_max)]
    ar_cost_pen = C_d[:D_max] + np.array(pen_)
    D_slope_opt = np.argmin(ar_cost_pen)
    
    return ar_cost_pen, D_slope_opt

'''
References and copyright:
    
    [1] Arlot, S., Celisse, A., and Harchaoui, Z.: A kernel multiple change-
        point algorithm via model selection, 
        arXiv preprint arXiv:1202.3878,52016
        
    [2] Letzgus, S.: Change-point detection in wind turbine SCADA data for 
        robust condition monitoring with normal behaviour models, submitted to: 
        Wind Energy Science, Special Issue: WESC 2019

<Kernel change-point detection for Wind SCADA data>
Copyright (C) <2020>  <Simon Letzgus>
Published under the GNU GENERAL PUBLIC LICENSE Version 3

contact: simon.letzgus@tu-berlin.de
'''

