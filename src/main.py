# import required packages & functions
import numpy as np
import pandas as pd
import pickle
import ruptures as rpt
from classes import kernel_hyper, data_samples
from penalty_heuristics import slope_heur, cost_heur
from plot_cp import plot_cp

# =============================================================================
# Configuration 
# =============================================================================

dct_config = dict({# data intake settings
                   'load_sample_data': True, # True, False
                   'signal_id': 0, # 0,1,2,3,4,5,6,7,8,9,10
                   
                   # kernel configuration for cost function
                   'kernel': 'laplace',  # 'gaussian', 'linear', 'laplace'
                   'bandwidth': 'sig_std_batch_max', # 'median', 'sig_std', 
                                                     # 'sig_std_batch_max'
                   
                   # penalty heuristic configuration
                   'pen_heur': 'cost',  # 'cost', 'slope'
                   'alpha': 150,  # opt range cost_heur ~75-150 / slope_heur ~4-12
                   'n_cp_max': 10,  # maximum number of cps considered
                   'D_max': 10,  # max number of segments considered =<n_cp_max
                   'D_min': 6})  # min number of segments for slope heuristics

# potentially import your own data here:
ar_signal = np.array([])  # !!!<-- enter your signal as np.array here !!!
lst_cp_true = list() # !!! <-- enter your list of true CPs here !!!

# =============================================================================
# Import exemplary SCADA data if selected
# =============================================================================

if dct_config['load_sample_data'] == True:
    
    data = pickle.load( open( "data_samples.pkl", "rb" ) )
    
    df_signal = data.df_data[dct_config['signal_id']].dropna()
    df_info = data.df_info[dct_config['signal_id']]
    
    # Visualise selected signal
    sig_name = 'Signal '+str(dct_config['signal_id'])+': '+df_info.Signal
    
    title_fig = sig_name+' containing '+str(len(df_info.CP_true)-1)+' CPs'
    plot_cp(df_signal, df_info.CP_true, title=title_fig)

    ar_signal = df_signal.values  # pre-processed signal as np.array 
    lst_cp_true = df_info.CP_true  # list of ints representing the true CPs


# =============================================================================
# Find the first n_cp_max cps with ruptures-Dynp and kernel_hyper costum-cost
# =============================================================================

# define and fit costum cost object
custom_cost = kernel_hyper(dct_config['kernel'], 
                           dct_config['bandwidth']).fit(ar_signal) 

# define and fit search method 
cp_detector = rpt.Dynp(custom_cost = custom_cost, jump=1).fit(ar_signal)    

# prepare result file
df_dynp_cp = pd.DataFrame(index = [i for i in range(dct_config['n_cp_max']+1)], 
                          columns = ['kernel', 'bandwidth', 'n_cp',
                                     'lst_cp_det', 'cost'])

T = len(ar_signal)  # number of signal time-steps

# Loop through n_cp_max+1 options and calculate optimal cp-positions
for n_cp in range(dct_config['n_cp_max']+1):
    print('Calculating cp '+str(n_cp)+'/'+str(dct_config['n_cp_max'])+'...')
    
    if n_cp == 0:
        lst_cp_det = [T]  # last data-point in accordance with ruptures format   
    else:
        lst_cp_det = list(np.sort(cp_detector.predict(n_bkps=n_cp)))
    
    cost = custom_cost.sum_of_costs(lst_cp_det)  # calculating respective cost
    
    # store in result file
    df_dynp_cp.loc[n_cp] = [dct_config['kernel'], dct_config['bandwidth'], 
                            n_cp, lst_cp_det, cost] 

# array of cost for respective segmentations
ar_cost = np.array(df_dynp_cp.cost)

# =============================================================================
# Determin optimal number of CPs according to cost/slope heuristic
# =============================================================================
if dct_config['pen_heur'] =='cost':
    cp_opt = cost_heur(T, ar_cost, dct_config['alpha'], 
                       dct_config['n_cp_max'])[1]
    
elif dct_config['pen_heur'] == 'slope':
    cp_opt = slope_heur(T, ar_cost, dct_config['alpha'], 
                        dct_config['D_max'], dct_config['D_min'])[1]

# list of detected CPs
lst_cp_det = df_dynp_cp.loc[cp_opt, 'lst_cp_det']  

# =============================================================================
# Visualise solution
# =============================================================================
if dct_config['load_sample_data']==True:
    title_fig = str(df_info.Signal+' - number of CPs true/detected: '+
                 str(len(lst_cp_true)-1)+'  / '+ str(len(lst_cp_det)-1))  
else: 
    title_fig = str('Costum signal - number of CPs true/detected: '+
                 str(len(lst_cp_true)-1)+'  / '+ str(len(lst_cp_det)-1))

plot_cp(df_signal, lst_cp_true, lst_cp_det, title=title_fig)
print(dct_config)


'''
References and copyrigth:
    
<Kernel change-point detection for Wind SCADA data>
Copyright (C) <2020>  <Simon Letzgus>
Published under the GNU GENERAL PUBLIC LICENSE Version 3

contact: simon.letzgus@tu-berlin.de
'''
