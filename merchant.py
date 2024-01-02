class Merchant:
    def __init__(self, products):
        self.products=products
    def sell(self, item):
        self.products.remove(item)
    def welcome(x):
        print(f"Welcome to my shop! You can buy items from my catalogue, or sell any sellable item here!")
