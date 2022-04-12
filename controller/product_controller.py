from service.products_service import ProductsService


class ProductController:
    def __init__(self, product_service: ProductsService):
        self.product_service = product_service

    def save(self):
        return self.product_service.save()

    def load(self):
        return self.product_service.load()

    def find_by_name(self, name):
        return self.product_service.find_by_name(name)

    def delete_by_name(self, name):
        return self.product_service.delete_by_name(name)

    def find_all(self):
        return self.product_service.find_all_prod()

    def add_new_product(self, product):
        return self.product_service.add_product(product)
