import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from datetime import datetime

from categories import categories

class SetOfMoves:

    def __init__(self):
        self.moves = []
        self.months = set()

    def append_move(self,m):
        self.moves.append(m)
        self.months.add((m.date.month,m.date.year))

    def assign_categories(self):
        for m in self.moves:
            m.assign_category()

    def filter_by_date(self,date_init,date_end):
        som_filtered = SetOfMoves()
        for move in self.moves:
            #If date is in range, append
            if move.date >= datetime.strptime(date_init, '%d/%m/%Y')\
                    and move.date <= datetime.strptime(date_end, '%d/%m/%Y'):
                som_filtered.append_move(move)
        return som_filtered
    
    def filter_by_cat(self,category):
        som_filtered = SetOfMoves()
        for move in self.moves:
            if move.category == category:
                som_filtered.append_move(move)
        return som_filtered

    def filter_out_by_cat(self,category):
        som_filtered = SetOfMoves()
        for move in self.moves:
            if move.category != category:
                som_filtered.append_move(move)
        return som_filtered

    def total_by_cat_and_month(self):
        months_idx = []
        last_month_idx = 0
        cats_idx = np.array(categories.keys(),dtype='S20')
        amount_by_month_and_cat = np.zeros((len(categories),len(self.months)))
        #Sum costs of moves by month and cat
        for m in self.moves:
            idx_cat, = np.where(cats_idx == m.category)
            if len(idx_cat)!=1:
                raise Exception('Repeated category? Category with more than 10 chars?',
                        cats_idx,m.category,len(idx_cat))
            idx_cat = idx_cat[0]
            str_month = str(m.date.month)+'/'+str(m.date.year)
            #Month exists
            if str_month in months_idx:
                idx_mon = months_idx.index(str_month)
                amount_by_month_and_cat[idx_cat][idx_mon]+=m.amount
            else:
                months_idx.append(str_month)
                amount_by_month_and_cat[idx_cat][last_month_idx]+=m.amount
                last_month_idx+=1
        return months_idx, cats_idx, amount_by_month_and_cat

    def plot_histogram(self):

        months_labels, cats_labels, data_by_month = self.total_by_cat_and_month()
        #plot in reverse order
        num_months = len(months_labels)
        months_labels = reversed(months_labels)
        #cats_labels = np.flip(cats_labels,0)
        data_by_month = np.flip(data_by_month,1)
        # multiple line plot
        colors = ['blue','skyblue','olive','pink','red','yellow','green','purple','brown','cyan','black','grey']
        for idx_dm, dm in enumerate(data_by_month[:,]):
            if cats_labels[idx_dm]=='hipoteca':
                continue
            plt.plot(range(0,dm.shape[0]), dm*-1, marker='o', color=colors[idx_dm], linewidth=2,label=cats_labels[idx_dm])
        plt.grid()
        plt.legend(loc=0,ncol=3)
        plt.xticks(np.arange(num_months), months_labels)
        ax = plt.gca()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
        plt.show()
