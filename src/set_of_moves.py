#import matplotlib.pyplot as plt
import numpy as np

from categories import categories

class SetOfMoves:

    def __init__(self):
        self.moves = []
        self.months = set()

    def append_move(self,m):
        self.moves.append(m)
        self.months.update((m.date.month,m.date.year))

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
        months_idx = np.zeros((len(self.months),2))
        last_month_idx = 0
        cats_idx = np.array(categories.keys(),dtype='S10')
        amount_by_month_and_cat = np.zeros((len(categories),len(self.months)))
        #Sum costs of moves by month and cat
        for m in self.moves:
            idx_cat, = np.where(cats_idx == m.category)
            if len(idx_cat)!=1:
                raise Exception('Repeated category? Category with more than 10 chars?',
                        cats_idx,m.category,len(idx_cat))
            idx_cat = idx_cat[0]
            np_month = np.array([m.date.month,m.date.year])
            [idx_mon] = np.where((months_idx == np_month).all(axis=1))
            #Month exists
            if idx_mon.shape != (0,):
                amount_by_month_and_cat[idx_cat][idx_mon]+=m.amount
            else:
                months_idx[last_month_idx] = np_month
                amount_by_month_and_cat[idx_cat][last_month_idx]+=m.amount
                last_month_idx+=1
        ##Create and fill label numpy (categories sorted)
        #dtype = [('month', int), ('year', int)]
        #ordered_months = np.array([*sum_by_months_and_cats], dtype=dtype)
        #ordered_months = np.sort(ordered_months, order=['year','month'])
        ##Create and fill data numpy
        #month_and_cat_mat = np.zeros((len(categories),len(sum_by_months_and_cats)))
        #for month in ordered_months:
        #    for cat in categories.keys():
        #        print(sum_by_months_and_cats[month][cat])
        #        month_and_cat_mat[month][cat] = sum_by_months_and_cats[month][cat]
        #print(month_and_cat_mat)
        #todo_fill= dsfs

        #dtype = [('name', 'S10'), ('height', float), ('age', int)]
        #values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
        #    ...           ('Galahad', 1.7, 38)]
        #a = np.array(values, dtype=dtype)       # create a structured array
        #np.sort(a, order='height')


        return sum_np_data, month_and_cat_mat

    def plot_histogram(self):

        data_by_month = self.total_by_cat_and_month()
        # multiple line plot
        plt.plot( 'x', 'y1', data=data_by_month, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
        plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
        plt.legend()
        plt.show()
