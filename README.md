# KernelCPD_WindSCADA

Python implementation and supplementary material complementing the WES-submission: "Change-point detection in wind turbine SCADA data for robust condition monitoring with normal behaviour models". It contains code of all presented algorithms as well as samples of selected pre-processed SCADA signals.

## Abstract

Analysis of data from wind turbine supervisory control and data acquisition (SCADA) systems has attracted considerable research interest in recent years. The data is predominantly used to gain insights into turbine condition without the need for additional sensing equipment. Most successful approaches apply semi-supervised anomaly detection methods, also called normal behaivour models, that use clean training data sets to establish healthy component baseline models. However, one of the major challenges when working with wind turbine SCADA data in practice is the presence of systematic changes in signal behaviour induced by malfunctions or maintenance actions. Even though this problem is well described in literature it has not been systematically addressed so far. This contribution is the first to comprehensively analyse the presence of change-points in wind turbine SCADA signals and introduce an algorithm for their automated detection. 600 signals from 33 turbines are analysed over an operational period of more than two years. During this time one third of the signals are affected by change points. Kernel change-point detection methods have shown promising results in similar settings but their performance strongly depends on the choice of several hyperparameters. This contribution presents a comprehensive comparison between different kernels as well as kernel-bandwidth and regularisation-penalty selection heuristics. Moreover, an appropriate data pre-processing procedure is introduced. The results show that the combination of Laplace kernels with a newly introduced bandwidth and penalty selection heuristic robustly outperforms existing methods. In a signal validation setting more than 90\% of the signals were classified correctly regarding the presence or absence of change-points, resulting in a F1-score of 0.86. For a change-point-free sequence selection the most severe 60\% of all CPs could be automatically removed with a precision of more than 0.96 and therefore without a significant loss of training data. These results indicate that the algorithm can be a meaningful step towards automated SCADA data pre-processing which is key for data driven methods to reach their full potential. The algorithm is open source and its implementation in Python publicly available.

## Getting Started

## Description


### Installing

This code is written in '''Python 3.7''' and requires the packages listed in '''requirements.txt'''. Clone the repository to your local machine and directory of choice:
'''git clone https://github.com/sltzgs/KernelCPD_WindSCADA.git'''

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running change-point detection

Explain how to run the automated tests for this system



## Examples

If you want to embed images, this is how you do it:

![Exemplary_image](https://github.com/sltzgs/KernelCPD_WindSCADA/blob/master/figures/f1_1y_detail.png)

## Data
The '''data_samples.pkl'' in the src-folder contains a selection of 11 pre-processed SCADA signals. They represent all examplary cases used in the publication for visualising the algorithm's performance. The '''.pkl'''-file contains a '''data_samples'''-object which holds the SCADA signals and additional information to each siganl, both as '''pd.DataFrames'''. The information-DataFrame

| Signal ID | Turbine ID | Signal name | CP present | Figure |
| --- | --- | --- | --- |--- |
| 0 | A | Nacelle Temperature | yes (2) | 8 |
| 1 | B | Gear Bearing Temperature | no | 9 |
| 2 | C | Hydraulic Oil Temperature | yes (1) | 3,5 |
| 3 | D | Generator Bearing Temperature | yes (2) | 9 |
| 4 | E | Gear Oil Pressure | yes (3) | 4 |
| 5 | F | Gear Oil Pressure | yes (2) | 3,5 |
| 6 | G | Gear Bearing Temperature | yes (1) | 3,5 |
| 7 | H | Gear Oil Temperature | yes (2) | 11 |
| 8 | I | Pitch Motor Temperature | yes (6) | 11 |
| 9 | I |Gear Oil Pressure | yes (1) | 8 |
| 10 | J | Gear Bearing Temperature | yes (1) | 11 |

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

