import streamlit as st
from datetime import time, datetime

from authentification import login
from sidebar import show_leftbar

# Страницы системы
from home.home import show_hope_page


def main():
    log = login()
    auth = log.authenticator()
    auth.login()

    if st.session_state['authentication_status']:
        auth.logout('Выйти из аккаунта', 'sidebar')


        with st.sidebar:
            menu = show_leftbar()

        if menu.title() == 'Главная':
            show_hope_page()

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()
