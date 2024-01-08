import pickle
from preprocessing import hashing
import pandas as pd

file = pd.read_csv('test_file.csv')

def run_prediction():
    # Load the model from the file
    with open('stacking_regressor_model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    # Read the input data
    ip = pd.read_csv('test_file.csv')
    
    # Perform necessary preprocessing
    ip = hashing(ip)
    
    # Make predictions
    y_p_00 = loaded_model.predict(ip)
    
    # Round the predictions to integers
    y_p_00_int = [round(y) for y in y_p_00]

    # Save predictions to output.csv
    predictions_df = pd.DataFrame({'Prediction': y_p_00_int})
    predictions_df.to_csv('output.csv', index=False)

run_prediction()
