
import os

import csv

csvfile = r'PyPoll\Resources\election_data.csv'

Nvotes = 0
candidatename = []
candidatenumber = 0
votes = 0
votescounter = []
MaxVotes = 0
percentagevotes = []

with open(csvfile, 'r') as poll:
     
     csvreader = csv.reader(poll, delimiter=',')
     header = next(csvreader)

     for row in csvreader:
          
          Nvotes = Nvotes + 1
          
          
          if row[2] not in candidatename:
               
               if votes > 1:
                    
                    votescounter.append(votes)

               candidatename.append(row[2])
               votes = 1

          else:
               
               votes = votes + 1

     votescounter.append(votes)
     
     for Cvotes in votescounter:

          if Cvotes > MaxVotes:
               
               MaxVotes=Cvotes

          percentagevotes.append(Cvotes/Nvotes)

winner = candidatename[votescounter.index(MaxVotes)]

print('Election Results')
print('-------------------------')
print(f'Total Votes:  {Nvotes}')
print('-------------------------')

for candidate in candidatename:

     print(f'{candidate}: {percentagevotes[candidatename.index(candidate)]: .2%} ( {votescounter[candidatename.index(candidate)]} )')

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

Poll_results = r'PyPoll\Analysis\Poll_results.txt'

with open(Poll_results, 'w') as txtfile:

     txtfile.write('Election Results')
     txtfile.write('\n')
     
     txtfile.write('-------------------------')
     txtfile.write('\n')
     
     txtfile.write(f'Total Votes:  {Nvotes}')
     txtfile.write('\n')
     
     txtfile.write('-------------------------')
     txtfile.write('\n')

     for candidate in candidatename:
          
          txtfile.write(f'{candidate}: {percentagevotes[candidatename.index(candidate)]: .2%} ( {votescounter[candidatename.index(candidate)]} )')
          txtfile.write('\n')
     
     
     txtfile.write('-------------------------')
     txtfile.write('\n')
     
     txtfile.write(f'Winner: {winner}')
     txtfile.write('\n')
     
     txtfile.write('-------------------------')
     txtfile.write('\n')