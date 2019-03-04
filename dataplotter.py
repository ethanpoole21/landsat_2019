'''
Created on Feb 24, 2019

@author: ethanpoole
'''
# Ethan Poole
import matplotlib.pyplot as plt
import csv
import numpy as np

segment = []
all_segments = []
num = 0;


# import and read the csv file, splitting it up when it hits a break
with open('LOG00009.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    
    for row in csv_reader:
        if row[0] == 'break':
            
            if num == 0:
                all_segments.append(np.array(segment))
            else:
                all_segments.append(np.array(segment))
            num = num +1
            segment = []        
        else:
            segment.append([int(row[0]), float(row[1]), float(row[2])])

all_segments = np.array(all_segments)
print all_segments
# create plots for each of the figures
fig = plt.figure(1)
plot_increment = 1
list_a = []
list_b = []
for segs in all_segments:
    for plots in range(1,3):
        
        if plots == 1:      
            fig.add_subplot(2,num,plot_increment)
            plt.title("Time Vs. Channel A")
            plt.plot(segs[:,0], segs[:,plots], color='black', linewidth=1,
                label="Channel A_%i" %plot_increment)
            plt.xlabel('Time')
            plt.ylabel('Channel Value')
            plt.legend(loc='upper left')
            list_a.append(np.mean(segs[:,1]))
        elif plots == 2: 
            fig.add_subplot(2,num,plot_increment+num)
            plt.title("Time Vs. Channel B")
            plt.plot(segs[:,0], segs[:,plots], color='red', linewidth=1,
                label="Channel B_%i" %plot_increment)
            plt.xlabel('Time')
            plt.ylabel('Channel Value')
            plt.legend(loc='upper left')
            list_b.append(np.mean(segs[:,2]))
    plot_increment = plot_increment + 1

# create plots of average values
x_values = range(1,plot_increment)
print list_a
plt.figure()
plt.plot(x_values, list_a,'o-', color='green', linewidth=1,
         label="Chanel A average")
plt.title("Average chanel A")
plt.xlabel('Incrament')
plt.ylabel('Channel Average')
plt.legend(loc='upper left')
print list_b
plt.figure
plt.plot(x_values, list_b,'o-', color='black', linewidth=1,
         label="Chanel B average")
plt.title("Average chanel b")
plt.xlabel('Incrament')
plt.ylabel('Channel Average')
plt.legend(loc='best')
print plot_increment
plt.show()