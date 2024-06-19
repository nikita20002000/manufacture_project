# TODO: Закончить общий функционал классов инструметов

class Instrument:
    def __init__(self,
                 instrument_id: str,
                 instrument_type: str,
                 tech_char: str,
                 tech_state: int,
                 state: str,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0
                 ):

        self.instrument_id = instrument_id
        self.instrument_type = instrument_type
        self.tech_char = tech_char
        self.tech_state = tech_state
        self.state = state
        self.defect_member = defect_member
        self.defect_member_counter = defect_member_counter
        self.defect_guilty = defect_guilty
        self.defect_guilty_counter = defect_guilty_counter

    def __repr__(self):
        return f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Класс Инструмент - эмулятор инструмента                                                                                                       |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  instrument_id (Идентификационный номер инструмента) {self.instrument_id}\n' \
               f'  instrument_type (тип инструмента) - {self.instrument_type}\n' \
               f'  tech_char (технические характеристики инструмента) - {self.tech_char}\n' \
               f'  tech_state (техническое состояние инструмента от 0 до 10) - {self.tech_state}\n' \
               f'  state (состояние инструмента) - {self.state}\n' \
               f'  defect_member_counter (Счетчик участия в браке) - {self.defect_member_counter}\n' \
               f'  defect_guilty (Виноват ли в браке) - {self.defect_guilty}\n' \
               f'  defect_guilty_counter - переменная / счетчик кол-ва раз вины в браке - {self.defect_guilty_counter}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n'


    def __str__(self):
        return f'(Инструмент - {self.instrument_id}) \n' \
               f'|   Тип инструмента - {self.instrument_type} \n' \
               f'|   Текущее состояние - {self.state}'

    def set_instrument(self):
        pass

    def get_state(self):
        return self.state

    def get_mark(self):
        pass

    def get_type(self):
        return self.type


