
from Entities.products import Product
from Entities.table import Table
from Repository.Repository import Repository
from exceptions.entity_not_found_exc import EntityNotFoundException
from exceptions.table_exception import TableAlreadyOpenedException
from util.func_utils import find_first


class TableRepository(Repository):
    def __init__(self, table_id=None):
        super().__init__(table_id)

    def create(self, entity):
        if entity._id not in self._entities:
            self._entities[entity._id] = entity
            entity.waiter.tables.append(entity)
            return entity
        raise TableAlreadyOpenedException(f'Table {entity._id} already created.')

    def update(self, entity):
        self.find_by_id(entity._id)
        self._entities[entity._id] = entity
        return entity

    def find_table_by_waiter_key(self, key):
        return find_first(lambda t: t.waiter.password == key, self.find_all())

    def delete_by_id(self, id):
        old = self.find_by_id(id)
        old.waiter.tables.remove(old)
        del self._entities[id]
        return old





