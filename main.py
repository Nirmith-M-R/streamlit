import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")
st.write("Hello, *World!* :sunglasses:")
st.write(1234)

df=pd.DataFrame({'first Column':[1,2,3,4],
                 'Second Column':[10,20,30,40]})
st.write(df)
st.write("Below is dataframe",df,"Above is dataframe")
df2=pd.DataFrame(np.random.rand(200,3),columns=['a','b','c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)