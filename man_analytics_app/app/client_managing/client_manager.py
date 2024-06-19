import streamlit as st
import streamlit_antd_components as sac

def open_client_data():
    import pandas as pd
    with open("../data/company_data/client_data.csv", "rb") as f:
        return pd.read_csv(f)

def show_client_manager():

    clients_manager_tabs = sac.tabs([
        sac.TabsItem(label='База данных клиентов'),
        sac.TabsItem(label='Система кластеризации клиентов'),
        sac.TabsItem(label='Панель рассылок', tag='soon'),
        sac.TabsItem(label='Дополнительные сведения', tag='soon')
    ], format_func='title', variant='outline')

    match clients_manager_tabs.title():
        case "База Данных Клиентов":
            show_clients_db()

        case "Система Кластеризации Клиентов":
            show_claster_panel()

        case "Панель Рассылок":
            show_messaging_panel()


def show_claster_panel():
    # TODO: Дописать полностью раздел / добавить цвета элементов и стили
    st.title("Панель управления клиентами")
    st.header("Кластеризация клиентов")

    client_data = open_client_data()

    st.markdown("## :blue[Новые клиенты]")
    st.data_editor(client_data[client_data['Mark'] == 'Новые клиенты'].drop("Mark", axis=1), width=2400)
    # Первая группа клиентов
    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        st.html("<h2 style='color: red'> Высокий риск потери</h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Высокий риск потери'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')


    with col_2:
        st.html("<h2 style='color: orange'> В зоне риска </h3>")
        st.data_editor(client_data[client_data['Mark'] == 'В зоне риска'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    with col_3:
        st.html("<h2 style='color: gray'> Высокий риск потери</h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Неактивные'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')


    # Вторая группа клиентов

    col_4, col_5, col_6 = st.columns(3)

    with col_4:
        st.html("<h2 style='color: rgb(156, 141, 224)'> Высокий риск потери</h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Лояльные'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    with col_5:
        st.html("<h2 style='color: rgb(174, 163, 65)'> Обратить внимание</h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Обратить внимание'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    with col_6:
        st.html("<h2 style='color: rgb(92, 79, 23)'> Близкие к неактивным </h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Близкие к неактивным'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    col_7, col_8, col_9 = st.columns(3)

    with col_7:
        st.html("<h2 style='color: rgb(99, 202, 209)'> Многообещающие </h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Многообещающие'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    with col_8:
        st.html("<h2 style='color: rgb(159, 205, 97)'> Потенциально лояльные </h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Потенциально лояльные'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')

    with col_9:
        st.html("<h2 style='color: rgb(80, 164, 138)'> Чемпионы </h3>")
        st.data_editor(client_data[client_data['Mark'] == 'Чемпионы'].drop("Mark", axis=1), width=2400)

        with st.popover('Рекомендации по работе'):
            st.markdown('Здесь отображаются рекомендации по работе с кластером')


def show_clients_db():
    st.title('База данных клиентов')
    st.data_editor(open_client_data().drop("Mark", axis=1), width=2400)


from streamlit_elements import elements, mui, html
def show_messaging_panel():
    st.title('Панель рассылок и работы с клиентами')

    with elements("dashboard"):
        # You can create a draggable and resizable dashboard using
        # any element available in Streamlit Elements.

        from streamlit_elements import dashboard

        # First, build a default layout for every element you want to include in your dashboard

        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_item", 0, 0, 2, 2),
            dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
            dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
        ]

        # Next, create a dashboard layout using the 'with' syntax. It takes the layout
        # as first parameter, plus additional properties you can find in the GitHub links below.

        with dashboard.Grid(layout):
            mui.Paper("First item", key="first_item")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Third item (cannot resize)", key="third_item")

        # If you want to retrieve updated layout values as the user move or resize dashboard items,
        # you can pass a callback to the onLayoutChange event parameter.

        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)

        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            mui.Paper("First item", key="first_item")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Third item (cannot resize)", key="third_item")

    with elements("nivo_charts"):
        # Streamlit Elements includes 45 dataviz components powered by Nivo.

        from streamlit_elements import nivo

        DATA = [
            {"taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114},
            {"taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72},
            {"taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99},
            {"taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30},
            {"taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103},
        ]

        with mui.Box(sx={"height": 500}):
            nivo.Radar(
                data=DATA,
                keys=["chardonay", "carmenere", "syrah"],
                indexBy="taste",
                valueFormat=">-.2f",
                margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                borderColor={"from": "color"},
                gridLabelOffset=36,
                dotSize=10,
                dotColor={"theme": "background"},
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )