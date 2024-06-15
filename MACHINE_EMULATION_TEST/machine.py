class Machine:
    def __init__(self,
                 machine_id: str,
                 machine_type: str,
                 tech_char: str,
                 days_to_service: int,
                 max_power: int,
                 max_size: int,
                 stag_time: float,
                 is_working: bool,
                 instrument: object,
                 sensor: object,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0,
                 status=0,
                 ):
        self.machine_id = machine_id
        self.type = machine_type
        self.tech_char = tech_char
        self.days_to_service = days_to_service
        self.max_power = max_power
        self.max_size = max_size
        self.stag_time = stag_time
        self.is_working = bool(is_working)
        self.defect_member = defect_member
        self.defect_member_counter = defect_member_counter
        self.defect_guilty = defect_guilty
        self.defect_guilty_counter = defect_guilty_counter
        self.status = status
        self.instrument = instrument
        self.sensor = sensor

    def __repr__(self):
        return f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Класс Machine - эмулятор станка                                                                                                        |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  machine_id (Номер оборудования) - {self.machine_id}\n' \
               f'  machine_type (Тип оборудования) - {self.type}\n' \
               f'  tech_char (Короткое описание технических характеристик оборудования) - {self.tech_char}\n' \
               f'  days_to_service (кол-во дней до планового обслуживания) - {self.days_to_service}\n' \
               f'  max_power (максимальные показатели мощности) - {self.max_power}\n' \
               f'  max_size (показатели максимального размера обработки) - {self.max_size}\n' \
               f'  stag_time (время простоя оборудования) - {self.stag_time}\n' \
               f'  is_working (В работе или нет, -> Boolean) - {self.is_working}\n' \
               f'  defect_member (Участвовал ли в браке) - {self.defect_member}\n' \
               f'  defect_guilty (Виноват ли в браке) - {self.defect_guilty}\n' \
               f'  status (Статус оборудования (Показатели оборудования, предварительная оценка состояния оборудования, полученная от датчиков))) - {self.status}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  instrument (подключенный объект - инструмент) - {self.instrument}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  sensor (подключенные датчики мониторинга) - {self.sensor}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n'

    def __bool__(self):
        return self.is_working

    def __str__(self):
        return f'Станок - {self.id} \nТип оборудования - {self.type} \nБазовые технические характеристики - {self.tech_char}'

    # Дописать
    def prepare_to_work(self):
        pass

    def work(self):
        pass

    def stop_work(self):
        pass

    def end_of_work(self):
        pass

    def error(self):
        pass
