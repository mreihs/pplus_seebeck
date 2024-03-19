# read csv file and clean the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# read csv file
def read_csv(file_path):
    # , is used as decimal separator in the csv file
    # ; is used as column separator in the csv file
    # skip the first row
    data = pd.read_csv(file_path, decimal=',', sep=';', skiprows=[1])
    return data


def read_all_files(path, filename_prefix, number_of_files):
    data = []
    for i in range(1, number_of_files + 1):
        if i < 10:
            file = filename_prefix + '0' + str(i) + '.csv'
        else:
            file = filename_prefix + str(i) + '.csv'
        
        file_path = os.path.join(path, file)
        data.append(read_csv(file_path))

    return data

def fix_time(datasets):
    # convert the time to the time + the highest time of the previous file
    previous_time = 0
    for i in range(len(datasets)):
        datasets[i]['Time'] = datasets[i]['Time'] + previous_time
        previous_time = datasets[i]['Time'].max()
    return datasets


# function that saves the data to a csv file
def save_to_csv(data, file_name):
    data.to_csv(file_name, index=False)

# channel A - type T thermocouple
# channel B - Nickel Copper thermocouple
# heating from -200 to above 0 C
messung_1 = read_all_files('data_raw/Messung_1', 'Messung_1_', 16)
messung_1 = fix_time(messung_1)
messung_1 = pd.concat(messung_1)
save_to_csv(messung_1, 'data_combined/messung_1.csv')
print(messung_1.head())

# channel A - type T thermocouple
# channel B - Nickel Copper thermocouple
# cooling from 100 to = C
messung_2 = read_all_files('data_raw/Messung_2_Dritter_Versuch', 'Messung_2_Dritter_Versuch_', 17)
messung_2 = fix_time(messung_2)
messung_2 = pd.concat(messung_2)
save_to_csv(messung_2, 'data_combined/messung_2.csv')
print(messung_2.head())

# channel A - Copper Graphene thermocouple
messung_3 = read_all_files('data_raw/KupferGraphen', 'KupferGraphen_', 9)
messung_3 = fix_time(messung_3)
messung_3 = pd.concat(messung_3)
save_to_csv(messung_3, 'data_combined/messung_3.csv')
print(messung_3.head())

# channel A - Copper Graphite thermocouple
messung_4 = read_all_files('data_raw/Messung_Vier', 'Messung_Vier_', 9)
messung_4 = fix_time(messung_4)
messung_4 = pd.concat(messung_4)
save_to_csv(messung_4, 'data_combined/messung_4.csv')
print(messung_4.head())

# channel A - Graphene Graphite thermocouple
messung_5 = read_all_files('data_raw/Messung_5', 'Messung_5_', 9)
messung_5 = fix_time(messung_5)
messung_5 = pd.concat(messung_5)
save_to_csv(messung_5, 'data_combined/messung_5.csv')
print(messung_5.head())