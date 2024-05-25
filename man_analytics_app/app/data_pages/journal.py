import streamlit as st
import streamlit_antd_components as sac

import yaml


# Функция записи в журнал активность пользователей
def write_journal(message):
    with open('../data/journal/journal.txt', 'a') as f:
        f.write(message + '\n')


# Функция чтения журнала активности пользователей
def read_journal():
    with open('../data/journal/journal.txt', 'r') as f:
        information = f.readlines()
    return information


def read_error_journal():
    try:
        with open('../data/journal/error_journal.txt', 'r') as errors_file:
            errors_info = errors_file.readlines()

    except Exception:
        return f'Ошибка чтения файла :blue[error_journal.txt]'




# Функция чтения журнала контроля версий и изменений
def read_version_control_changes():
    try:
        with open('../data/journal/version_control_changes.txt', 'r') as version_file:
            version_info = version_file.readlines()

        return version_info

    except Exception:
        return 'Ошибка чтения файла обновлений'




# ОСНОВНАЯ ПАНЕЛЬ ОТОБРАЖЕНИЯ
def show_journal_page():

    # Создаем меню навигации по менеджеру
    journal_tabs = sac.tabs([
        sac.TabsItem(label='Активность', tag='👨🏽‍💻'),
        sac.TabsItem(label='Системные ошибки', tag='🚨'),
        sac.TabsItem(label='Журнал изменений', tag='📝'),
    ], format_func='title', variant='outline')


    match journal_tabs.title():
        case 'Активность':
            activity_journal()

        case 'Системные Ошибки':
            sys_err_journal()

        case 'Журнал Изменений':
            version_control_journal()


def activity_journal():
    st.title('Активность пользователей')
    activity = read_journal()

    st.table(activity)



def sys_err_journal():
    st.title('Журнал ошибок системы')
    st.markdown('### Отображение истории сбоев работы системы и ошибок при обработке информации ###')

    if read_error_journal() == None:
        st.write('Ошибок нет')
    else:
        st.write(read_error_journal())




def version_control_journal():
    st.title('Журнал изменений')

    st.markdown('### V 0.1 PreBETA (MVP) ###')

    data = read_version_control_changes()
    st.markdown(data)


