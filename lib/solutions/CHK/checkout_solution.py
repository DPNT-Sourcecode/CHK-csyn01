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
    market_obj.checkout()
    return market_obj.total_price


class SuperMarket:
    """
    Supermarket object with a specific checkout list
    This object includes checkout rules, and must be up to date according to newest discounts
    """

    def __init__(self, total_items):
        self.total_items = Counter(total_items)
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
        else:
            raise SuperMarketException()

    def product_a(self, items):
        """
        calculates product according to its pricing rules
        :param items: int, number of items
        """
        PRICE = 50
        DISCOUNT_1 = 130
        DISCOUNT_2 = 200
        DISCOUNT_THRESHHOLD_1 = 3
        DISCOUNT_THRESHHOLD_2 = 5
        while items >= 0:
            if items >= 5:
                self.product_a_sum += PRICE * (items % DISCOUNT_THRESHHOLD_2) + (DISCOUNT_2 * int(items / DISCOUNT_THRESHHOLD_2))
                items -= DISCOUNT_THRESHHOLD_2
            elif items >= 3:
                self.product_a_sum += PRICE * (items % DISCOUNT_THRESHHOLD_1) + (DISCOUNT_1 * int(items / DISCOUNT_THRESHHOLD_1))
                items -= DISCOUNT_THRESHHOLD_1
            else:
                self.product_a_sum += PRICE
                items -= 1

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
        if 'B' in self.total_items and self.total_items['E'] >= 2:
            self.product_b_sum = self.product_b_sum - 30

    def checkout(self):
        self.special_offers()

        self.total_price = self.product_a_sum + self.product_b_sum + self.product_c_sum + self.product_d_sum + \
                           self.product_e_sum


class SuperMarketException(Exception):
    """Invalid product input"""
    pass

if __name__ == '__main__':
    print(checkout("AAAAAAAA"))
