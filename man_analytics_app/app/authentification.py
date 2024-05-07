import streamlit_authenticator as stauth


# Импорты
import yaml
from yaml.loader import SafeLoader

class login:
    @classmethod
    def authenticator(self):
        with open('../user_data/users.yaml') as f:
            config = yaml.load(f, Loader=SafeLoader)

        return stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['pre-authorized'],

        )