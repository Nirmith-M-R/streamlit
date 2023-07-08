import streamlit as st 
import numpy as np 
import pandas as np 

st.markdown("Emoji's Multiplier :smile:")
emojis=[":smile:",":100:",":rice:", ":cookie:", ":chocolate_bar:", ":grinning:",":grin:",":joy:",":smiley:",":sweat_smile:"]
emoji=st.selectbox("Select emoji", emojis)

count=st.number_input("Enter count",value=0,min_value=1,max_value=200,step=1)

st.write(emoji*int(count))
