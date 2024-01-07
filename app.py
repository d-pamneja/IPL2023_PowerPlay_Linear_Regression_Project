import streamlit as st  
import pandas as pd
from prediction import run_prediction

st.set_page_config(page_title="IPL_Regression", page_icon=":chart_increasing:", layout="wide")

## HEADER 
st.title('IPL Score Prediction')
st.subheader('Predicting the score of the powerplay in both innings of an IPL match')
st.write('The aim of this project is to predict the runs that will be scored in the powerplay of each innings, given the infomration of the venue, batting an bowling team for that innings, and the players which participated in the given overs.')

import os

def write_to_csv(data, filename='test_file.csv'):
    if os.path.exists(filename):
        # File exists, append data
        df = pd.DataFrame([data], columns=['venue', 'innings', 'batting_team', 'bowling_team', 'batsmen', 'bowlers'])
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        # File doesn't exist, create a new file with headers
        df = pd.DataFrame([data], columns=['venue', 'innings', 'batting_team', 'bowling_team', 'batsmen', 'bowlers'])
        df.to_csv(filename, mode='w', header=True, index=False)



st.subheader('Innings 1:')  
venue = st.text_input('Venue', key='venue_1')
innings_1 = st.number_input('Innings', key='innings_1', value=1)
batting_team_1 = st.text_input('Batting Team', key='batting_team_1')
bowling_team_1 = st.text_input('Bowling Team', key='bowling_team_1')
batsmen_1 = st.text_input('Batsmen', key='batsmen_1')
bowlers_1 = st.text_input('Bowlers', key='bowlers_1')

st.subheader('Innings 2:')  
venue = st.text_input('Venue', key='venue_2',value=venue)
innings_2 = st.number_input('Innings', key='innings_2', value=2)
batting_team_2 = st.text_input('Batting Team', key='batting_team_2',value=bowling_team_1)
bowling_team_2 = st.text_input('Bowling Team', key='bowling_team_2',value=batting_team_1)
batsmen_2 = st.text_input('Batsmen', key='batsmen_2')
bowlers_2 = st.text_input('Bowlers', key='bowlers_2')

if st.button('Run Prediction'):
    data_1 = {'venue': venue, 'innings': innings_1, 'batting_team': batting_team_1, 'bowling_team': bowling_team_1, 'batsmen': batsmen_1, 'bowlers': bowlers_1}
    data_2 = {'venue': venue, 'innings': innings_2, 'batting_team': batting_team_2, 'bowling_team': bowling_team_2, 'batsmen': batsmen_2, 'bowlers': bowlers_2}
    write_to_csv(data_1)
    write_to_csv(data_2)
    
    file=pd.read_csv('test_file.csv')

    prediction_result = run_prediction(file)
    
    if prediction_result:
        score_1, score_2 = prediction_result
        st.success(f'Prediction Result: {score_1} - {score_2}')