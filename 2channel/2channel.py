# -*- coding: utf-8 -*-
import numpy as np 
from matplotlib import pyplot as plt
import os
from scipy.optimize import curve_fit
from Chips import y620, y475

# get current directory
path = os.getcwd()





txt = os.path.abspath(os.path.join(path, os.pardir)) + '\\2channel\\Blue_Amber\\2 channel test-single-20211213-151240.txt'



with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("datablue.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("datablue.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("datablue.txt", "w")
for element in f_contents2:
    data2.write(element)
data2.close()

x = f_contents2.split("{")

y1 = []
y2 = []

for i in range(len(x)):
    y3 = x[i].partition(":")
    y1.append(y3[0].strip('""'))
    y2.append(y3[2].strip("},"))
    



y1 = y1[slice(400)]
y2 = y2[slice(400)]
#print(y1)
#target_ibdex
yy = np.array(y1)
yy2 = np.array(y2)

yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)
yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)

xblue = yy.astype(float)
yblue = yy2.astype(float)


plt.plot(xblue, yblue)
plt.plot(xblue, y475)
plt.plot(xblue, 0.8*y620)
plt.grid()
plt.axvline(475, color = 'red', linestyle = '--', label = '425nm')
plt.xlabel('Wavelenght(nm)')
plt.ylabel('Relative Intensity')

plt.axvline(620, color = 'green', linestyle = '--', label = '620nm')
plt.legend()
#------------------------------------------------

#Import two channels of that we are investigating 



