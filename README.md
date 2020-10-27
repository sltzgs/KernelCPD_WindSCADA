# KernelCPD_WindSCADA

Python implementation and supplementary material complementing the WES-submission: "Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models" [1]. The repository contains code of all presented algorithms as well as samples of selected 
essed SCADA signals. It complements comprehension of the paper and allows reproduction of results using on a set of available data samples or your own pre-processed SCADA data. 

If you would like to get in touch, please contact simon.letzgus@tu-berlin.de.

[![DOI](https://zenodo.org/badge/248196713.svg)](https://zenodo.org/badge/latestdoi/248196713)


## Repo content
The repo is structured as follows:
- src: folder contains all code files
	- main.py:		 main file that allows to run the complete algorithm and adjustments of its hyperparameters.
	- classes.py:		 file contains a helper-class for the data sample import as well as the kernel cost function, which represents an instance of the custom cost class within the ruptures-framework [2].
	- penalty_heuristics.py: file contains implementation of slope-heuristic as described in [3] and the cost-heuristic [1].
	- plot_cp:		 file contains function for visualising the cp-detection results.
- figures: folder contains exemplary plots for illustration
- requirements: txt-file listing package requirements
- LICENSE: license information

## Installing

This code is written in ```Python 3.7``` and requires the packages listed in ```requirements.txt```.  Clone the repository to your local machine and directory of choice:
```git clone https://github.com/sltzgs/KernelCPD_WindSCADA.git```

Get started by navigating to your target directory. In the main.py-file you can chose the signal to be analysed as well as the hyperparameters of the algorithm. Execute the main.py-file to run the algorithm with the respective settings.

## How to run the algorithm?
The main.py file is used to execute the algorithm and adjust its hyperparameters. All adjustable hyperparameter can be found in the ```dct_conf``` dictionary. For further explanations of the algorithm refer to [1]. The following options are given:

### Data intake settings:
```load_sample_data_```: Select 'True' if you want to use one of the sample signals provided. Select 'False' if you want to load costum data and enter your own data in the lines 31 and 32 of the file as described below.

```singal_id```: Select an ID for one of the sample signals (compare Data)

### Kernel configuration for cost function 
```kernel```: specify the kernel as 'linear', 'gaussian' or 'laplace'

```bandwidth```: specify bandwith heuristic for the respective kernel as 'median', 'sig_std' ,or 'sig_std_batch_max'

### Penalty heuristic configuration
```pen-heur```: 'cost' for cost-heuristic introduced and described in section 4.2 of [1], or 'slope' for slope heuristic described in [3]

```alpha```: regularising penalty-factor. For adequate choice refer to [1]

```n_cp_max```: maximum number of change-points considered

```D_min/D_max```: hyperparameter for slope-heuristic (compare [3])

### Running the algorithm on your own data
In case you want to run the algorithm on your own SCADA data, firstly follow the pre-processing procedure described described in detail [1], section 4.1. Then, insert your signal as a np.array() in line 31 of ```main.py``` into the ```ar_signal``` variable and the corresponding list with integers indicating true change-points into the ```lst_cp_true``` variable (line 32). Chose the desired hyperparameters as described above and run the script.

## Script output
When you run the script, the initially selected signal is displayed as shown in the following pictures:

![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_signal_0.png)
![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_signal_6.png)

Moreover, the results of the change-point detection algorithm under the respective configuration will be displayed:
![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_cpd_result_signal_0.png)
![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/plot_cpd_result_signal_6.png)


The location of the detected change-points will be stored in the list ```lst_cp_det```.

## Data
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




## Paper abstract
Analysis of data from wind turbine supervisory control and data acquisition (SCADA) systems has attracted considerable research interest in recent years. Its predominant application is to monitor turbine condition without the need for additional sensing equipment. Most approaches apply semi-supervised anomaly detection methods, also called normal behaviour models, that require clean training data sets to establish healthy component baseline models. In practice, however, the presence of change points induced by malfunctions or maintenance actions poses a major challenge. Even though this problem is well described in literature, this contribution is the first to systematically evaluate and address the issue. A total of 600 signals from 33 turbines are analysed over an operational period of more than 2 years. During this time one-third of the signals were affected by change points, which highlights the necessity of an automated detection method. Kernel-based change-point detection methods have shown promising results in similar settings. We, therefore, introduce an appropriate SCADA data preprocessing procedure to ensure their feasibility and conduct comprehensive comparisons across several hyperparameter choices. The results show that the combination of Laplace kernels with a newly introduced bandwidth and regularisation-penalty selection heuristic robustly outperforms existing methods. More than 90 % of the signals were classified correctly regarding the presence or absence of change points, resulting in an F1 score of 0.86. For an automated change-point-free sequence selection, the most severe 60 % of all change points (CPs) could be automatically removed with a precision of more than 0.96 and therefore without any significant loss of training data. These results indicate that the algorithm can be a meaningful step towards automated SCADA data preprocessing, which is key for data-driven methods to reach their full potential. The algorithm is open source and its implementation in Python is publicly available.

# References

[1] Letzgus, S.: Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models, submitted to: Wind Energy Science, Special Issue: WESC 2019
        
[2] https://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html, Copyright (c) 2017, ENS Paris-Saclay, CNRS, All rights reserved.

[3] Arlot, S., Celisse, A., and Harchaoui, Z.: A kernel multiple change-point algorithm via model selection, arXiv preprint arXiv:1202.3878,52016
# License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details


