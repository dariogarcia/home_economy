import sys
from movement import Movement

if len(sys.argv)!=2:
    raise Exception("One parameter needed: File to read")

file_name = sys.argv[1]

#Read file, line by line
read_movements = []
with open(file_name,'r') as f:
    for l in f:
        fields = l.split('\t')
        #date, _, description, _, _, amount, _ = fields
        m = Movement(fields[0], fields[2], fields[5])
        read_movements.append(m)

for m in read_movements:
    m.assign_category()
