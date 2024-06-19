# TODO написать тесты (как получится)

from machine import Machine
from sensor import Sensor
from employee import Employee, Machine_worker
from instrument import Instrument

# TODO: Организовать полностью эмуляцию рабочего процесса


sensor_1 = Sensor(id='str',
                  type='str',
                  mark=10,
                  state='str')

inst_1 = Instrument(instrument_id='str',
                    instrument_type='str',
                    tech_char='str',
                    tech_state=19,
                    state='str')

machine_1 = Machine(machine_id='str',
                    machine_type='str',
                    tech_char='str',
                    days_to_service=10,
                    max_power=10,
                    max_size=12,
                    stag_time=10.0,
                    is_working=True,
                    instrument=inst_1,
                    sensor=sensor_1)

w_1 = Machine_worker(worker_id='str',
                     name='str',
                     surname='str',
                     age=129,
                     address='str',
                     is_working=1,
                     instrument=inst_1,
                     machine=machine_1)


w_1.total_operations += 10242
w_1.defect_guilty_counter += 221
w_1.calculate_rating()
print(repr(w_1))

