import csv as csv
import numpy as np
import matplotlib.pyplot as plt


print '----DATA INCOMING---'

f= open('timeofacc.csv','r')
f_obj = csv.reader(f)
header = f_obj.next()
data = []

#downloading data from file
for row in f_obj:
    data.append(row)

#arranging the accidents count in ascending order
for i in range(0,len(data)-1):
    minval = int(data[i][9])
    idx = i
    for j in range(i,len(data)-1):
        if minval>int(data[j][9]):
            minval = int(data[j][9])
            idx = j
    temp = data[i]
    data[i] = data[idx]
    data[idx] = temp

#getting the top 10 states with max accidents
temp1 = data[len(data)-11:len(data)-1]


#removing the final column and the final row from data
t = []
for i in range(len(temp1)):
    t.append(temp1[i][:len(temp1[i])-1])

#differnt types of lines
d = ['-r',':r',':c','-c',':b','-b','-k',':g',':k','-g']

#initializing
fig = plt.figure()
ax = plt.axes()

#24 hours split in 3 hour windows
x = np.linspace(0,24,8)

#plotting data
for i in range(len(t)):
    plt.plot(x,t[i][1:],d[i],label=t[i][0])

#data information
plt.ylabel('Accidents Count',fontsize=18)
plt.title("No. of Accidents according to the time of day(2014)",fontsize=20)
plt.xlabel('Time of Day',fontsize = 18)

plt.legend(loc="best")
plt.show()

