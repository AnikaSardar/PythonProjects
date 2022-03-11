# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:16:15 2021

@author: anika
"""
# =============================================================================
# list=[]
# x=1
# while x<=9: 
#     list.append(x)
#     x=x+1 
# 
# 
# f=open ("Nasdaq.txt", "r")
# datastr=f.read()
# data=datastr.split() 
# 
# 
# c_1=c_2=c_3=c_4=c_5=c_6=c_7=c_8=c_9=0
# 
# 
# 
# for i in range(len(data)): 
#     firstdigit=data[i][0] 
#     if firstdigit=="1":
#         c_1+=1
#     elif firstdigit=="2":
#         c_2+=1
#     elif firstdigit=="3":
#         c_3+=1
#     elif firstdigit=="4":
#         c_4+=1
#     elif firstdigit=="5":
#         c_5+=1
#     elif firstdigit=="6":
#         c_6+=1
#     elif firstdigit=="7":
#         c_7+=1
#     elif firstdigit=="8":
#         c_8+=1
#     elif firstdigit=="9":
#         c_9+=1
#         
#     else:
#         print("Not counting value: " + str(firstdigit))
# 
# count_list = [c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9]
# 
# total = 0
# 
# for i in range(len(count_list)):
#     total += count_list[i] #total comes 999 because there is a value of 0.82 at Nasdaq.txt 
#     print("For " + str(list[i]) + ": " + str(count_list[i]))
# 
# print("Total: "+ str(total))
# 
# f.close()
# 
# 
# 'Step 5 ==> Write data to a file called "bennyout.txt"'
# 
# f=open("bennyout.txt", "a")
# for i in range(len(count_list)):
#     f.write("For " + str(list[i]) + ": " + str(count_list[i]) + "\n") 
# 
# f.write("Total: " + str(total) +"\n")
# 
# f.close()
#  
# 
# =============================================================================



    
x=1
l_list=[]
while x<10: 
    l_list.append(x)
    x+=1
    
file=open("Nasdaq.txt", "r")
datastr=file.read()
lines=datastr.split()
print("datastr " + str(datastr))
print("lines " + str(lines))
c_1=c_2=c_3=c_4=c_5=c_6=c_7=c_8=c_9=0

for i in range(len(lines)): 
    y=lines[i][0]
    if y=="1": 
        c_1+=1
    elif y=="2": 
        c_2+=1
    elif y=="3": 
        c_3+=1
    elif y=="4": 
        c_4+=1
    elif y=="5": 
        c_5+=1
    elif y=="6": 
        c_6+=1
    elif y=="7": 
        c_7+=1
    elif y=="8": 
        c_8+=1
    elif y=="9": 
        c_9+=1
file.close()
     
counts=[c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9]
print(counts)
total=0
new_file=open("Results.txt", "w")
for i in range(len(counts)):
    total+=counts[i]
    
    s="For " + str(l_list[i])+ ": "+ str(counts[i])
    print(s+'\n')
    new_file.write(s+"\n")
    
new_file.write("total= " + str(total))
new_file.close()

