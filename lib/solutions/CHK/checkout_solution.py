from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    total_price = 0
    items_counter = Counter([x for x in skus])
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
        except SuperMarketException:
            return -1

    return total_price


class SuperMarket:
    """
    Supermarket object with a specific checkout list
    This object includes checkout rules, and must be up to date according to newest discounts
    """
    def __init__(self):
        self.total_items = None
        self.product_a_sum = 0
        self.product_b_sum = 0
        self.product_c_sum = 0
        self.product_d_sum = 0
        self.product_e_sum = 0
        self.total_price = 0

    def add_product(self, product):
        """
        Adds item to class
        :param product: tuple
        """
        if product[0] == 'A':
            self.product_a(product[1])
        elif product[0] == 'B':
            self.product_b(product[1])
        elif product[0] == 'C':
            self.product_c(product[1])
        elif product[0] == 'D':
            self.product_d(product[1])
        elif product[0] == 'E':
            self.product_e(product[1])
        else:
            raise SuperMarketException()

    def product_a(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 50
        DISCOUNT = 130
        DISCOUNT_THRESHHOLD = 3
        if items % DISCOUNT_THRESHHOLD == 0:
            self.product_a_sum += int(DISCOUNT * (items / DISCOUNT_THRESHHOLD))
        else:
            self.product_a_sum += PRICE * (items % DISCOUNT_THRESHHOLD) + (DISCOUNT * int(items / DISCOUNT_THRESHHOLD))

    def product_b(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 30
        DISCOUNT = 45
        DISCOUNT_THRESHHOLD = 2
        if items % 2 == 0:
            self.product_b_sum += int(DISCOUNT * (items / DISCOUNT_THRESHHOLD))
        else:
            self.product_b_sum += PRICE * (items % DISCOUNT_THRESHHOLD) + (DISCOUNT * int(items / DISCOUNT_THRESHHOLD))

    def product_c(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 20
        self.product_c_sum = PRICE * items

    def product_d(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 15
        self.product_d_sum = PRICE * items

    def product_e(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 40
        self.product_e_sum = PRICE * items

    def special_offers(self):
        """
        Calculates price right before checkout to verify special deals
        """
        for i in self.total_items:
            if 'D' == i[0] and i[1] >= 2:








    def checkout(self):
        self.special_offers()

        self.total_price = self.product_a_sum + self.product_b_sum + self.product_c_sum + self.product_d_sum + \
                           self.product_e_sum


class SuperMarketException(Exception):
    """Invalid product input"""
    pass

if __name__ == '__main__':
    a = checkout("ABACDDE")
