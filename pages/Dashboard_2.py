import streamlit as st
import pandas as pd
from app.db import get_connection 
from app.incidents import get_all_cyber_incidents
import sqlite3

conn = get_connection()
st.set_page_config(
    page_title='Dashbaord_c',
    page_icon=' ',
    layout='wide'
    
)

st.title('Cyber incidents dashboard\n--------------------------------------')
data = get_all_cyber_incidents(conn)

data['timestamp'] = pd.to_datetime(data['timestamp'])


with st.sidebar:
    st.header('Navigator')
    severity_ = st.selectbox('severity', data['severity'].unique())

filtered_data = data[data['severity'] == severity_]

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(filtered_data['category'].value_counts())

with col2:
    st.line_chart(filtered_data, x = 'timestamp', y = 'incident_id')

st.dataframe(filtered_data)