# IPL 2023 Powerplay Prediction - Linear Regression ML Project
## Using linear regression alogrithms in machine learning to predict the powerplay runs scored in each inning of a given match

### Decription of Problem Statement
The aim of this project is to predict the runs that will be scored in the powerplay of each innings, given the infomration of the venue, batting an bowling team for that innings, and the players which participated in the given overs.

#### Data Description
1. **Training data**: You will be provided two files for training data, they are as following:
    * **IPL_Ball_by_Ball_2008_2022.csv**: This file contains a ball by ball record of each IPL match since 2008 to 2022. The column names are self explanatory. 
    * **IPL_Matches_Result_2008_2022.csv**: This file contains results of each IPL match since 2008 to 2022. The column names are self explanatory. 

The data can be found in the link given [here](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset).

### Evaluation Metric
Here, the data has been evaluated using mean absolute error.

## Models Evaluated
Here,in this project I have evaluated the performance of the following models:

* Ridge 
* Lasso 
* Linear Regression
* SGD Regressor
* Bayesion Ridge
* Kernel Ridge
* HistGradientBoostingRegressor
* MLPRegressor
* ExtraTreesRegressor
* BaggingRegressor
* RandomForestRegressor
* AdaBoostRegressor
* GradientBoostingRegressor
* XGBRegressor
* LGBMRegressor

Apart from that, I have also tried ensemble models, such as:

* VotingRegressor
* StackingRegressor

## Model Used 
Hence, we will use **Stacking Regresor** to make predictions. 

1. We can also use the voting regressor as well. However, since 
stacking has a lower MAE in train data set and the error on test dataset is marginally high than voting regressor, we will go for that.

2. Kindly note that either of the two models i.e. Voting and Stacking Regressor could be the ideal model as per my analysis.

## Final Test Error
The final test error (MAE) is : **8.579578436102235**.

## Collab Link
The collab link for the file can be found [here](https://colab.research.google.com/drive/18s4W3x5FH24CYBoL92zNAF551EUfI-tM?usp=sharing).