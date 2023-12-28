class Merchant:
    def __init__(self, products):
        self.products=products
    def sell(self, item):
        self.products.remove(item)
        print(f"You have purchased {item}")
    def welcome():
        print(f"Welcome to my shop!")