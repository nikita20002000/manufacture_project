import time

import streamlit as st
import streamlit_antd_components as sac
import yaml
from yaml.loader import SafeLoader


def check_tasks():
    with open('../user_data/users.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)

        return config['credentials']['usernames'][st.session_state["username"]]['tasks']


# ОСНОВНАЯ ПАНЕЛЬ ОТОБРАЖЕНИЯ
def show_manager():

    # Создаем меню навигации по менеджеру
    tabs = sac.tabs([
        sac.TabsItem(label='Задачи', tag='🔥'),
        sac.TabsItem(label='Эффективность'),
        sac.TabsItem(label='Проекты', tag='soon'),
    ], format_func='title', variant='outline')

    match tabs.title():
        case 'Задачи':
            task_manager()

        case 'Эффективность':
            efficiency_manager()

        case 'Проекты':
            project_manager()


#   ПАНЕЛЬ ЗАДАЧ
def task_manager():
    st.title('Менеджер задач')
    # Получаем список задач пользователя
    tasks = check_tasks()

    if tasks == 0:
        st.header('У вас нет ни одной задачи для выполнения')

    else:
        st.header(f'У вас {len(tasks)} {correct_sent(len(tasks))}')
        show_tasks(tasks)

    st.markdown('*Нажмите кнопку ниже, чтобы добавить :blue[задачи]*')

    placeholder = st.empty()

    create_but = placeholder.button('Создать задачу', type='secondary')

    if create_but:
        placeholder.empty()

        with st.form('task-form'):
            task_name = st.text_input(label='Название задачи', key='name', max_chars=30,
                                      placeholder='Введите название задачи')
            task_description = st.text_input(label='Описание задачи', key='desc', max_chars=120,
                                             placeholder='Введите описание задачи')
            task_deadline = st.date_input(label='Дедлайн', key='deadline')
            complete = st.checkbox('Завершена', key='complete')

            submit = st.form_submit_button('dffds', on_click=create_task)




# Функционал создания новой задачи
def create_task():
    with open('../user_data/users.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)

        if config['credentials']['usernames'][st.session_state['username']]['tasks'] == 0:
            config['credentials']['usernames'][st.session_state["username"]]['tasks'] = {
                st.session_state.name: {
                    'description': st.session_state.desc,
                    'deadline': st.session_state.deadline,
                    'complete': st.session_state.complete
                }
            }
        else:
            config['credentials']['usernames'][st.session_state["username"]]['tasks'][st.session_state.name] = {
                'description': st.session_state.desc,
                'deadline': st.session_state.deadline,
                'complete': st.session_state.complete
            }



    with open('../user_data/users.yaml', 'w') as update_file:
        yaml.dump(config, update_file)


# Функция отображения задач на панели 🫡
def show_tasks(tasks):
    import pandas as pd


    tasks_df = [
        {'Название задачи': i, 'Описание': tasks[i]["description"], 'Срок': tasks[i]["deadline"], 'Статус':tasks[i]["complete"]} for i in tasks.keys()
    ]

    st.data_editor(tasks_df, width=800,)



# Функция возврата правильного окончания слово задач 😎
def correct_sent(num: int):
    import math
    nouns_list = [
        'незавершенная задача',
        'незавершенных задачи',
        'незавершенных задач',
        'задач'
    ]
    num = abs(num) % 100

    if num == 0:
        return nouns_list[3]
    if num > 10 & num < 20:
        return nouns_list[2]
    if num >= 5 & num < 10:
        return nouns_list[1]
    if num == 1:
        return nouns_list[0]


# ЭФФЕКТИВНОСТЬ
def efficiency_manager():
    import matplotlib.pyplot as plt
    st.title('Эффективность')

    tasks = check_tasks()

    # Подготовка данных для диаграммы
    from collections import Counter
    counter = Counter(tasks[j]['complete'] for j in tasks.keys())

    done = {
        'Незавершенные': int(counter[False]),
        'Завершенные': int(counter.get(True, 0))
    }

    # Построение и вывод диаграммы
    fig, ax = plt.subplots()
    # ax.pie(dict(done).values(), labels=dict(done).keys(), colors='cyan')
    pathches, text = ax.pie(done.values(), labels=done.keys(), colors='cyan')
    for t in text:
        t.set_color('white')
    plt.legend(pathches, done.keys())

    col_diagramm, col_chart = st.columns(2, gap='medium')
    col_diagramm.pyplot(fig, clear_figure=True, transparent=True)



    col_chart.write('График')



# ПРОЕКТЫ
def project_manager():
    st.markdown('# :blue[SOON]')