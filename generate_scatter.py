'''
Created on Feb 1, 2019

@author: ethanpoole
'''
import numpy as np
import random
import csv



def generate_scatter():
    x_data = range(0,100)
    y_data = list()
    for i in range(0,100):
        b =random.randint(1,10)
        y_data.append(b+i)  
    return np.asarray(y_data),x_data

y_data,x_data = generate_scatter()

with open('scatter.csv', 'w')as a:
    scatter  = csv.writer(a)
    c,d = generate_scatter()
    scatter_Data = ""
    for count,i in enumerate(c):
        scatter.writerow([c[count],d[count]])
        
   
    
