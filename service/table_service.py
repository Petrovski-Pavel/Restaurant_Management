from Entities.products import Product
from Entities.table import Table
from Repository.products_repository import ProductsRepository
from Repository.table_repository import TableRepository


class TableService:
    def __init__(self, tables_repo: TableRepository, products_repo: ProductsRepository):
        self.tables_repo = tables_repo
        self.products_repo = products_repo


    def add_product_by_table_id_and_product_name(self, id, name):
        table: Table = self.tables_repo.find_by_id(id)
        product: Product = self.products_repo.find_by_name(name)
        table.products[product.type][product] = table.products[product.type].get(product, 0) + 1
        return table

    def delete_product_by_table_id_and_product_name(self, id , name):
        table: Table = self.tables_repo.find_by_id(id)
        product: Product = self.products_repo.find_by_name(name)
        if product in table.products[product.type]:
                if table.products[product.type][product] == 1:
                    del table.products[product.type][product]
                    return table
                else:
                    table.products[product.type][product] -= 1
                    return table
        raise Exception(f'{product.name} not in table {id}')

    def print_products_table_by_id(self, id):
        table: Table = self.tables_repo.find_by_id(id)
        return f"Waiter {table.waiter.name}, {table.get_formatted()} \n {' ||| '.join([prod.get_formatted() for prod_dict in table.products.values() for prod in prod_dict])}"







