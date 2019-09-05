import os

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    total_price = 0
    raw_items_list = [x for x in skus]
    items_counter = [(x, raw_items_list.count(x)) for x in set(raw_items_list)]
    for i in items_counter:
        try:
            if i[0] == 'A':
                if i[1] % 3 == 0:
                    total_price += int(130 * (i[1] / 3))
                else:
                    total_price += 50 * (i[1] % 3) + (130 * int(i[1] / 3))
            elif i[0] == 'B':
                if i[1] % 2 == 0:
                    total_price += int(45 * (i[1] / 2))
                else:
                    total_price += 30 * (i[1] % 2) + (45 * int(i[1] / 2))
            elif i[0] == 'C':
                total_price += 20 * i[1]
            elif i[0] == 'D':
                total_price += 15 * i[1]
            elif i[0] == 'E':
                total_price += 40 * i[1]
            else:
                return -1
        except ValueError:
            return -1

    return total_price


class SuperMarket:
    """
    Supermarket object with a specific checkout list
    This object includes checkout rules, and must be up to date according to newest discounts
    """
    def __init__(self):
        self.products_list = []
        self.product_a_sum = 0
        self.product_b_sum = 0
        self.total_price = 0

    def add_product(self, product):
        """
        Adds item to class
        :param product: tuple
        """
        self.products_list.append(product)
        if product[0] == 'A':
            self.product_a(product[1])
        elif product[0] == 'B':
            self.product_a(product[1])
        elif product[0] == 'E':
            self.product_b(product[1])
        else:
            raise SuperMarketException()

    def product_a(self, items):
        """
        calculates product according to its pricing rules
        :param items: int
        """
        pass

    def product_b(self, items):
        """
        calculates product according to its pricing rules
        :param items: int
        """
        pass

    def product_e(self, items):
        """
        calculates product according to its pricing rules
        :param items: int
        """
        pass


class SuperMarketException(Exception):
    pass