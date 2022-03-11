# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:13:41 2021

@author: anika
"""
# =============================================================================
# import random
# 
# outcome=[2,3,4,5,6,7,8,9,10,11,12]
# roll=1
# #acc=0 
# holding=[]
# roll_total = 3600000
# 
# while roll<=roll_total:
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     x=dice1+dice2
#  #   acc +=1
#     holding.append(x)
#     roll += 1
# print(holding)
#     
# #print(acc)
# 
# 
# print("****************Printing counts ***************")
# for possible_outcome in outcome:
#     s = "For " + str(possible_outcome) + " : "
#     count = holding.count(possible_outcome)
#     count_p = (count / roll_total) * 100
#     print(s + str(count))
#     print("Probability= "+ str(count_p)+"%")
# =============================================================================
# =============================================================================
# 
# c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0 
# 
# x=[2,3,4,5,6,7,8,9,10,11,12]
# each_count=[]
# roll_dice=1
# import random 
# 
# while roll_dice<=3600: 
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     summation=dice1+dice2
#     if summation==2: 
#         c2+=1
#         each_count.append(c2)
#     elif summation==3:
#         c3+=1
#         each_count.append(c3)
#     elif summation==4:
#         c4+=1
#         each_count.append(c4)
#     elif summation==5:
#         c5+=1
#         each_count.append(c5)
#     elif summation==6:
#         c6+=1
#         each_count.append(c6)
#     elif summation==7:
#         c7+=1
#         each_count.append(c7)
#     elif summation==8:
#         c8+=1
#         each_count.append(c8)
#     elif summation==9:
#         c9+=1
#         each_count.append(c9)
#     elif summation==10:
#         c10+=1
#         each_count.append(c10)
#     elif summation==11:
#         c11+=1
#         each_count.append(c11)
#     elif summation==12:
#         c12+=1
#         each_count.append(c12)
#     roll_dice+=1
#     
# print(each_count)
# print(c6)
# list=[c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
# print("list " + str(list))
# total=0
# for i in range(len(list)): 
#     nume=list[i]
#     total+=list[i]
#     avg=nume/total
#     print(avg)
# print("total " + str(total))
# 
# 
# 
# for i in range(len(list)): 
#     s="For " + str(x[i]) + ":" + str(list[i])
#     print (s)
# 
# =============================================================================


# =============================================================================
# def avg_func(x): 
#     total=0
#     for i in range(len(x)): 
#         total+=x[i]
#     average=total/len(x)
#     return total 
# =============================================================================

def first_even(list): 
    for i in range(len(list)):
        if list[i]%2==0: 
            even=list[i]
            print(even)
     
            

list=[2,3,4,56,3]
print(first_even(list))

def avg(list): 
    total=0
    for i in range(len(list)):
        total+=list[i]
    length=len(list)
    average=total/length
    return average 
    
print( "average" + str(avg(list)))
list=[2,3,4,56,3]