
from Repository.json_repository import JsonRepository
from exceptions.entity_not_found_exc import EntityNotFoundException



class UserRepository(JsonRepository):

    def create(self, entity):
        """
        Created new entity in the repository and assigns it a unique id using idGenrator provided in __init__()
        :param entity: entity to be created
        :return: created new entity with assignes
        """
        if self.find_by_key(entity.password) is not None:
            raise Exception(f"User with this key already exists")

        if entity.id is None:
            entity.id = self._idGenrator.get_next_id()
        self._entities[entity.id] = entity
        return entity

    def find_by_key(self, key):
        found = [usr for usr in self.find_all() if usr.password == key]
        if found:
            return found[0]

        return
       #raise EntityNotFoundException(f'No user with this key: {key}')

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

    def get_waiter_financial_statement(self, key):
        waiter = self.find_by_key(key)
        fin = waiter._invoicement
        waiter._invoicement = 0
        return fin


