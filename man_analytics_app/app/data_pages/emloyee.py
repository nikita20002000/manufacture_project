import pandas as pd
import streamlit as st
import streamlit_antd_components as sac



def read_employee_data():
    import pandas as pd

    try:
        return pd.read_csv('../data/company_data/employee.csv')

    except Exception:
        return 'Ошибка чтения файла сотрудников'


def show_employee_page():
    st.title('Сотрудники')

    employee_data = read_employee_data()
    st.data_editor(employee_data.set_index(pd.Index(employee_data['ID'])), width=1200, height=800)

    st.markdown('## :green[Сейчас в работе] ##')
    employee_in_work = employee_data[employee_data['Работает'] == 1]
    st.data_editor(employee_in_work)