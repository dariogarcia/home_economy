
class SetOfMoves:

    def __init__(self):
        self.moves = []

    def append_move(self,m):
        self.moves.append(m)

    def assign_categories(self):
        for m in self.moves:
            m.assign_category()
