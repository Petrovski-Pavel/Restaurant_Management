

class Users:
    def __init__(self, name=None, password=None, id=None):
        self.id = id
        self.name = name
        self.password = password
        self.role = None
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    @classmethod
    def from_json(cls, prop_dict):
        return cls( prop_dict['name'], prop_dict['password'],prop_dict['id'])

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__

        }


    def __str__(self):
        return f'ID: {self.id} Name: {self.name}, Key: {self.password}, Role: {self.role}'

    def get_formatted(self):
        if self.role == 'Waiter':
            return f'ID: {self.id} | Name: {self.name:} | Key: {self.password} | Role: {self.role:} | Tables: {", ".join([str(t) for t in self.tables])}'

        return f'ID: {self.id} | Name: {self.name} | Key: {self.password} | Role: {self.role:15.15s}'


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


    @classmethod
    def from_json(cls, prop_dict):
        ent = cls(prop_dict['name'], prop_dict['password'],prop_dict['id'])
        ent.tables = prop_dict['tables']
        ent._invoicement = prop_dict['invoicement']
        return ent

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'tables': self.tables,
            'invoicement': self._invoicement,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class Manager(Users):
    def __init__(self, name=None, password=None, id=None):
        super().__init__(name, password, id)
        self.role = __class__.__name__



