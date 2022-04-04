
from Repository.Repository import Repository
from exceptions.entity_not_found_exc import EntityNotFoundException



class UserRepository(Repository):
    def __init__(self, idGenerator):
        super().__init__(idGenerator)

    def find_by_key(self, key):
       found = [usr for usr in self.find_all() if usr.password == key]
       if found:
           return found[0]
       raise EntityNotFoundException(f'No user with this key: {key}')

    def find_by_name(self, name):
        found = [usr for usr in self.find_all() if usr.name == name]
        if found:
            return found[0]
        raise EntityNotFoundException(f'No user with this name: {name}')

    def delete_by_key(self, key):
        old = self.find_by_key(key)
        ide = old.id
        del self._entities[ide]
        return old

    def delete_by_name(self, name):
        old = self.find_by_name(name)
        ide = old.id
        del self._entities[ide]
        return old

