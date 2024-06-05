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
    st.title('Мониторинг работы')
    st.header('Список оборудования')
    st.markdown('#### В данном разделе находится весь список оборудования и статус его работы')


    machines = update_work().sort_values('InWork', ascending=False)
    machines = machines.set_index('ID')
    print(machines.head())
    for machine in machines.index:

        col1, col2, col3, col4, col5 = st.columns(5, gap='small')


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
                    with st.popover(f'Статус ✅'):
                        st.markdown('### Оборудование работает исправно!')

                case 'Внимание':
                    with st.popover(f'Статус 🟠'):
                        st.markdown('### Обратить внимание на параметры работы оборудования')

                case 'Ошибка':
                    with st.popover(f'Статус ❗'):
                        st.markdown('### Критическая ошибка работы')



        st.html("""
        <style>
            h3 {
                margin-bottom: 20px;
            }
        </style>
        """)







def update_work():
    import numpy as np

    machine_df = read_machine_data()
    machine_df['InWork'] = np.random.randint(0,2, size=10)

    return machine_df