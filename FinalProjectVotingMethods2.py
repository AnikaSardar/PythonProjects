# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:45:20 2021

@author: anika
"""
"""
Voting Method
Borda Count Method
"""

votes=[[1,2,3,4], # votes[voter#][candidate#]=ranking
       [2,1,4,3],
       [4,1,2,3],
       [3,4,1,2],
       [1,2,4,3]]  


print("********************** Voting Method (Borda Count) ***********************\n")
points_for_cand = []

for columns in range(len((votes[0]))): 
    total = 0
    for rows in range(len(votes)):
        rank=votes[rows][columns]
        total += 5-rank
    points_for_cand.append(total)
print("Borda Count Points: "+str(points_for_cand))

for win in range(len(points_for_cand)):
    highest_pt=max(points_for_cand)
    candidate=points_for_cand.index(highest_pt)+1
print("Highest Point: " +str(highest_pt)) 
print("Winner of the Borda Count is Candidate " + str(candidate))   
    

"""
Make It Interesting
Rank Choice Voting     
"""
print("\n******************* Voting Method (Rank Choice Voting) ******************\n")
def get_first_place_votes(votes):
    first_place_votes=[]
    for columns in range(len((votes[0]))): 
        count=0
        for rows in range(len(votes)):
            if votes[rows][columns]==1:
                count+=1
            elif votes[rows][columns]==100:
                count=100
                break 
        first_place_votes.append(count)
    print("First Place votes: " +str(first_place_votes))
    return first_place_votes


def get_max(fp_votes):
    max_val = fp_votes[0]
    for i in range(len(fp_votes)):
        if fp_votes[i] > max_val and fp_votes[i] != 100:
            max_val = fp_votes[i]
    return max_val



# =============================================================================
# votes=[[1,2,3,4], # votes[voter#][candidate#]=ranking
#        [2,1,4,3],
#        [1,4,2,3],
#        [3,4,1,2],
#        [2,1,4,3]] 
# =============================================================================

half_no_votes = len(votes)/2
max_votes_received = 0

while max_votes_received <= half_no_votes:
    first_place_votes = get_first_place_votes(votes)
    lowest=min(first_place_votes)
    eliminatecand=first_place_votes.index(lowest)
    for rows in range(len((votes))): 
        for columns in range(len(votes[0])):
            if votes[rows][columns]!=100 and votes[rows][columns]>votes[rows][eliminatecand]:
                votes[rows][columns]=votes[rows][columns]-1
                #votes[rows][eliminatecand] = 100  #eliminated
        votes[rows][eliminatecand] = 100
    print(votes)
    max_votes_received = get_max(first_place_votes)
    print("max" +str(max_votes_received))
print("Final Votes: " + str(votes))
max_plurality=get_max(first_place_votes)
winner=first_place_votes.index(max_plurality)+1
print("\n Winner of Rank Choice Voting is Candidate " + str(winner) )

