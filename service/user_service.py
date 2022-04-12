from Entities.products import Product
from Entities.table import Table
from Repository.table_repository import TableRepository
from Repository.user_repository import UserRepository
from exceptions.table_exception import CannotFindTableException
from exceptions.wrong_user_exceptions import UserCannotOpenTable


class UserService:
    def __init__(self, users_repo: UserRepository, tables_repo: TableRepository):
        self.users_repo = users_repo
        self.tables_repo = tables_repo


    def check_if_waiter_has_table(self, waiter, table):
        if table in waiter.tables:
            return True
        return False
        #raise CannotFindTableException(f'User {waiter.name} doesn have table with number {table._id}.')

    def waiter_open_table_by_waiter_key_table_id(self,key, table_id):
        waiter = self.users_repo.find_by_key(key)
        table = self.tables_repo.create(Table(table_id, waiter))
        if not self.check_if_waiter_has_table(waiter, table):
            if waiter.role == 'Administrator':
                raise UserCannotOpenTable(f'User {waiter.name} is {waiter.role} and cannot open tables!')
            return waiter, table

    # def waiter_add_product_by_waiter_key_and_table_id(self,key, tbl_id, product: Product):
    #     table: Table = self.tables_repo.find_by_id(tbl_id)
    #     waiter = self.users_repo.find_by_key(key)
    #     if self.check_if_waiter_has_table(waiter, table):
    #         table.products[product.type][product] = table.products[product.type].get(product, 0) + 1
    #         return waiter, table


    # def print_products_on_waiter_table_by_key_id(self,key, id):
    #     waiter = self.users_repo.find_by_key(key)
    #     table = self.tables_repo.find_by_id(id)
    #     if self.check_if_waiter_has_table(waiter, table):
    #         return f'Waiter {waiter.name}, {table.get_formatted()}'

    def delete_table_by_waiter_key_table_id(self, key, id):
        waiter = self.users_repo.find_by_key(key)
        table = self.tables_repo.find_by_id(id)
        if self.check_if_waiter_has_table(waiter,table):
            self.tables_repo.delete_by_id(id)
            waiter.tables.remove(table)
            return waiter

    def list_all_tables(self, key):
        user = self.users_repo.find_by_key(key)
        for table in user.tables:
            yield table._id

    # def delete_product_from_table(self, key, id, product: Product):
    #     waiter = self.users_repo.find_by_key(key)
    #     table = self.tables_repo.find_by_id(id)
    #     if self.check_if_waiter_has_table(waiter, table):
    #         if product in table.products[product.type]:
    #             if table.products[product.type][product] == 1:
    #                 del table.products[product.type][product]
    #                 return waiter, table
    #             else:
    #                 table.products[product.type][product] -= 1
    #                 return waiter,table
    #         raise Exception(f'{product.name} not in table {table._id}')

    def add_staff(self, person):
        self.users_repo.create(person)
        self.users_repo.save()
        #self.users_repo.load()

    def find_all(self):
        self.users_repo.find_all()

    def load(self):
        self.users_repo.load()

    def save(self):
        self.users_repo.save()

