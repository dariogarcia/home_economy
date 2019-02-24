import matplotlib.pyplot as plt
import numpy as np

from categories import categories

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
            #If date is in range, append
            if move.date >= date_init and move.date <= date_end:
                som_filtered.append_move(move)
        return som_filtered

    def total_by_cat_and_month(self):
        months = set()
        for m in self.moves:
            months.add((m.date.month,m.date.year))
        total_months = len(months)
        total_cats = len(categories)
        np_data = np.array((total_months,total_cats))
        #TODO
        fill the matrix!

        return np_data

    def plot_histogram(self):

        data_by_month = self.total_by_cat_and_month()
        # multiple line plot
        plt.plot( 'x', 'y1', data=data_by_month, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
        plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
        plt.legend()
        plt.show()
