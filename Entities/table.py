from Entities.users import Waiter


class Table:
    def __init__(self, id=None, waiter: Waiter = None):
        self.waiter = waiter
        self._id = id
        self.products = {}



    def __str__(self):
        pr = ' | '.join([f"{prod.name}: {quant}" for prod, quant in self.products.items()])
        return f'{self._id} {pr}'

    def get_formatted(self):
        pr = ' | '.join([f"{prod.name}: {quant}" for prod, quant in self.products.items()])
        return f'| Table number: {self._id} | opened by {self.waiter.name} | with products: {pr}'
