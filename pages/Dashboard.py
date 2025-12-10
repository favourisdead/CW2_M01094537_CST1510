import streamlit as st
import pandas as pd
from app.metadata import get_all_dataset_metadata
from app.db import get_connection
from app.incidents import get_all_cyber_incidents
import sqlite3

conn = get_connection()


df = get_all_dataset_metadata(conn)

img = '/Users/samuelzionbaheten-ikeng/Downloads/Untitled11_20250310214328.png'
st.logo(img)
st.title("Dashboard\n------------------------------")

st.session_state['logged_in']
if not st.session_state['logged_in']:
    st.warning('please login to access dashboard')
    st.stop()
else:
    st.success(f'welcome, {st.session_state['username']}')
    

video_path = '/Users/samuelzionbaheten-ikeng/Downloads/youtube_zenitsu vs kaigaku.mp4'
st.video(video_path)

# Section
st.title('Zenitsu vs Kaigaku\n------------------------------------')
st.header('Home Page')

st.markdown("""
    <style>
        [data-testid="stHeader"] {
            background-color:  #f0f0f0 !important;
        }
    </style>
""", unsafe_allow_html=True)



st.sidebar.title("Side Bar\n--------------------------")
with st.sidebar:
    st.header('NAVIGATOR')
    uploaded_by = st.selectbox("uploaded_by", ['data_scientist', 'cyber_admin'])
    



name = st.text_input("Name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Enter name")







col1, col2 = st.columns(2)

with col1:
    st.subheader('**Customer name and id**\n-------------')
    st.bar_chart(x = 'name', y= 'dataset_id', data=df)

with col2:
    st.subheader('**Customers and coloumns**\n------------------')
    st.line_chart(df.set_index('name')['columns'])

st.write('------------------------------------\n Meta - data')

filtered = df.copy()  
with st.expander("See filtered data"):
    st.dataframe(df)


