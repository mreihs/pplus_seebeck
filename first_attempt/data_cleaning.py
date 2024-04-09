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
        if i < 10 and number_of_files >= 9:
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


def do_all(fileName, number_of_files):
    messung = read_all_files('data_raw/' + fileName, fileName + '_', number_of_files)
    messung = fix_time(messung)
    messung = pd.concat(messung)
    messung_temperature = read_csv('data_raw/' + fileName + '_temp.csv')
    messung = pd.merge(messung, messung_temperature, how='outer', on='Time')
    # do linear interpolation for the voltage Nan values
    messung['Channel A'] = messung['Channel A'].interpolate()
    messung['Channel B'] = messung['Channel B'].interpolate()
    # convert the Temperature values to float
    messung['Temperature'] = messung['Temperature'].str.replace(',', '.').astype(float)
    messung['Temperature'] = messung['Temperature'].interpolate()
    save_to_csv(messung, 'data_combined/' + fileName + '.csv')

# channel A - type T thermocouple
# channel B - Nickel Copper thermocouple
# heating from -200 to above 0 C
do_all('Messung_1', 16)

# channel A - type T thermocouple
# channel B - Nickel Copper thermocouple
# cooling from 100 to = C
# thermocouple fell out of the metal block
do_all('Messung_2', 8)

# channel A - type T thermocouple
# channel B - Nickel Copper thermocouple
# cooling from 100 to = C
do_all('Messung_2_Dritter_Versuch', 17)

# channel A - Copper Graphene thermocouple
#picometer junction temp: about 17-19°C
do_all('KupferGraphen', 9)

# channel A - Copper Graphite thermocouple
do_all('Messung_4', 9)

# channel A - Graphene Graphite thermocouple
do_all('Messung_5', 9)