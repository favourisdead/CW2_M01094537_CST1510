import streamlit as st
from app.incidents import get_all_cyber_incidents
from app.db import get_connection
from login_ import hash_password
from app.users import get_all_users
from app.users import add_user
from main import is_valid_hash
from main import get_user
conn = get_connection()



st.title('Welcome to the home page')
st.write('This is the home page')


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


if 'username' not in st.session_state:
    st.session_state['username'] = ''


if st.button('log in', key='main_login'):
    st.session_state['logged_in'] = True
    st.success("You are logged in")
    st.session_state['username'] = 'sam'


tab_log_in, tab_registration = st.tabs(["Login", "Register"])

with tab_log_in:
    st.header('Login')
    login_username = st.text_input('Username', key='login_user')
    login_password = st.text_input('Password', type='password', key='login_password')

    if st.button('Login', key='login_tab'):
        id, name, hash = add_user(conn, login_password, hash)
        
        if login_username == name and is_valid_hash(login_password, hash):
            st.session_state['logged_in'] = True
            st.switch_page('page/dashboard.py')
            st.success(f'You are logged in as {login_username}')
        st.session_state['logged_in'] = False



with tab_registration:
    st.header('Register')
    reg_username = st.text_input('Username', key='reg_user')
    reg_password = st.text_input('Password', type='password', key='reg_password')


    if st.button('register'):
        hash_password = hash_password(reg_password)
        add_user(conn, reg_username, hash_password)
        st.success('you have registered succesfully')
