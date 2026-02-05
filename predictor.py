import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
st.set_page_config(page_icon="🏏",page_title="score prediction")
st.title("**🏏 CRICKET SCORE PREDICTOR**")
# st.write("Cricket is often called the *game of gentlemen* because it emphasizes fair play, respect, and sportsmanship. Players are expected to follow the rules honestly and show respect toward opponents, officials, and the spirit of the game. Along with physical skill and strategy, cricket values discipline and good conduct on and off the field. This tradition of integrity and mutual respect is what gives cricket its reputation as a noble and gentlemanly sport")
model = joblib.load(r"d:\nikhil\python\ds\project3.py\score.joblib")
team_encoder = pickle.load(open(r"d:\nikhil\python\ds\project3.py\team.pkl", "rb"))
city_encoder = pickle.load(open(r"d:\nikhil\python\ds\project3.py\own.pkl","rb"))
team_encode = pickle.load(open(r"d:\nikhil\python\ds\project3.py\trans.pkl","rb"))

team=st.selectbox(label="batting team",options=team_encoder.classes_)
team2=st.selectbox(label="bowling team",options=team_encoder.classes_)
venue=st.selectbox(label="venue",options=city_encoder.classes_)

batteam= team_encoder.transform([team])[0]
bowling_team = team_encoder.transform([team2])[0]
city_enc = city_encoder.transform([venue])[0]


delivery_left=st.number_input(label="deliveries left(bowls left)",min_value=1)
score=st.number_input(label="current score",min_value=1)
runrate=st.number_input(label="current runrate")
wicket=st.number_input(label="wickets left",min_value=1)
runlast=st.number_input(label="run in last 5 overs",min_value=0)
wiklast=st.number_input(label="wicket in last 5 overs",min_value=0)
innings=st.number_input(label="inning",min_value=1,max_value=2)
st.session_state.data=[batteam,bowling_team,city_enc,delivery_left,score,runrate,wicket,runlast,wiklast,innings]
if st.button(label="predict"):
    res=model.predict([st.session_state.data])
    st.write(res)