# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 08:40:22 2021

@author: ankit
"""

import pandas as pd
from zipfile import ZipFile
import glob
import zipfile
import os


my_path="C:/Users/ankit/Downloads/my_task/Que1"


number_of_file=0 
for file in glob.glob(my_path + "/*.zip"):
    print(file)
    number_of_file += 1
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(my_path)
        
print("all the files has been unzipped")
#extension = 'csv'
#all_filenames = [i for i in glob.glob("60d_DAM_PTPObligationBidAwards*.csv")]
filelist = [file for file in os.listdir(my_path) if file.startswith('abc')]
print(filelist)
combined_csv = pd.concat([pd.read_csv(my_path+'/'+f) for f in filelist])

#export to csv
combined_csv.to_csv(my_path+'/combined_csv.csv', index=False, encoding='utf-8-sig')
print("all required csv has been combined")

