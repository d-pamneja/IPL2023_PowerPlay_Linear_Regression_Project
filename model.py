from preprocessing import X,y
import pickle

#Creating the final model
from sklearn.ensemble import StackingRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge

ab = AdaBoostRegressor(random_state = 1,loss = 'linear',n_estimators = 400, learning_rate = 0.04)
gb = GradientBoostingRegressor(random_state = 1,n_estimators = 400, max_depth = 3,loss = 'absolute_error',learning_rate = 0.04)
rfr = RandomForestRegressor(random_state = 1,n_estimators = 100,criterion = 'absolute_error')
byr = BayesianRidge()

sr_final = StackingRegressor([('gb',gb),('ab',ab),('rfr',rfr)],final_estimator = byr)
sr_final.fit(X,y)

with open('stacking_regressor_model.pkl', 'wb') as model_file:
    pickle.dump(sr_final, model_file)