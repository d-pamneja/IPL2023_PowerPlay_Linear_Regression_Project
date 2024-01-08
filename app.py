import streamlit as st  
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IPL_Regression", page_icon=":chart_increasing:", layout="wide")

## HEADER 
st.title('IPL Score Prediction')
st.header('Predicting the score of the powerplay in both innings of an IPL match')
st.write('The aim of this project is to predict the runs that will be scored in the powerplay of each innings, given the infomration of the venue, batting an bowling team for that innings, and the players which participated in the given overs.')

import os

        

def write_to_csv(data, filename='test_file.csv'):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        existing_data = pd.read_csv(filename)
    else:
        existing_data = pd.DataFrame()

    new_data = pd.DataFrame([data], columns=['venue', 'innings', 'batting_team', 'bowling_team', 'batsmen', 'bowlers'])
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)

    combined_data.to_csv(filename, mode='w', header=True, index=False)



def get_prediction():
    try:
        subprocess.run(['python', 'prediction.py'], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Error running prediction.py: {e}")
        st.stop()

def display_predictions():
    predictions_df = pd.read_csv('output.csv')
    
    predictions_df['innings'] = [1, 2]

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='innings', y='Prediction', data=predictions_df, ax=ax)
    
    for index, row in predictions_df.iterrows():
        ax.text(row['innings'] - 1, row['Prediction'] + 0.5, str(row['Prediction']), color='black', ha='center', va='bottom')

    ax.set_title('Predicted Scores for Both Innings')
    ax.set_ylabel('Score')
    st.pyplot(fig)
    
def validate_inputs(data_1, data_2):
    error_placeholder = st.empty()

    if not all(data_1.values()):
        error_placeholder.error("Please fill in all input values for Innings 1.")
        return False

    if not all(data_2.values()):
        error_placeholder.error("Please fill in all input values for Innings 2.")
        return False

    return True

def clear_files():
    open('test_file.csv', 'w').close()
    open('output.csv', 'w').close()

team_list = ['Kolkata Knight Riders', 'Royal Challengers Bangalore',
       'Chennai Super Kings', 'Punjab Kings', 'Rajasthan Royals',
       'Delhi Capitals', 'Mumbai Indians', 'Sunrisers Hyderabad',
       'Gujarat Titans', 'Lucknow Super Giants']

stadium_list = ['Arun Jaitley Stadium', 'Wankhede Stadium',
       'M.Chinnaswamy Stadium', 'Rajiv Gandhi International Stadium',
       'Maharashtra Cricket Association Stadium',
       'Sawai Mansingh Stadium', 'Eden Gardens', 'Holkar Cricket Stadium',
       'MA Chidambaram Stadium', 'Punjab Cricket Association Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Zayed Cricket Stadium', 'Dubai International Cricket Stadium',
       'Sharjah Cricket Stadium', 'Narendra Modi Stadium',
       'Brabourne Stadium', 'Dr DY Patil Sports Academy']

st.subheader('Innings 1:')  
venue = st.selectbox('Venue', stadium_list,key='venue_1')
innings_1 = st.number_input('Innings', key='innings_1', value=1)
batting_team_1 = st.selectbox('Batting Team',team_list, key='batting_team_1')
bowling_team_1 = st.selectbox('Bowling Team',team_list, key='bowling_team_1')
batsmen_1 = st.text_input('Batsmen', key='batsmen_1')
bowlers_1 = st.text_input('Bowlers', key='bowlers_1')

st.subheader('Innings 2:')  
venue = st.selectbox('Venue', stadium_list,key='venue_2')
innings_2 = st.number_input('Innings', key='innings_2', value=2)
batting_team_2 = st.selectbox('Batting Team',team_list, key='batting_team_2')
bowling_team_2 = st.selectbox('Bowling Team',team_list, key='bowling_team_2')
batsmen_2 = st.text_input('Batsmen', key='batsmen_2')
bowlers_2 = st.text_input('Bowlers', key='bowlers_2')

if st.button('Run Prediction'):
    data_1 = {'venue': venue, 'innings': innings_1, 'batting_team': batting_team_1, 'bowling_team': bowling_team_1, 'batsmen': batsmen_1, 'bowlers': bowlers_1}
    data_2 = {'venue': venue, 'innings': innings_2, 'batting_team': batting_team_2, 'bowling_team': bowling_team_2, 'batsmen': batsmen_2, 'bowlers': bowlers_2}
    
    if not validate_inputs(data_1, data_2):
        st.stop()
        
    clear_files()
    
    write_to_csv(data_1)
    write_to_csv(data_2)
    
    main_page = st.empty()

    # Run prediction
    get_prediction()

    # Display prediction result
    main_page.title('Prediction Results')
    display_predictions()
    
    
    
    if st.button('Go Back'):
        st.rerun()
    
    
st.markdown('---')  # Horizontal line for separation
st.markdown('Reach out to me at [LinkedIn](https://www.linkedin.com/in/dhruv-pamneja-3b8432187/),[GitHub](https://github.com/d-pamneja) or [Email](mailto:dpamneja@gmailcom)') 