# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:17:14 2021

@author: anika
"""

'Making a list'
y=[]
Win = []

x=1
total_num=20 #you can also view it as the last digit of the list if starting with 1

while x<=total_num:
    y.append(x)
    Win.append(x) #because if I do Win=y, then if y changes inside the loop, so would Win
                 #for example, the user moves the pieces to left, so now "1" would be the last item in list
                 #and "2" first item. Now, if Win=y, then Win=[2,3...1]
                # hence, to avoid that, we are appending x to Win so that Win=[1,2...20]
    x=x+1
print("Original list:", y)



'Controls for the user'
Move_R=1
Move_L=2
Spin=3
Exit=4

user=1 #user can be any number other than 4 to begin the loop 


while user != Exit: 
    print("What is your move? \n Enter one of the following-\n 1 for moving pieces to right\n 2 for moving pieces to left\n 3 for spinning the pieces\n 4 for exiting the game")
    user=int(input("Answer: "))
    if user==Move_R:
        y.insert(0, y.pop())
        print("After the move, the new list=", y) 
    elif user==Move_L:
# =============================================================================
#         y.append(y[0]) #Professor showed this way to solve it
#         del y[0]
#         print(y)
# =============================================================================
        store=y[1:] 
        store.append(y[0])
        y=store
        print("After the move, the new list=", y)
    elif user==Spin:
        store = y[8:12]
        store.reverse()
        y[8:12] = store #assigning index from 8 to 11 (as 12 doesn't count) back to the y-list
        print("After the move, the new list=", y)
print("Game Ended!")

        


