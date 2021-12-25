import numpy as np 
from matplotlib import pyplot as plt
import os
from scipy.optimize import curve_fit


# get current directory
path = os.getcwd()

 

#Get info for 405nm LED chip

txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\405nm\\405.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x405 = yy.astype(float)
y405 = yy2.astype(float)

# 451 nm 


txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\451nm\\451.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
    
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x451 = yy.astype(float)
y451 = yy2.astype(float)

##############475nm
txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\475nm\\475.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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


x475 = yy.astype(float)
y475 = yy2.astype(float)

#################500nm


txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\500nm\\500.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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
    

#print(y1)   
#print(y2)


#y2 = y2.strip("},")
#print(y1)
#print(y1)
#print(y2)




y1 = y1[slice(400)]
y2 = y2[slice(400)]

#target_ibdex
yy = np.array(y1)
yy2 = np.array(y2)

yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)
yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)

x500 = yy.astype(float)
y500 = yy2.astype(float)



########526nm


txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\526nm\\526.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
    
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

#target_ibdex
yy = np.array(y1)
yy2 = np.array(y2)

yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)
yy = np.delete(yy,0)
yy2 = np.delete(yy2, 0)

x526 = yy.astype(float)
y526 = yy2.astype(float)


#####548 nm


txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\548nm\\548.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
    
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x548 = yy.astype(float)
y548 = yy2.astype(float)


##############597nm#####################

txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\597nm\\597.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x597 = yy.astype(float)
y597 = yy2.astype(float)


########620nm##########
txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\620nm\\620.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
    
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x620 = yy.astype(float)
y620 = yy2.astype(float)


############630nm###############


txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\630nm\\630.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
   
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    #print(f_contents2)
    
data2 = open("data500.txt", "w")
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

x630 = yy.astype(float)
y630 = yy2.astype(float)
################665nm



txt = os.path.abspath(os.path.join(path, os.pardir)) + '\LED_chips\\665nm\\665.txt'

with open(txt, 'r') as f:
    
    size_to_read = 10
    f.seek(595)
    f_contents1 = f.readlines()
    
    
    
data = open("data500.txt", "w")
for element in f_contents1:
    data.write(element + "\n")
data.close()



with open("data500.txt", 'r') as ff:
    size_to_read = 8084
    f_contents2 = ff.read(size_to_read)
    
    
data2 = open("data500.txt", "w")
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

x665 = yy.astype(float)
y665 = yy2.astype(float)
