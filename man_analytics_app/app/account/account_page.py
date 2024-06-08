import streamlit as st

def show_account():
    st.title('Личный кабинет пользователя')
    st.markdown(f'### {st.session_state["name"]}')


    # Функционал смены и загрузки фото
    render_user_photo()

    a = st.file_uploader('Изменить фото профиля')

    if a:
        if st.button('Загрузить'):
            with open(f'../media/user_pic/{st.session_state.username}_pic.png', 'w') as f:
                f = a





    col_1, col_2 = st.columns(2)

    with col_1:
        st.text_area(label='Имя', placeholder=st.session_state.username, height=100)

    with col_2:
        st.text_area(label='Фамилия')


# Функционал смены и загрузки фото
def render_user_photo():
    try:
        st.image(f'../media/user_pic/{st.session_state.username}_pic.png', width=200)

    except:
        st.image(f'../media/user_pic/user_stock.png', width=200)
