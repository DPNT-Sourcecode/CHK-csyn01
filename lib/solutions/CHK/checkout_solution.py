

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    total_price = 0
    raw_items_list = [x for x in skus]
    items_counter = [(x, raw_items_list.count(x)) for x in set(raw_items_list)]
    for i in items_counter:
        if i[0] == 'A':
            if i[1] > 3:
                total_price += 130
            else:
                total_price += 50 * i[1]
        elif i[0] == 'B':
            if i[1] > 2:
                total_price += 45
            else:
                total_price += 30 * i[1]
        elif i[0] == 'C':
            total_price += 20 * i[1]
        elif i[0] == 'D':
            total_price += 15 * i[1]
        else:
            return -1

    return total_price


if __name__ == '__main__':
    a = checkout("AAAA")
    print(a)



