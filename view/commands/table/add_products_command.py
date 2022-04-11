from Entities.products import Product
from controller.table_controller import TableController


class AddProductsCommand:
    def __init__(self, table_controller: TableController, ):
        self.table_controller = table_controller

    def __call__(self, table_id, product_name):
        self.table_controller.add_product(table_id, product_name)