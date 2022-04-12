from Repository.products_repository import ProductsRepository


class ProductsService:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    def save(self):
        return self.products_repository.save()

    def load(self):
        return self.products_repository.load()

    def find_by_name(self, name):
        return self.products_repository.find_by_name(name)

    def delete_by_name(self, name):
        return self.products_repository.delete_by_name(name)

    def find_all_prod(self):
        return self.products_repository.find_all()

    def find_by_id(self, id):
        return self.products_repository.find_by_id(id)

    def add_product(self, product):
        self.products_repository.create(product)
        self.products_repository.save()
        self.products_repository.load()

    def delete_by_id(self, id):
        self.products_repository.delete_by_id(id)
        self.products_repository.save()
