# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:27:09 2021

@author: anika
"""

# =============================================================================
# a=[]
# b=[]
# 
# xv=[0,1,.5]
# yv=[0,0,.860]
# x=.5
# y=.5
# 
# import random
# for i in range(9000): 
#     i=random.randint(0,2)
#     xmid=(xv[i]+x)/2
#     ymid=(yv[i]+y)/2
#     x=xmid
#     y=ymid
#     a.append(x)
#     b.append(y) 
# # =============================================================================
# #     print(i)
# # =============================================================================
# print("xmid", a)
# print("ymid", b)
#     
# 
# from matplotlib import pyplot as plt 
# plt.scatter(a,b, color="orange", marker="o", s=20)
# plt.title("Sierpinski Gasket")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.axis([0,.4,0,.5])
# plt.show()
# =============================================================================

# =============================================================================
# a=[]
# b=[]
# 
# xv=[0,0,0, .5, .5, 1,1,1]
# yv=[0,2,1,0,2,0,2,1]
# x=.5
# y=.5
# 
# import random
# for i in range(9000): 
#     i=random.randint(0,7)
#     xmid=(xv[i]+x)/3
#     ymid=(yv[i]+y)/3
#     x=xmid
#     y=ymid
#     a.append(x)
#     b.append(y) 
# # =============================================================================
# #     print(i)
# # =============================================================================
# print("xmid", a)
# print("ymid", b)
#     
# 
# from matplotlib import pyplot as plt 
# plt.scatter(a,b, color="red", marker="o", s=20)
# plt.title("Sierpinski Gasket")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# # =============================================================================
# # plt.axis([0,.4,0,.5])
# # =============================================================================
# plt.show()
# =============================================================================

a=[]
b=[]

xv=[0, 0, 1, 1 , -0.5, 1.5 ]
yv=[0, 1 , 0, 1, 0.5, 0.5]
x=.5
y=.5

import random
for i in range(9000): 
    i=random.randint(0,5)
    xmid=(xv[i]+x)/3
    ymid=(yv[i]+y)/3
    x=xmid
    y=ymid
    a.append(x)
    b.append(y) 
# =============================================================================
#     print(i)
# =============================================================================
print("xmid", a)
print("ymid", b)
    

from matplotlib import pyplot as plt 
plt.scatter(a,b, color="green", marker="o", s=20)
plt.title("Sierpinski Gasket")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis([0,.4,0,.5])
plt.show()

