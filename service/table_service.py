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
        table.products[product] = table.products.get(product, 0) + 1
        return table

    def add_product_by_table_id_and_product_id(self, table_id, prod_id):
        table: Table = self.tables_repo.find_by_id(table_id)
        product: Product = self.products_repo.find_by_id(prod_id)
        table.products[product] = table.products.get(product, 0) + 1
        return table

    def delete_product_by_table_id_and_product_name(self, table_id , prod_id):
        table: Table = self.tables_repo.find_by_id(table_id)

        product: Product = self.products_repo.find_by_id(prod_id)

        for products in table.products:
            if products.id == product.id:
                if table.products[products] == 1:
                    del table.products[products]
                    return table
                else:
                    table.products[products] -= 1
                    return table
        raise Exception(f'{product.name} not in table {table_id}')

    def print_products_table_by_id(self, id):
        table: Table = self.tables_repo.find_by_id(id)
        return f"Waiter {table.waiter.name}, {table.get_formatted()} \n {' ||| '.join([prod.get_formatted() for prod in table.products])}"

    def find_by_id(self, id):
        return self.tables_repo.find_by_id(id)

    def find_all(self):
        return self.tables_repo.find_all()

    def delete_table(self, table_id):
        return self.tables_repo.delete_by_id(table_id)






