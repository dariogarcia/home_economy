from categories import categories

class Movement:
    
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = None

    def assign_category(self):
        found_categories = set()
        for cat_name,cat_terms in categories.items():
            for term in cat_terms:
                if term in self.description:
                    found_categories.add(cat_name)
        if len(found_categories) == 0:
            print('Category not found for:',self.description,self.amount)
        if len(found_categories) == 2 and 'hipoteca' in found_categories:
            found_categories.remove('hipoteca')
            print('WARNING: Ignoring hipoteca label for:',self.description)
        if len(found_categories) >= 2:
            print('Multiple categories found for:',self.description,':',found_categories)
        #TODO: This is ugly
        self.category = next(iter(found_categories))
