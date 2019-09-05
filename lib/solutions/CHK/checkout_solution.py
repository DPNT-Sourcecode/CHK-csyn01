

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    raw_items_list = [x.strip() for x in skus.split(",")]
    count_dict = [(x, raw_items_list.count(x)) for x in set(raw_items_list)]

    return count_dict


if __name__ == '__main__':
    a = checkout("A, B, C, D, D")
    print(a)




