from Repository.products_repository import ProductsRepository


class ProductsService:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    def save(self):
        return self.products_repository.save()

    def load(self):
        return self.products_repository.load()

    def find_by_name(self, name):
        self.products_repository.find_by_name(name)

    def delete_by_name(self, name):
        self.products_repository.delete_by_name(name)

    def find_all_prod(self):
        self.products_repository.find_all()