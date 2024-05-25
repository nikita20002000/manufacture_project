import random

import pandas as pd


workers = pd.read_csv('../../data/industrial_processes/workers/workers.csv')
workpieces = pd.read_csv('../../data/industrial_processes/workpieces/workpieces.csv')
instruments = pd.read_csv('../../data/industrial_processes/instruments/instrumets.csv')
machines = pd.read_csv('../../data/industrial_processes/machine_data/machines.csv')

def get_random_number():
    import random
    return random.randint(1, 10)

def workpiece_control():
    return random.choice(['YES', 'YES', 'YES', 'NO',])

def tech_epoch_control():
    return random.choice(['Брак', 'Не брак', 'Не брак', 'Не брак'])


def start_producing():
    work_list = []
    work_list.append(f'WP00{get_random_number()}')

    if workpiece_control() == 'NO':
        work_list.append('❌')
        return work_list

    else:
        work_list.append('✅')
        for n in range(random.randint(1,3)):
            work_list.append(f'Операция {n+1}')

            work_list.append(f'W00{get_random_number()}')
            work_list.append(f'M00{get_random_number()}')
            work_list.append(f'I00{get_random_number()}')

            if tech_epoch_control() == 'Брак':
                work_list.append('Брак')
                break
            else:
                work_list.append('Успешно')


    return work_list

import csv

with open('results.csv', 'a', newline="") as res_file:
    writer = csv.writer(res_file)
    for i in range(100):
        writer.writerow(start_producing())