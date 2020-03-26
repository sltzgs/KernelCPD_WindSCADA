# KernelCPD_WindSCADA

Python implementation and supplementary material complementing the WES-submission: "Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models" [1]. The repository contains code of all presented algorithms as well as samples of selected pre-processed SCADA signals. It complements comprehension of the paper and allows reproduction of results using on a set of available data samples or your own pre-processed SCADA data. 

If you would like to get in touch, please contact simon.letzgus@tu-berlin.de.

## Abstract

Analysis of data from wind turbine supervisory control and data acquisition (SCADA) systems has attracted considerable research interest in recent years. The data is predominantly used to gain insights into turbine condition without the need for additional sensing equipment. Most successful approaches apply semi-supervised anomaly detection methods, also called normal behaivour models, that use clean training data sets to establish healthy component baseline models. However, one of the major challenges when working with wind turbine SCADA data in practice is the presence of systematic changes in signal behaviour induced by malfunctions or maintenance actions. Even though this problem is well described in literature it has not been systematically addressed so far. This contribution is the first to comprehensively analyse the presence of change-points in wind turbine SCADA signals and introduce an algorithm for their automated detection. 600 signals from 33 turbines are analysed over an operational period of more than two years. During this time one third of the signals are affected by change points. Kernel change-point detection methods have shown promising results in similar settings but their performance strongly depends on the choice of several hyperparameters. This contribution presents a comprehensive comparison between different kernels as well as kernel-bandwidth and regularisation-penalty selection heuristics. Moreover, an appropriate data pre-processing procedure is introduced. The results show that the combination of Laplace kernels with a newly introduced bandwidth and penalty selection heuristic robustly outperforms existing methods. In a signal validation setting more than 90\% of the signals were classified correctly regarding the presence or absence of change-points, resulting in a F1-score of 0.86. For a change-point-free sequence selection the most severe 60\% of all CPs could be automatically removed with a precision of more than 0.96 and therefore without a significant loss of training data. These results indicate that the algorithm can be a meaningful step towards automated SCADA data pre-processing which is key for data driven methods to reach their full potential. The algorithm is open source and its implementation in Python publicly available.

## Getting Started

### Repo content
The repo is structured as follows:
- src: folder contains all code files
	- main.py:		 main file that allows to run the complete algorithm and adjustments of its hyperparameters.
	- classes.py:		 file contains a helper-class for the data sample import as well as the kernel cost function.
	- penalty_heuristics.py: file contains implementation of slope-heuristic as described in [2] and the cost-heuristic [1].
	- plot_cp:		 file contains function for visualising the cp-detection results.
- figures: folder contains exemplary plots for illustration
- requirements.txt: package requirements
- LICENSE: license information

### Installing

This code is written in ```Python 3.7``` and requires the packages listed in ```requirements.txt``` Clone the repository to your local machine and directory of choice:
```git clone https://github.com/sltzgs/KernelCPD_WindSCADA.git```

Get started by navigating to your target directory. In the main.py-file you can chose the signal to be analysed as well as the hyperparameters of the algorithm. Execute the main.py-file to run the algorithm with the respective settings.

### The main.py step-by-step

After importing the required library-packages, the Data-import section loads and unpickles the ```data_sample.pkl``` file. Via the variable ```id_signal``` one of the exemplary signals can be selected (see [data](#Data))

### Data (#Data)
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

## Result visualisation

If you want to embed images, this is how you do it:

![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/f1_1y_detail.png)



## Running change-point detection on your own data




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

