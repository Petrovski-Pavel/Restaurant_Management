from Entities.users import Waiter


class Table:
    def __init__(self, id, waiter: Waiter):
        self.waiter = waiter
        self._id = id
        self.products = {'Beverage': {}, 'Dish': {}}


    def __str__(self):
        pr = " | ".join([f'{k}: {", ".join([f"{vv.name}: {v[vv]}"for vv in v])}' for k, v in self.products.items()])
        return f'{self._id} {pr}'

    def get_formatted(self):
        pr = " | ".join([f'{k}: {", ".join([f"{vv.name}: {v[vv]}" for vv in v])}'for k, v in self.products.items()])
        return f'| Table number: {self._id} | opened by {self.waiter.name} | with products: {pr}'

    # def add_product(self, product):
    #     pass
