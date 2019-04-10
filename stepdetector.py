'''
Created on Apr 1, 2019

@author: ethanpoole
'''
import matplotlib.pyplot as plt
import csv
import numpy as np


channel_a = []
channel_b = []
thermoster = []

with open('3_16_19_60C_sweep.TXT') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        channel_a.append(row[0])
        channel_b.append(row[1])
        thermoster.append(row[2])
        
#convert and segment loops to add breaks at jumps


this_value = 0
last_value = 0
yvalues =[]
xvalues =[]
value = []

value = ([channel_a,channel_b,thermoster])
for x in channel_a:
    this_value = int(x)
    if abs(this_value-last_value) >= 10:
        last_value = int(x)
        value[0].append(10)
        value[1].append(10)
    else:
        last_value = int(x)
    
#print (value)


a_yvalues = np.array(value[0])
b_yvalues = np.array(value[1])
xvalues = np.array(range(a_yvalues.size))

print a_yvalues.shape
print b_yvalues.shape
print xvalues.shape



a = np.array(a_yvalues)
b = np.array(xvalues)
c = np.array(b_yvalues)
# plotting stuff

plt.plot(b,a)  
plt.plot(b,a)  
plt.show()

