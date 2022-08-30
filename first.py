import streamlit as st 
st.title("my first app")
data=pd.read_csv("htp.csv")
st.dataframe(data)
