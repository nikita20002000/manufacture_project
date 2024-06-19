# Системные библиотеки
import streamlit as st
from datetime import datetime


# Аутентификация пользователей
from authentification import login


# Страницы системы
from sidebar import show_leftbar
from home.home import show_hope_page
from settings.user_config import show_settings
from task_manager.manager import show_manager
from client_managing.client_manager import show_client_manager
from calendar_p import calendar_page

from data_pages import journal, emloyee, machines, instruments

from account import account_page
import data_pages

def main():
    st.set_page_config(layout="wide")
    log = login()
    auth = log.authenticator()
    auth.login()

    if st.session_state['authentication_status']:
        auth.logout('Выйти из аккаунта', 'sidebar')

        journal.write_journal(f'Успешный вход - {st.session_state["name"]} |'
                              f' Время и дата входа - {datetime.now()}')
        with st.sidebar:
            menu = show_leftbar()

        match menu.title():
            case 'Дэшборд':
                show_hope_page()

            case 'Календарь':
                calendar_page.show_calendar()

            case 'Настройки':
                show_settings()

            case "Менеджер Задач":
                show_manager()

            case "CRM":
                pass

            case "Управление Клиентами":
                show_client_manager()

            case "Оборудование":
                machines.show_machines_page()

            case "Инструмент":
                pass

            case "Test":
                test()

            case "Сотрудники":
                emloyee.show_employee_page()

            case "Журнал":
                journal.show_journal_page()

            case "Личный Кабинет":
                account_page.show_account()



    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

def test():
    from streamlit_extras.metric_cards import style_metric_cards

    st.title('тестовая страница')
    st.header('Карточки')
    from streamlit_extras.metric_cards import style_metric_cards
    def example():
        col1, col2, col3 = st.columns(3)

        col1.metric(label="Gain", value=5000, delta=1000)
        col2.metric(label="Loss", value=5000, delta=-1000)
        col3.metric(label="No Change", value=5000, delta=0)

        style_metric_cards()

    example()

    st.header('Стилизованные всякие штуки контейнеры')
    from streamlit_extras.stylable_container import stylable_container
    def example_2():
        with stylable_container(
                key="green_button",
                css_styles="""
                button {
                    background-color: green;
                    color: white;
                    border-radius: 20px;
                }
                """,
        ):
            st.button("Green button")

        st.button("Normal button")

        with stylable_container(
                key="container_with_border",
                css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px)
                }
                """,
        ):
            st.markdown("This is a container with a border.")


    example_2()

    st.header('TODO')

    from streamlit_extras.stodo import to_do
    def example_3():
        to_do(
            [(st.write, "☕ Take my coffee")],
            "coffee",
        )
        to_do(
            [(st.write, "🥞 Have a nice breakfast")],
            "pancakes",
        )
        to_do(
            [(st.write, ":train: Go to work!")],
            "work",
        )
    example_3()

    st.header('Running widget')
    from streamlit_extras.customize_running import center_running
    import time

    def example_4():
        click = st.button("Observe where the 🏃‍♂️ running widget is now!")
        if click:
            center_running()
            time.sleep(2)
    example_4()

    # st.header('Падающие смайлы')
    #
    # from streamlit_extras.let_it_rain import rain
    #
    # def example_5():
    #     rain(
    #         emoji="🎈",
    #         font_size=54,
    #         falling_speed=5,
    #         animation_length="infinite",
    #     )
    # example_5()

    st.header('DF explorer')
    from streamlit_extras.dataframe_explorer import dataframe_explorer, generate_fake_dataframe

    def example_6():
        dataframe = generate_fake_dataframe(
            size=500, cols="dfc", col_names=("date", "income", "person"), seed=1
        )
        filtered_df = dataframe_explorer(dataframe, case=False)
        st.dataframe(filtered_df, use_container_width=True)

    example_6()
if __name__ == "__main__":
    main()

