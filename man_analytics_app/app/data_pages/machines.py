import streamlit as st
import streamlit_antd_components as sac
import time

def read_machine_data():
    import pandas as pd

    try:
        return pd.read_csv('../data/industrial_processes/machine_data/machines.csv')

    except Exception:
        return 'Ошибка чтения файла сотрудников'


def show_machines_page():
    st.title('Мониторинг работы')


    machines = update_work().sort_values('InWork', ascending=False)

    machines = update_work().sort_values('InWork', ascending=False)

    for machine in machines['ID']:
        process = machines['InWork'][machines['ID'] == machine]
        process_var = ''
        process_symbol = ''

        print(process)
        if process == True:
            process_var = 'Работает'
            process_symbol = '🟢'
        else:
            process_var = 'Отключен'
            process_symbol = '🔴'


        st.markdown(f'### ⚙️Станок :blue[{machine}] - {process_var} {process_symbol} ###')
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