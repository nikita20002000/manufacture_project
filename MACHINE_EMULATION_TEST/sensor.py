class Sensor:
    class_description = 'Класс Sensor - эмулятор датчиков оборудования\n' \
                        'id: Идентификационный номер датчика\n' \
                        'type: тип датчика\n' \
                        'mark: показатель датчика\n' \
                        'state: состояние датчика'

    def __init__(self,
                 id: str,
                 type: str,
                 mark: 0,
                 state: str):
        self.id = id
        self.type = type
        self.mark = mark
        self.state = state

    def __str__(self):
        return f'(Датчик - {self.id}) \n' \
               f'     Тип датчика - {self.type} \n' \
               f'     Текущее состояние - {self.state}'

    def set_sensor(self):
        pass

    def set_state(self, new_state):
        pass

    def get_state(self):
        return self.state

    def get_mark(self):
        pass

    def get_type(self):
        return self.type


