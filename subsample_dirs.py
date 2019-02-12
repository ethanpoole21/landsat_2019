'''
Created on Jan 28, 2019

@author: ethanpoole
'''

import matplotlib.pyplot as plt
import numpy as np
import csv


#create function to split data based off the nth term 

def split_data(yd,nth):
    x_data = list()
    y_data = list()
    for i in range(0,len(yd)):
        if (i % nth) == 0:
            y_data.append(yd[i])
            x_data.append(i) 
    return np.asarray(x_data),np.asarray(y_data)



# import data from csv data and insert into appendix 
x_data = []
y_data = []

with open('scatter.csv', 'r')as a:
    b = csv.reader(a, delimiter=',')
    for rows in b:
        x_data.append(float(rows[0]))
        y_data.append(float(rows[1]))
        
# plot original points
plt.figure()
plt.scatter(x_data, y_data, color='blue', s=20, marker='o', label="Dataset points")


z = np.polyfit(x_data, y_data, 1)
func = np.poly1d(z)
preds = func(x_data)


plt.plot(x_data, preds, color='orange', linewidth=2, label="Dataset line")
plt.legend(loc='upper left')

# parse the data

x_data, y_data = split_data(x_data,3)
plt.figure()
plt.scatter(x_data, y_data, color='red', s=20, marker='o', label="Splitted points")

z = np.polyfit(x_data, y_data, 1)
func = np.poly1d(z)
preds = func(x_data)

# plot the parsed data on a second graph

plt.plot(x_data, preds, color='green', linewidth=2, label="splitted line")

plt.legend(loc='upper left')
plt.savefig('./subsample')
plt.show()

# calculate r-squared

def rsquare(x, y, degree):
        results = {}
        coeffs = np.polyfit(x, y, 1)
        results['polynomial'] = coeffs.tolist()
        p = np.poly1d(coeffs)
        print p
q = 1

rsquare(x_data, y_data, q)
