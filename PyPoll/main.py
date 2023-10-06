import os
import csv

candidates=[]

election_csv = os.path.join(".", "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvpointer = csv.reader(csvfile, delimiter=",")
    header=next(csvpointer)
    for row in csvpointer:
        candidates.append(row[2]) #this list wil have the name of a candidate 'n' number of times the candidate was voted

#Define a list in which to store the 'universe' of candidates (one time per candidate)
candidates_set=[]        

#to do this, the code will iterate in the list 'candidates' which contains an item with the name of the candidate per vote recived, 
#and store it if it was not previously stored, therefore storing each different candidate once
for candidate in candidates:
     if candidate not in candidates_set:
         candidates_set.append(candidate)

#now that it has the 'universe' of candidates, the code will determine the individual number of votes per candidate getting advantage of the 'count' method
#and it will store each value to a new list
total_indv=[]

for candidate in candidates_set:
    vote=candidates.count(candidate)
    total_indv.append(vote)

#the total votes count will be the sum of each of the individuals total
total_gral = sum(total_indv)

#to calculte the percentage of votes recived for each candidate, the code will iterate in the list with the total for each individual
#and will store each result in a new list
percentages=[]

for ti in total_indv:
     percent=ti/total_gral
     percentages.append('{:.3%}'.format(percent))

#the index of the three created lists should match
#the code will create a dictionary with the results from the previous steps
results={'Candidate':candidates_set,'Percentage':percentages ,'Total':total_indv}

#to determine the winner the code will use the 'max' function over the list 'Total' contained in the dictionary 'results' to get the index of this value
#then with that index the code will read the name of the winner in the 'Candidate' list
#we should not apply the 'max' function to the 'Percentage' list because the data type is string because we applied the format when appending the list
winner_index = results["Total"].index(max(results["Total"]))
winner=results["Candidate"][winner_index]

lines1=[
    '',
    'Election Results',
    '-'*50,
    f'Total Votes: {total_gral}',
    '-'*50
]

for line in lines1:
    print(line)
#this will print the results no matter the number of candidates in our 'universe'
for x in range(0 , len(candidates_set)):
    print(f'{results["Candidate"][x]}: {results["Percentage"][x]} ({results["Total"][x]})')

lines2=[ 
    '-'*50,
    f'Winner: {winner}',
    '-'*50,
    ''
]  

for line in lines2:
    print(line)

#Finally export the results to a txt file
outputpath= os.path.join('.','analysis','Election_Results.txt')

with open(outputpath,'w',encoding='utf-8') as f:
    for line in lines1:
        f.write(line)
        f.write('\n') 
    for x in range(0 , len(candidates_set)):
        f.write(f'{results["Candidate"][x]}: {results["Percentage"][x]} ({results["Total"][x]})')
        f.write('\n')
    for line in lines2:
        f.write(line)
        f.write('\n')


