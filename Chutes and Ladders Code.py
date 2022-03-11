# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:30:49 2021

@author: anika
"""



import random 


def single_game_over100(current_p, hit_ladder, ladder, up, chutes, down): 
    count = 0
    while current_p<100: #wins on sq 100 or over it
        count+=1
        dice=random.randint(1,6)
        current_p+=dice
        #print("current"+str(current_p))
        
        for i in range(len(ladder)):
            if current_p==ladder[i]:
                hit_ladder=True
                current_p=up[i]
                #print(current_p)
                
        if hit_ladder==False:
            for i in range(len(chutes)):
                if current_p==chutes[i]:
                    current_p=down[i]
                    #print(current_p)
        hit_ladder=False #reset
    #print ("You won the game!")
    return count


def single_game_100(temp, current_p, hit_ladder, ladder, up, chutes, down): 
    count = 0
    while  current_p<100: #wins when landed exactly on sq 100 
        count+=1
        dice=random.randint(1,6)
        temp = current_p + dice
        #print("Temp value is: " + str(temp))
        if temp<=100:
            current_p=temp
                
            for i in range(len(ladder)):
                if current_p==ladder[i]:
                    hit_ladder=True
                    current_p=up[i]
                    #print(current_p)
            if hit_ladder==False:
                for i in range(len(chutes)):
                    if current_p==chutes[i]:
                        current_p=down[i]
                        #print(current_p)
                            
            #print("current: "+str(current_p))                
            hit_ladder=False #reset
    #print ("You won the game!")   
    return count 


# main program
from statistics import mean
ladder=[1,4,9,21,28,36,51,71,80]
up=[38,14,31,42,84,44,67,91,100]
chutes=[16,47,49,56,62,64,87,93,95,98]
down=[6,26,11,53,19,60,24,73,75,78]

temp=0
current_p=0
hit_ladder=False 

trial = 1000000
run=1

list1=[]
list2=[]
while run<=trial:
    list1.append(single_game_100(temp, current_p, hit_ladder, ladder, up, chutes, down))
    list2.append(single_game_over100(current_p, hit_ladder, ladder, up, chutes, down))

    run +=1
print("Trial: " + str(trial))
print("Average no. of spins for landing exactly on 100 for 1,000,000 trials: " + str(mean(list1)))
print("Average no. of spins for landing on or over 100 for 1,000,000 trials: " + str(mean(list2)))

print("****For the Curious Mind****")
print("Max number of spins for landing exactly on 100: " + str(max(list1)))
print("Min number of spins for landing exactly on 100: " + str(min(list1)))
print("Max number of spins for landing on or over 100: " + str(max(list2)))
print("Min number of spins for landing on or over 100: " + str(min(list2)))




print("-----Ending Scenario#1: Landing exactly on square 100-------")
count_once1=set(list1) #counts the values in list1 only once
#print(count_once1)
c=0
c_list1=[]

maximum = 0
maximum_key = 0


for most_prob_spin in count_once1: 
    s="For " + str(most_prob_spin) + " : "
    c= list1.count(most_prob_spin)
    
    # check if this is max
    if maximum < c:
        maximum = c
        maximum_key = most_prob_spin
        
        
    c_list1.append(c)
    print(s+str(c))
    

print("*****************************")
print("Maximum number value: " + str(maximum))
print("Maximum key value: " + str(maximum_key))
print("***********************")

# =============================================================================
# x=max(c_list1)
# 
# print("X value: " + str(x))
# =============================================================================


print("-----Ending Scenario#2: Landing on square 100 or over-------")
count_once2=set(list2) #same thing for list2
c=0
c_list2=[]


for most_prob_spin in count_once2: 
    s="For " + str(most_prob_spin) + " : "
    c= list2.count(most_prob_spin)
    
    # check if this is max
    if maximum < c:
        maximum = c
        maximum_key = most_prob_spin
        
        
    c_list2.append(c)
    print(s+str(c))
    

print("*****************************")
print("Maximum number value: " + str(maximum))
print("Maximum key value: " + str(maximum_key))
print("*****************************")

# =============================================================================
# x=max(c_list2)
# 
# print("X value: " + str(x))
# =============================================================================

"Std dev"
print("-----Standard Deviation------")
import statistics
num_of_spins_for_100=list1
num_of_spins_for_over100=list2

#Std dec of list1 
res1=statistics.pstdev(num_of_spins_for_100)
res2=statistics.pstdev(num_of_spins_for_over100)

print("Standard deviation for Ending Scenario#1: " + str(res1))
print("Standard deviation for Ending Scenario#2: " + str(res2))
