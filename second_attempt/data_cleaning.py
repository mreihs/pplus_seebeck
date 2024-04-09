# read csv file and clean the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# read csv file
def read_csv(file_path):
    # skip row 0 and 1
    # column names are: Time, V_R, V_T
    data = pd.read_csv(file_path, decimal='.', sep=',', skiprows=2)
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

def fix_time(datasets, single_channel=False):
    # convert the time to the time + the highest time of the previous file
    previous_time = 0
    for i in range(len(datasets)):
        if single_channel:
            datasets[i].columns = ['Time', 'V_T']
        else:
            datasets[i].columns = ['Time', 'V_R', 'V_T']

        datasets[i]['Time'] = datasets[i]['Time'] + previous_time
        previous_time = datasets[i]['Time'].max()
    return datasets


# function that saves the data to a csv file
def save_to_csv(data, file_name):
    data.to_csv(file_name, index=False)


def do_all(fileName, number_of_files, single_channel=False):
    messung = read_all_files('data_raw/' + fileName, fileName + '_', number_of_files)
    messung = fix_time(messung, single_channel)
    messung = pd.concat(messung)
    save_to_csv(messung, 'data_combined/' + fileName + '.csv')


do_all('Kupfer_Konstantan_Full_Range', 51)
print('Kupfer_Konstantan_Full_Range done')

do_all('Kupfer_Nickel_Full_Range', 27)
print('Kupfer_Nickel_Full_Range done')

do_all('PT100_0_Grad', 2, True)
print('PT100_0_Grad done')

do_all('PT100_Kochend', 1, True)
print('PT100_Kochend done')

do_all('PT100_LN', 2, True)
print('PT100_LN done')