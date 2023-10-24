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

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL WIN PREDICTOR')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('SELECT BATTING TEAM',sorted(teams))
with col2:
    bowling_team = st.selectbox('SELECT BOWLING TEAM',sorted(teams))

selected_city = st.selectbox('SELECT HOST CITY',sorted(cities))

target = st.number_input('TAREGT')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('SCORE')

    if(score>280):
        st.subheader("INVALID SCORE")
with col4:
    overs = st.number_input('OVERS COMPLETED')

    if(overs>20):
        st.subheader("INVALID OVERS")
with col5:
    wickets = st.number_input('WICKETS OUT')

    if(wickets>10):
        st.subheader("INVALID WICKETS")

if st.button('PREDICT PROBABILITY') and bowling_team!=batting_team:
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'Team1':[bowling_team],'BattingTeam':[batting_team],'City':[selected_city],'runs_left':[runs_left],'wicket':[wickets],'total_run_x':[target],'balls_left':[balls_left],'curr_run_rate':[crr],'required_run_rate':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
else:
    st.subheader("CHOOSE CORRECT TEAMS")
