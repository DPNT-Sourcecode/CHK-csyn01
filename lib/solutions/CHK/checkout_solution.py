

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    total_price = 0
    raw_items_list = [x.strip() for x in skus.split(",")]
    items_counter = [(x, raw_items_list.count(x)) for x in set(raw_items_list)]
    for i in items_counter:
        if i[0] == 'A' and i[1] == 3:
            total_price += 130
        elif i[0] == 'B' and i[1] == 2:
            total_price += 45
        elif i[0] == 'C':
            total_price += 20
        elif i[0] == 'D':
            total_price += 15
        else:
            return -1

    return total_price


if __name__ == '__main__':
    a = checkout("A, B, C, D, D")
    print(a)





