import sys
from movement import Movement
from set_of_moves import SetOfMoves

#Parse parameters
if len(sys.argv)!=2:
    raise Exception("One parameter needed: File to read")
file_name = sys.argv[1]

#Read file and fill structure
som = SetOfMoves()
with open(file_name,'r') as f:
    for l in f:
        fields = l.split('\t')
        #date, _, description, _, _, amount, _ = fields
        som.append_move(Movement(fields[0], fields[2], fields[5]))

#Assign categories to movements based on categories.py
som.assign_categories()


date_start = '01/01/2019'
date_end = '10/01/2019'
som_filtered = som.filter_by_date(date_start,date_end)

for x in som_filtered.moves:
    print(x)

#print(som)
#som.plot_histogram()
