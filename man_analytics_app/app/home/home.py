import streamlit as st

def show_hope_page():
    st.image('../media/logo.png')


    st.title(f'{check_time()} {st.session_state["name"]} ⏱')



# Получение времени и подготовка ответа пользователю ⏱️
def check_time():
    from datetime import datetime

    time = datetime.now().time().hour
    match time:
        case 5 | 6 | 7 | 8 | 9 | 10 | 11:
            return "Доброе утро"

        case 12 | 13 | 14 | 15 | 16:
            return "Добрый день"

        case 17 | 18 | 19 | 20 | 21 | 22 | 23:
            return "Добрый вечер"

        case 24 | 1 | 2 | 3 | 4:
            return "Доброй ночи"

    return