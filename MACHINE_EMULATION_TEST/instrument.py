class Instrument:
    class_description = 'Класс Instrument - эмулятор инструментов в револьверной головке станка\n' \
                        'instrument_id: Идентификационный номер инструмента\n' \
                        'instrument_type: тип инструмента\n' \
                        'tech_char - технические характеристики инструмента' \
                        'tech_state - техническое состояние инструмента от 0 до 10' \
                        'state: состояние инструмента' \
                        'defect_member - участвовал ли в браке' \
                        'defect_member_counter - переменная / счетчик кол-ва раз участия в браке' \
                        'defect_guilty - виноват ли в браке (True / False)' \
                        'defect_guilty_counter - переменная / счетчик кол-ва раз вины в браке'

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

        self.id = instrument_id
        self.type = instrument_type
        self.tech_char = tech_char
        self.tech_state = tech_state
        self.state = state
        self.defect_member = defect_member
        self.defect_member_counter = defect_member_counter
        self.defect_guilty = defect_guilty
        self.defect_guilty_counter = defect_guilty_counter

    def __str__(self):
        return f'(Датчик - {self.id}) \n' \
               f'     Тип датчика - {self.type} \n' \
               f'     Текущее состояние - {self.state}'

    def set_instrument(self):
        pass

    def get_state(self):
        return self.state

    def get_mark(self):
        pass

    def get_type(self):
        return self.type


