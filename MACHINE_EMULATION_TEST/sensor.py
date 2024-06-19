# TODO: Закончить общий функционал классов датчиков

class Sensor:
    class_description = 'Класс Sensor - эмулятор датчиков оборудования\n' \
                        'id: Идентификационный номер датчика\n' \
                        'type: тип датчика\n' \
                        'mark: показатель датчика\n' \
                        'state: состояние датчика'

    def __init__(self,
                 sensor_id: str,
                 sensor_type: str,
                 mark: 0,
                 state: str):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.mark = mark
        self.state = state

    def __str__(self):
        return f'(Датчик - {self.sensor_id}) \n' \
               f'     Тип датчика - {self.sensor_type} \n' \
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
        return self.sensor_type


class Defect_sensor(Sensor):
    def __init__(self,
                 sensor_id: str,
                 sensor_type: str,
                 mark: 0,
                 state: str,
                 defect=False,
                 defect_counter=0):
        super().__init__(sensor_id, sensor_type, mark, state)
        self.defect = defect
        self.defect_counter = defect_counter

    # Перед началом работы показатель отрицательный
    def start_work(self):
        self.defect = False

    # По окончании работы идет расчет реального показателя (эмуляция)
    def end_work(self, operation_index):
        self.defect = operation_index

        if not self.defect:
            self.defect_counter += 1

    # ПРОВЕРЬ После всех технологических операций этот датчик отправит сообщение является ли браком конечное изделие

    # TODO доделать вывод функции
    def send_message(self):
        return f'| Окончание обработки заготовки до конечного изделия \n' \
               f'Результат - {"Брак" if self.defect else "Успешно ✅"}'


