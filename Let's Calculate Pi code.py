# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 01:24:52 2021

@author: anika
"""

'''
1. 1000 terms need to be added to get pi accurate to 3.14 
2. 1,000,000 terms need to be added to get pi accurate to 3.14159
3. The result depends if one starts with n=1 to n=Nmax vs
the other way round, because python can store only a set number of numbers
and then delete the other half, and then keep on adding to the saved digits
4. When keep increasing the terms from 10,000 to 100,000,000 the pi comes closer
to the accurate pi digits'''

# =============================================================================
# n=0
# acc=0
# 
# while n<=10000000:
#     x= (-1)**n
#     y= (2*n)+1
#     z= (x/y)*4
#     acc=acc+z
#     n=n+1
#     print(acc)   
# 
# =============================================================================

n=100
acc=0

while n>=0:
    x= (-1)**n
    y= (2*n)+1
    z= (x/y)*4
    acc=acc+z
    n=n-1
    print(acc)   

