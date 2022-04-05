import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai',
       'Jaipur', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Bengaluru']

pipe = pickle.load(open('pipe1.pkl', 'rb'))

st.title('IPL WIN PREDICTOR')
st.image('https://crickettimes.com/wp-content/uploads/2021/02/IPL-2021-complete-squads-1260x657.jpg')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select The Batting Team', sorted(teams))  

with col2:
    bowlling_team = st.selectbox('Select The Bowling Team', sorted(teams))  

selected_city = st.selectbox('Select Host City', sorted(cities))
target = st.number_input('Taget')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Over Done')

with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probability'):
    runs_left = target - score
    bowls_left = 120 - overs*6
    wicket = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/bowls_left


    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowlling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[bowls_left],'wicket_left':[wicket],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowlling_team + "- " + str(round(loss*100)) + "%")
