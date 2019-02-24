from datetime import datetime

class SetOfMoves:

    def __init__(self):
        self.moves = []

    def append_move(self,m):
        self.moves.append(m)

    def assign_categories(self):
        for m in self.moves:
            m.assign_category()

    def filter_by_date(self,date_init,date_end):
        som_filtered = SetOfMoves()
        for move in self.moves:
            #TODO process data
            mdate = datetime.strptime(move.date, '%d/%m/%Y')
            idate = datetime.strptime(date_init, '%d/%m/%Y')
            edate = datetime.strptime(date_end, '%d/%m/%Y')
            #If date is in range, append
            if mdate >= idate and mdate <= edate:
                som_filtered.append_move(move)
        return som_filtered
