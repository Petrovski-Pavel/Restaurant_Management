from service.table_service import TableService


class TableController:
    def __init__(self, table_service: TableService):
        self.table_service = table_service

    def add_product(self, id, name):
        return self.table_service.add_product_by_table_id_and_product_name(id, name)

    def delete_product(self, id, name):
        return self.table_service.delete_product_by_table_id_and_product_name(id , name)

