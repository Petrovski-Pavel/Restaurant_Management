class Product:
    def __init__(self, name=None, price=None, quantity=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__
        self.type = __class__.__name__

    # @classmethod
    # def from_json(cls, prop_dict):
    #     print(type(cls(prop_dict['id'], prop_dict['name'], prop_dict['price'], prop_dict['quantity'])))
    #     return cls(prop_dict['id'], prop_dict['name'], prop_dict['price'], prop_dict['quantity'])


    def __str__(self):
        return f'{self.id}, {self.name}, {self.type}, {self.price}, {self.quantity}'

    def get_formatted(self):
        if self.type == 'Beverage':
            return f'ID: {self.id} | Name: {self.name:20.20s} | {self.type:8.8s} | Price: {self.price:.2f} lv | Quantity: {self.quantity:.2f} ml'
        return f'ID: {self.id} | Name: {self.name:20.20s} | {self.type:8.8s} | Price: {self.price:.2f} lv | Quantity: {self.quantity:.2f} gr'


class Beverage(Product):
    def __init__(self, name=None, price=None, quantity=None, id=None):
        super().__init__(name, price, quantity, id)
        self.type = __class__.__name__


class Dish(Product):
    def __init__(self, name=None, price=None, quantity=None, id=None):
        super().__init__(name, price, quantity, id)
        self.type = __class__.__name__
