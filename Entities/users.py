

class Users:
    def __init__(self, name=None, password=None, id=None):
        self.id = id
        self.name = name
        self.password = password
        self.role = None
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__


    def __str__(self):
        return f'ID: {self.id} Name: {self.name}, Key: {self.password}, Role: {self.role}'

    def get_formatted(self):
        if self.role == 'Waiter':
            return f'ID: {self.id} | Name: {self.name:10.10s} | Key: {self.password} | Role: {self.role:15.15s} | Tables: {", ".join([str(t._id) for t in self.tables])}'

        return f'ID: {self.id} | Name: {self.name:10.10s} | Key: {self.password} | Role: {self.role:15.15s}'


class Administrator(Users):
    def __init__(self, name=None, password=None, id=None):
        super().__init__(name, password, id)
        self.role = __class__.__name__


class Waiter(Users):
    def __init__(self, name=None, password=None, id=None):
        super().__init__(name, password, id)
        self.tables = []
        self._invoicement = 0
        self.role = __class__.__name__


class Manager(Users):
    def __init__(self, name=None, password=None, id=None):
        super().__init__(name, password, id)
        self.role = __class__.__name__


# ad = Administrator('Ivan',1245,)
# print(ad)
# print(ad.get_formatted())
