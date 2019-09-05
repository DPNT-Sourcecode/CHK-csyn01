

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    items_list = [x.strip() for x in skus.split(",")]
    count_dict = (x, items_list.count(x) or x in items_list)
    for i in items_list:
        try:
            int(i)
        except ValueError:
            return -1


