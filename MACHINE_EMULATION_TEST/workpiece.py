class Workpiece:
    def __init__(self,
                 workpiece_id: str,
                 material: str,
                 size: float,
                 obtain_method: str,
                 defect_member=False,
                 defect_member_counter=0,
                 defect_guilty=False,
                 defect_guilty_counter=0,
                 workpiece_defect=False
                 ):
        self.workpiece_id = workpiece_id
        self.material = material
        self.size = size
        self.obtain_method = obtain_method
        self.defect_member = defect_member
        self.defect_member_counter = defect_member_counter
        self.defect_guilty = defect_guilty
        self.defect_guilty_counter = defect_guilty_counter
        self.workpiece_defect = workpiece_defect


    def __repr__(self):
        return f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'| Класс Заготовка - эмулятор заготовки                                                                                                       |\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'  workpiece_id (ID заготовки) - {self.workpiece_id}\n' \
               f'  material (Материал заготовки) - {self.material}\n' \
               f'  size (Размер заготовки) - {self.size}\n' \
               f'  obtain_method (способ получения заготовки) - {self.obtain_method}\n' \
               f'  defect_member (Участвовал ли в браке) - {self.defect_member}\n' \
               f'  defect_member_counter (Счетчик участия в браке) - {self.defect_member_counter}\n' \
               f'  defect_guilty (Виноват ли в браке) - {self.defect_guilty}\n' \
               f'  defect_guilty_counter - переменная / счетчик кол-ва раз вины в браке - {self.defect_guilty_counter}\n' \
               f'  workpiece_defect (брак заготовки) - {self.workpiece_defect}\n' \
               f'+----------------------------------------------------------------------------------------------------------------------------------------+\n'

    def load_workpiece(self):
        pass

