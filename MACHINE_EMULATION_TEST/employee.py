class Employee:
    def __init__(self,
                 worker_id: str,
                 name: str,
                 surname: str,
                 age: int,
                 address: str,
                 is_working: bool,
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


class Machine_worker(Employee):
    def __init__(self, worker_id: str,
                 name: str,
                 surname: str,
                 age: int,
                 address: str,
                 is_working: bool,
                 instrument: object,
                 machine: object,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0,
                 violence_counter=0,
                 rating=10,):
        super().__init__(self, worker_id, name, surname, age, address, is_working, defect_member, defect_member_counter, defect_guilty, defect_guilty_counter, violence_counter, rating)
        self.instrument = instrument
        self.machine = machine




