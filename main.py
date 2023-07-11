import streamlit as st
import pandas as pd

data = {
  'series_1':[1,2,3,4,5],
  'series_2':[6,7,8,9,10]
}

df = pd.DataFrame(data)


st.title('Our first streamlit')
st.subheader('Intro to dashboard with python')
st.write('''Benvenuti in''')

st.write(df)