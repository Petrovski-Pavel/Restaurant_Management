products = {'Beverage': {}, 'Dish': {}}

class Prods:
    def __init__(self, name , price, type):
        self.name = name
        self.price = price
        self.type = type

prod1 = Prods('Pizza', 12, 'Dish')
prod2 = Prods('Budweiser', 4.90, 'Beverage')
prod5 = Prods('Budweiser', 4.90, 'Beverage')
prod3 = Prods('Sandwich', 8.20, 'Dish')
prod3 = Prods('Sandwich', 8.20, 'Dish')

if prod5 == prod2:
    print(True)
else:
    print(False)

prods = [prod1, prod1, prod3]

for prod in prods:
    products[prod.type][prod] = products[prod.type].get(prod, 0)+1
print(products)
print("\n".join(['I', 'would', 'expect', 'multiple', 'lines']))