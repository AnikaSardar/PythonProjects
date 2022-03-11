# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:09:29 2021

@author: anika
"""
'Ex-1'
# =============================================================================
# from matplotlib import pyplot as plt 
# x=[1,1,1,2,2,2]
# y=[0,2,1,1,2,0]
# s=[3,3]
# t=[0,2]
# plt.plot(x,y, color="purple", linewidth= 10)
# plt.plot(s,t, color='gold', linewidth= 10)
# plt.xlabel("horizontal")
# plt.ylabel("Vertical")
# plt.legend(['H', 'I'], loc='upper left')
# plt.show()
# =============================================================================


'Ex 2'
from math import sin
p=3.14159
x=0
s=[]
t=[]
while 0<=x<=5:
    y=sin(x/(2*p))*10
# =============================================================================
#     print("(",x,",",y,")")
#     x=x+0.05
# =============================================================================
    s.append(x)
    t.append(y)
    x=x+0.05
print(s) # Prints all the x-values in a list
print(t) # Prints all the y-values in a list

from matplotlib import pyplot as plt
x=s
y=t 
plt.xlabel("Position (meters)")
plt.ylabel("Height (m)")
plt.title("Wave Height vs. Position")
plt.plot(x,y)
plt.show()

    
    
    

