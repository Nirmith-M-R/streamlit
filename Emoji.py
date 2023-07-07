import streamlit as st 
import numpy as np 
import pandas as np 

st.markdown("Emoji's Multiplier :pencil:")
emojis=[":smile:",":100:",":rice:", ":cookie:", ":chocolate_bar:", ":grinning:"," :grin: ",":joy:",":smiley:",":sweat_joy:"]
emoji=st.selectbox("Select emoji", emojis)

count=st.text_input("Enter count")

st.write(emoji*count)
