

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items_list = [x.strip() for x in skus.split(",")]
    cnt = Counter()
    for i in items_list:
        try:
            int(i)
        except ValueError:
            return -1

