
from Entities.products import Product
from Entities.table import Table
from Repository.Repository import Repository
from Repository.json_repository import JsonRepository
from exceptions.entity_not_found_exc import EntityNotFoundException
from exceptions.table_exception import TableAlreadyOpenedException
from util.func_utils import find_first


class TableRepository(JsonRepository):
    def __init__(self, table_id=None, db_filename='table_db.json'):
        super().__init__(table_id,db_filename)

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

    def add_all(self, entities_iterable):
        self._entities.update(map(lambda entity: (entity._id, entity), entities_iterable))





