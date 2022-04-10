from Entities.users import Waiter


class Table:
    def __init__(self, id=None, waiter: Waiter = None):
        self.waiter = waiter
        self._id = id
        self.products = {}
        #self.products = {'Beverage': {}, 'Dish': {}}

    # @classmethod
    # def from_json(cls, prop_dict):
    #     return cls(prop_dict['id'], prop_dict['Waiter name'])
    #
    # def to_json(self):
    #     return {
    #         'id': self._id,
    #         'Waiter name': self.waiter.name,
    #         'Products': ", ".join([prod.name for prod_dict in self.products.values() for prod in prod_dict]),
    #         '_module': self.__class__.__module__,
    #         '_class': self.__class__.__name__
    #
    #     }



    def __str__(self):
        pr = " | ".join([f'{k}: {", ".join([f"{vv.name}: {v[vv]}"for vv in v])}' for k, v in self.products.items()])
        return f'{self._id} {pr}'

    def get_formatted(self):
        #pr = " | ".join([f'{k}: {", ".join([f"{vv.name}: {v[vv]}" for vv in v])}'for k, v in self.products.items()])
        return f'| Table number: {self._id} | opened by {self.waiter.name} | with products: {[f"{prod.name}: {quant}" for prod, quant in self.products.items()]}'

    # def add_product(self, product):
    #     pass
