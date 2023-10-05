import os
import csv

candidates=[]

election_csv = os.path.join(".", "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvpointer = csv.reader(csvfile, delimiter=",")
    header=next(csvpointer)
    for row in csvpointer:
        candidates.append(row[2])

candidates_set=[]        
               
for candidate in candidates:
     if candidate not in candidates_set:
         candidates_set.append(candidate)

total_indv=[]

for candidate in candidates_set:
    vote=candidates.count(candidate)
    total_indv.append(vote)

total_gral = sum(total_indv)

percentages=[]

for ti in total_indv:
     percent=ti/total_gral
     percentages.append('{:.3%}'.format(percent))


results={'Candidate':candidates_set,'Percentage':percentages ,'Total':total_indv}

winner_index = results["Percentage"].index(max(results["Percentage"]))
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

for x in range(0 , len(total_indv)):
    print(f'{results["Candidate"][x]}: {results["Percentage"][x]} ({results["Total"][x]})')

lines2=[ 
    '-'*50,
    f'Winner: {winner}',
    '-'*50,
    ''
]  

for line in lines2:
    print(line)

outputpath= os.path.join('.','analysis','Election_Results.txt')

with open(outputpath,'w',encoding='utf-8') as f:
    for line in lines1:
        f.write(line)
        f.write('\n') 
    for x in range(0 , len(total_indv)):
        f.write(f'{results["Candidate"][x]}: {results["Percentage"][x]} ({results["Total"][x]})')
        f.write('\n')
    for line in lines2:
        f.write(line)
        f.write('\n')


