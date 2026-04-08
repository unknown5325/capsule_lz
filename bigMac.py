import csv
from collections import Counter


class BigMac:
    def __init__(self, collumn_1, collumn_2):
        self.coll_1 = collumn_1
        self.coll_2 = collumn_2

    @property
    def dollar_pr(self):
        lis_1 = []
        lis_2 = []
        with open("BigmacPrice.csv", "r", encoding="utf-8") as filed:
            csv_reader = csv.DictReader(filed)
            for row in csv_reader:
                lis_1.append(row[self.coll_1])
                lis_2.append(row[self.coll_2])
        result = dict(zip(lis_2, lis_1))
        return result
    

    def __del__(self):
        pass