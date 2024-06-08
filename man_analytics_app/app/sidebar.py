import streamlit as st

def show_leftbar():
    import streamlit_antd_components as sac

    return sac.menu([
        sac.MenuItem('Главная', icon='house-fill'),

        sac.MenuItem('Календарь', icon='calendar-range'),
        sac.MenuItem('Менеджер задач', icon='list-task'),
        sac.MenuItem('CRM', icon='kanban-fill'),
        sac.MenuItem('Управление клиентами', icon='people-fill'),

        sac.MenuItem('Мониторинг', icon='box-fill', children=[
            sac.MenuItem('Оборудование', icon='cpu'),
            sac.MenuItem('Инструмент', icon='screwdriver'),
            sac.MenuItem('Сотрудники', icon='people-fill'),
            sac.MenuItem('Журнал', icon='calendar2-range-fill'),

        ]),
        sac.MenuItem('Контроль производства', icon='cone-striped'),

        sac.MenuItem(type='divider'),

        sac.MenuItem('Личный кабинет', icon='person-fill'),
        sac.MenuItem('Настройки', icon='gear-fill'),

        sac.MenuItem(type='divider'),

        sac.MenuItem('', type='group', children=[
            sac.MenuItem('Обо мне', icon='heart-fill'),
            sac.MenuItem('Поддержка Bootstrap', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
            sac.MenuItem('GitHub Nikita20002000', icon='github', href='https://github.com/nikita20002000')
        ]),
        ], color='#4682b4', open_all=True)



