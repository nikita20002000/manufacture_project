import streamlit as st


from authentification import login
from sidebar import show_leftbar

# Страницы системы
from home.home import show_hope_page
from settings.user_config import show_settings
from task_manager.manager import show_manager
from calendar_p import calendar_page


def main():
    log = login()
    auth = log.authenticator()
    auth.login()

    if st.session_state['authentication_status']:
        auth.logout('Выйти из аккаунта', 'sidebar')

        with st.sidebar:
            menu = show_leftbar()

        match menu.title():
            case 'Главная':
                show_hope_page()

            case 'Календарь':
                calendar_page.show_calendar()

            case 'Настройки':
                show_settings()

            case "Менеджер Задач":
                show_manager()

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    main()
