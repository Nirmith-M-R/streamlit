import streamlit as st
st.header("Check Cost Price:")
#st.subheader("Enter Initial")
i=st.text_input("Enter:")

dic={'k':1,'e':2,'y':3,'c':4,'h':5,'a':6,'i':7,'n':8,'s':9,'o':0,'O':0,
     'K':1,'E':2,'Y':3,'C':4,'H':5,'A':6,'I':7,'N':8,'S':9}
cost=0
check=st.button("Check")
if check:
    for k in i:
        cost*=10
        cost+=dic[k]
st.write("Price is:")
st.write(cost)