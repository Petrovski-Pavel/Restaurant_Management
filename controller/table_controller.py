from service.table_service import TableService


class TableController:
    def __init__(self, table_service: TableService):
        self.table_service = table_service

    def add_product_by_name(self, id, name):
        return self.table_service.add_product_by_table_id_and_product_name(id, name)

    def add_product_by_id(self, table_id, prod_id):
        return self.table_service.add_product_by_table_id_and_product_id(table_id, prod_id)

    def delete_product(self, id, name):
        return self.table_service.delete_product_by_table_id_and_product_name(id , name)

    def find_all(self):
        return self.table_service.find_all()

    def find_by_id(self, id):
        return self.table_service.find_by_id(id)

    def delete_table(self, table_id):
        return self.table_service.delete_table(table_id)
