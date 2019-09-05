

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items_list = skus.split()
    for i in items_list:
        try:
            int(i)
        except ValueError:
            return -1


