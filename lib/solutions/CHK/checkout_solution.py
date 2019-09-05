from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    items_list = [x for x in skus]
    market_obj = SuperMarket(items_list)
    for item in market_obj.total_items:
        try:
            market_obj.add_product(product=item)
        except SuperMarketException:
            return -1

    return market_obj.total_price


class SuperMarket:
    """
    Supermarket object with a specific checkout list
    This object includes checkout rules, and must be up to date according to newest discounts
    """

    def __init__(self, total_items):
        self.total_items = Counter(total_items)
        self.total_price = 0
        self.special_offers()

    def add_product(self, product):
        """
        Adds item to class
        :param product: tuple
        """
        if product == 'A':
            self.product_a(self.total_items[product])
        elif product == 'B':
            self.product_b(self.total_items[product])
        elif product == 'C':
            self.product_c(self.total_items[product])
        elif product == 'D':
            self.product_d(self.total_items[product])
        elif product == 'E':
            self.product_e(self.total_items[product])
        elif product == 'F':
            self.product_f(self.total_items[product])
        elif product == 'G':
            self.product_g(self.total_items[product])
        elif product == 'H':
            self.product_h(self.total_items[product])
        elif product == 'I':
            self.product_i(self.total_items[product])
        elif product == 'J':
            self.product_j(self.total_items[product])
        elif product == 'K':
            self.product_k(self.total_items[product])
        elif product == 'L':
            self.product_l(self.total_items[product])
        elif product == 'M':
            self.product_m(self.total_items[product])
        elif product == 'N':
            self.product_n(self.total_items[product])
        elif product == 'O':
            self.product_o(self.total_items[product])
        elif product == 'P':
            self.product_p(self.total_items[product])
        elif product == 'Q':
            self.product_q(self.total_items[product])
        elif product == 'R':
            self.product_r(self.total_items[product])
        elif product == 'S':
            self.product_s(self.total_items[product])
        elif product == 'T':
            self.product_t(self.total_items[product])
        elif product == 'U':
            self.product_u(self.total_items[product])
        elif product == 'V':
            self.product_v(self.total_items[product])
        elif product == 'W':
            self.product_w(self.total_items[product])
        elif product == 'X':
            self.product_x(self.total_items[product])
        elif product == 'Y':
            self.product_y(self.total_items[product])
        elif product == 'Z':
            self.product_z(self.total_items[product])
        else:
            raise SuperMarketException()

    def product_a(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 50
        total_price = 0
        while items > 0:
            if items >= 5:
                total_price += 200
                items -= 5
            elif items >= 3:
                total_price += 130
                items -= 3
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_b(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 30
        total_price = 0
        while items > 0:
            if items >= 2:
                total_price += 45
                items -= 2
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_c(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 20
        self.total_price += PRICE * items

    def product_d(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 15
        self.total_price += PRICE * items

    def product_e(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 40
        self.total_price += PRICE * items

    def product_f(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 10
        if self.total_items['F'] > 2:
            discount_number = int(self.total_items['F'] / 3)
            items -= discount_number
        self.total_price += PRICE * items

    def product_g(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 20
        self.total_price += PRICE * items

    def product_h(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        5H for 45, 10H for 80
        """
        PRICE = 10
        total_price = 0
        while items > 0:
            if items >= 10:
                total_price += 80
                items -= 10
            elif items >= 5:
                total_price += 45
                items -= 5
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_i(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 35
        self.total_price += PRICE * items

    def product_j(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 60
        self.total_price += PRICE * items

    def product_k(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 80
        total_price = 0
        while items > 0:
            if items >= 2:
                total_price += 150
                items -= 2
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_l(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 90
        self.total_price += PRICE * items

    def product_m(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 15
        self.total_price += PRICE * items

    def product_n(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 40
        self.total_price += PRICE * items

    def product_o(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 10
        self.total_price += PRICE * items

    def product_p(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        5P for 200
        """
        PRICE = 50
        total_price = 0
        while items > 0:
            if items >= 5:
                total_price += 200
                items -= 5
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_q(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 30
        total_price = 0
        while items > 0:
            if items >= 3:
                total_price += 80
                items -= 3
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_r(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 50
        self.total_price += PRICE * items

    def product_s(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 30
        self.total_price += PRICE * items

    def product_t(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 20
        self.total_price += PRICE * items

    def product_u(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 40
        self.total_price += PRICE * items

    def product_v(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        2V for 90, 3V for 130
        """
        PRICE = 50
        total_price = 0
        while items > 0:
            if items >= 3:
                total_price += 130
                items -= 3
            elif items >= 2:
                total_price += 90
                items -= 2
            else:
                total_price += PRICE
                items -= 1
        self.total_price += total_price

    def product_w(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 20
        self.total_price += PRICE * items

    def product_x(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 90
        self.total_price += PRICE * items

    def product_y(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 10
        self.total_price += PRICE * items

    def product_z(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 50
        self.total_price += PRICE * items

    def special_offers(self):
        """
        Special offers before starting the general calculation
        """
        if 'B' in self.total_items and self.total_items['E'] >= 2:
            discount_num = int(self.total_items['E'] / 2)
            self.total_items['B'] -= discount_num

        if 'M' in self.total_items and 'N' in self.total_items:
            discount_num = int(self.total_items['N'] / 3)
            self.total_items['M'] -= discount_num

        if 'R' in self.total_items and 'Q' in self.total_items:
            discount_num = int(self.total_items['R'] / 3)
            self.total_items['Q'] -= discount_num

        # if 'U' in self.total_items:
        #     discount_num = int(self.total_items['U'] / 3)
        #     self.total_items['U'] -= discount_num


class SuperMarketException(Exception):
    """Invalid product input"""
    pass






