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

#Filter set of moves based on dates
date_start = '01/09/2018'
date_end = '30/09/2018'
som_filtered = som.filter_by_date(date_start,date_end)

#Filter set of moves based on category
category = 'rebuts'
som_cat_filtered = som_filtered.filter_by_cat(category)
total = 0
for move in som_cat_filtered.moves:
    print(move)
    total+=move.amount
#Print histogram
som.plot_histogram()
