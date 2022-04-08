from Entities.products import Product
from Repository.json_repository import JsonRepository
from exceptions.entity_not_found_exc import EntityNotFoundException
from util.func_utils import find_first, find_every


class ProductsRepository(JsonRepository):

    def find_by_name(self, name: str) -> Product:
        return find_first(lambda p: p.name == name, self.find_all())


    def find_by_type(self, type):
        this_type = find_every(lambda p: p.type == type, self.find_all())

        if this_type:
            return this_type
        raise EntityNotFoundException(f'No products from type: {type}.')


    def delete_by_name(self, name):
        old_prod = self.find_by_name(name)
        del self._entities[old_prod.id]
        return old_prod
















