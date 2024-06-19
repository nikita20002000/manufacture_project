# ПРОВЕРЬ Общий функционал готов, проверь его еще раз

class Employee:
    def __init__(self,
                 worker_id: str,
                 name: str,
                 surname: str,
                 age: int,
                 address: str,
                 is_working: bool or int,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0,
                 violence_counter=0,
                 rating=10,
                 ):
        self.worker_id = worker_id
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.is_working = bool(is_working)
        self.defect_member = defect_member
        self.defect_member_counter = defect_member_counter
        self.defect_guilty = defect_guilty
        self.defect_guilty_counter = defect_guilty_counter
        self.violence_counter = violence_counter
        self.rating = rating

    def __repr__(self):
        return f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Класс Employee - Родительский класс работник                                                                                           |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  worker_id (ID работника) - {self.worker_id}\n' \
               f'  name (Имя сотрудника) - {self.name}\n' \
               f'  surname (Фамилия сотрудника) - {self.surname}\n' \
               f'  age (Возраст сотрудника) - {self.age}\n' \
               f'  address (Адрес сотрудника) - {self.address}\n' \
               f'  is_working (В работе или нет -> BOOL) - {self.is_working}\n' \
               f'  defect_member (Участвовал ли в браке) - {self.defect_member}\n' \
               f'  defect_member_counter (Счетчик участия в браке) - {self.defect_member_counter}\n' \
               f'  defect_guilty (Виноват ли в браке) - {self.defect_guilty}\n' \
               f'  defect_guilty_counter (Счетчик вины в браке) - {self.defect_guilty_counter}\n' \
               f'  violence_counter (Счетчик замечаний) - {self.violence_counter}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| РЕЙТИНГ СОТРУДНИКА - {self.rating}                                                                                                                |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n'

    def work(self):
        self.is_working = True

    def stop_work(self):
        self.is_working = False

    def get_reproof(self):
        self.violence_counter += 1

    def calculate_rating(self):
        pass


class Machine_worker(Employee):
    def __init__(self, worker_id: str,
                 name: str,
                 surname: str,
                 age: int,
                 address: str,
                 is_working: bool or int,
                 instrument: object,
                 machine: object,
                 total_operations=0,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0,
                 violence_counter=0,
                 rating=10,
                 ):
        super().__init__(worker_id, name, surname, age, address, is_working, defect_member, defect_member_counter, defect_guilty, defect_guilty_counter, violence_counter, rating)
        self.total_operations = total_operations
        self.instrument = instrument
        self.machine = machine

    def __repr__(self):
        return f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Класс Machine_worker                                                                                       |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  worker_id (ID работника) - {self.worker_id}\n' \
               f'  name (Имя сотрудника) - {self.name}\n' \
               f'  surname (Фамилия сотрудника) - {self.surname}\n' \
               f'  age (Возраст сотрудника) - {self.age}\n' \
               f'  address (Адрес сотрудника) - {self.address}\n' \
               f'  is_working (В работе или нет -> BOOL) - {self.is_working}\n' \
               f'  total_operations - количество операций с участием {self.total_operations}\n' \
               f'  defect_member (Участвовал ли в браке) - {self.defect_member}\n' \
               f'  defect_member_counter (Счетчик участия в браке) - {self.defect_member_counter}\n' \
               f'  defect_guilty (Виноват ли в браке) - {self.defect_guilty}\n' \
               f'  defect_guilty_counter (Счетчик вины в браке) - {self.defect_guilty_counter}\n' \
               f'  violence_counter (Счетчик замечаний) - {self.violence_counter}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Инструмент - {self.instrument}                                                                                                                \n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Рабочий станок - {self.machine}                                                                                                                \n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| РЕЙТИНГ СОТРУДНИКА - {self.rating}                                                                                                                |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n'

    def work(self):
        super().work()
        return 'Рабочий работает'

    def change_instrument(self, new_instrument):
        self.instrument = new_instrument

    def change_machine(self, new_machine):
        self.machine = new_machine

    def calculate_rating(self):
        if self.total_operations == 0:
            self.rating = 10
        else:
            self.rating = round(((self.total_operations - self.defect_guilty_counter) / self.total_operations) * 10, 2)

