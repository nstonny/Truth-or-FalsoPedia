from single_category import Category

class Categories:
    def __init__(self, categories):
        self.categories = categories



    def get_all_categories(self):
        return self.categories

    def get_all_summaries(self):
        summaries = []
        for item in self.categories:
            summaries.append(item.get_summary())
        return summaries



"""category1 = Category("Flowering plant")
#category2 = Category("List of European countries")
category2 = Category("List of music artists and bands from England")
category3 = Category("List of music artists and bands from England")


total_categories = Categories([category1, category2, category3])

all_items = total_categories.get_all_categories()

for item in all_items:
    if item:
        print(item.get_summary())"""


