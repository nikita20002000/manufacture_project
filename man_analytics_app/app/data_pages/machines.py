import random

import streamlit as st
import streamlit_antd_components as sac
import time

def read_machine_data():
    import pandas as pd

    try:
        return pd.read_csv('../data/industrial_processes/machine_data/machines.csv')

    except Exception:
        return 'Ошибка чтения файла оборудования'


def show_machines_page():

    # Стили добавляем в разметку страницы
    local_css("static/style.css")

    # Импортируем бутстрап
    import_bootstrap()

    st.title('Мониторинг работы')
    st.header('Список оборудования')
    st.markdown('#### В данном разделе находится весь список оборудования и статус его работы')


    machines = update_work().sort_values('InWork', ascending=False)
    machines = machines.set_index('ID')



    for machine in machines.index:

        col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')


        with col1:
            st.markdown(f'### ⚙️')

        with col2:
            st.markdown(f'### Станок :blue[{machine}]')

        with col3:
            st.markdown('### |')

        with col4:
            if machines.at[machine, 'InWork']:
                st.markdown('### В работе')

            else:
                st.markdown('### Отключен')

        with col5:
            match machines.at[machine, 'MachineStatus']:

                case 'ОК':
                    with st.popover('Статус ✅'):
                        st.markdown('### Оборудование работает исправно!')

                case 'Внимание':
                    with st.popover(f'Статус 🟠'):
                        st.markdown('### Обратить внимание на параметры работы оборудования')

                case 'Ошибка':
                    with st.popover(f'Статус ❗'):
                        st.markdown('### Критическая ошибка работы')


        with col6:
            with st.popover('Сведения'):
                st.markdown('### Здесь будут отображаться дополнительные сведения о неисправностях!!!')

        st.html("""
        <style>
            h3 {
                margin-bottom: 20px;
            }
        </style>
        """)
        st.html("""
        <div class='container-fluid divider'></div> 
        
        """)


def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def import_bootstrap():
    st.markdown(f'<script src = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity = "sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin = "anonymous" > < / script >', unsafe_allow_html=True)



def update_work():
    import numpy as np

    machine_df = read_machine_data()
    machine_df['InWork'] = np.random.randint(0,2, size=10)

    return machine_df

