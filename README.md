# KernelCPD_WindSCADA

Python implementation and supplementary material complementing the WES-submission: "Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models" [1]. The repository contains code of all presented algorithms as well as samples of selected 
essed SCADA signals. It complements comprehension of the paper and allows reproduction of results using on a set of available data samples or your own pre-processed SCADA data. 

If you would like to get in touch, please contact simon.letzgus@tu-berlin.de.

## Abstract

Analysis of data from wind turbine supervisory control and data acquisition (SCADA) systems has attracted considerable research interest in recent years. The data is predominantly used to gain insights into turbine condition without the need for additional sensing equipment. Most successful approaches apply semi-supervised anomaly detection methods, also called normal behaivour models, that use clean training data sets to establish healthy component baseline models. However, one of the major challenges when working with wind turbine SCADA data in practice is the presence of systematic changes in signal behaviour induced by malfunctions or maintenance actions. Even though this problem is well described in literature it has not been systematically addressed so far. This contribution is the first to comprehensively analyse the presence of change-points in wind turbine SCADA signals and introduce an algorithm for their automated detection. 600 signals from 33 turbines are analysed over an operational period of more than two years. During this time one third of the signals are affected by change points. Kernel change-point detection methods have shown promising results in similar settings but their performance strongly depends on the choice of several hyperparameters. This contribution presents a comprehensive comparison between different kernels as well as kernel-bandwidth and regularisation-penalty selection heuristics. Moreover, an appropriate data pre-processing procedure is introduced. The results show that the combination of Laplace kernels with a newly introduced bandwidth and penalty selection heuristic robustly outperforms existing methods. In a signal validation setting more than 90\% of the signals were classified correctly regarding the presence or absence of change-points, resulting in a F1-score of 0.86. For a change-point-free sequence selection the most severe 60\% of all CPs could be automatically removed with a precision of more than 0.96 and therefore without a significant loss of training data. These results indicate that the algorithm can be a meaningful step towards automated SCADA data pre-processing which is key for data driven methods to reach their full potential. The algorithm is open source and its implementation in Python publicly available.


## Repo content
The repo is structured as follows:
- src: folder contains all code files
	- main.py:		 main file that allows to run the complete algorithm and adjustments of its hyperparameters.
	- classes.py:		 file contains a helper-class for the data sample import as well as the kernel cost function, which represents an instance of the custom cost class within the ruptures-framework [2].
	- penalty_heuristics.py: file contains implementation of slope-heuristic as described in [3] and the cost-heuristic [1].
	- plot_cp:		 file contains function for visualising the cp-detection results.
- figures: folder contains exemplary plots for illustration
- requirements.txt: package requirements
- LICENSE: license information

## Installing

This code is written in ```Python 3.7``` and requires the packages listed in ```requirements.txt```.  Clone the repository to your local machine and directory of choice:
```git clone https://github.com/sltzgs/KernelCPD_WindSCADA.git```

Get started by navigating to your target directory. In the main.py-file you can chose the signal to be analysed as well as the hyperparameters of the algorithm. Execute the main.py-file to run the algorithm with the respective settings.

## The main.py step-by-step
The main.py file is used to execute the algorithm and adjust its hyperparameters. As a naming convention all variables considered an adjustable hyperparameter end with an underscore (_).

### Data import
In the ```Data-import``` section either the sample data or costum data can be loaded. If ```load_sample_data_ = True``` the ```data_sample.pkl``` file is loaded and unpickled. Via the variable ```id_signal_``` one of the exemplary signals can be selected (compare [Data](###Data)). The selected signal is automatically plotted as shown in XXX. If you want to load costum data, set ```load_sample_data_ = False``` and enter your own data in the lines 19 and 20 of the file as described in the [Running the algorithm on your own data](##Running-the-algorithm-on-you-own-data). 

### Kernel configuration
In this section the kernel type as well as the heuristic for the bandwidth selection have to be specified. The former is chosen via the variables ```kernel_```, which can assume the values 'linear', 'gaussian', or 'laplace'. The latter via the ```bandwidth_``` variable which can be set as 'medium', 'sig_std' or 'sig_std_batch_max'. Depending on the respective options an instance of the ruptures-package [custom cost class](#http://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/costs/costcustom.html) is created.

### Penalty heuristic configuration
In this section the heuristic for penalty selection can be configured. Firstly, it can be chosen between the cost-heuristic introduced and described in section 4.2 of [1], or the slope heuristic described in [3]. This is done via the ```sel_heur_``` variable, which can assume the values 'cost' or 'slope' respectively. Moreover, the penalty factor '''alpha_``` has to be selected. It serves as a regularisation parameter. Therefore, high values of ```alpha_``` will lead to a lower number of change-points to be detected. Recommendations on the choice of ```alpha_``` can be found in [1]. Lastly, when using the slope-heuristics the parameters ```D_max_``` and ```D_min_``` have to be chosen (refer to [3] for further advice on how to chose them).

### Data
The ```data_samples.pkl``` in the src-folder contains a selection of 11 pre-processed SCADA signals. The pre-processing procedure is described in detail [1], section 4.1. The signals represent all examplary cases used in [1] for visualising the algorithm's performance. The ```.pkl```file contains a ```data_samples```-object which holds the SCADA signals and additional information for each siganl, both as ```pd.DataFrames```. Namely, the following signals are included:

| Signal ID | Turbine ID | Signal name | CP present | Figure |
| --- | --- | --- | --- |--- |
| 0 | A | Nacelle Temperature | yes (2) | 8 |
| 1 | B | Gear Bearing Temperature | no | 9 |
| 2 | C | Hydraulic Oil Temperature | yes (1) | 3, 5 |
| 3 | D | Generator Bearing Temperature | yes (2) | 9 |
| 4 | E | Gear Oil Pressure | yes (3) | 4 |
| 5 | F | Gear Oil Pressure | yes (2) | 3, 5 |
| 6 | G | Gear Bearing Temperature | yes (1) | 3, 5 |
| 7 | H | Gear Oil Temperature | yes (2) | 11 |
| 8 | I | Pitch Motor Temperature | yes (6) | 11 |
| 9 | I |Gear Oil Pressure | yes (1) | 8 |
| 10 | J | Gear Bearing Temperature | yes (1) | 11 |

## Run the script
When you run the script, the initially selected signal is displayed as shown in the following pictures:

![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_signal_0.png)
![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_signal_6.png)

Moreover, the results of the change-point detection algorithm under the respective configuration will be displayed:

The location of the detected change-points will be stored in the list ```lst_cp_det```.

## Running the algorithm on your own data
In case you want to run the algorithm on your own SCADA data, firstly follow the pre-processing procedure described described in detail [1], section 4.1. Then, insert your signal as a np.array() in line 30 of ```main.py``` into the ```ar_signal``` variable and the corresponding list with integers indicating true change-points into the ```lst_cp_true``` variable (line 31). Chose the desired hyperparameters as described above and run the script.


# References

[1] Letzgus, S.: Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models, submitted to: Wind Energy Science, Special Issue: WESC 2019
        
[2] https://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html
        Copyright (c) 2017, ENS Paris-Saclay, CNRS
        All rights reserved.


# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

