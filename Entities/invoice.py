from Entities.table import Table
from Entities.users import Waiter
from Repository.table_repository import TableRepository
from Repository.user_repository import UserRepository


class Invoicing:
    def __init__(self, number, table: Table):
        self.id = number
        self.table = table

    def get_formatted(self):
        return f'Invoice {self.__class__.__name__} number: {self.id} for table: {self.table._id} by waiter: {self.table.waiter.name}'



class Bill(Invoicing):
    def __init__(self, number, table: Table):
        super().__init__(number, table)

class Invoice(Invoicing):
    def __init__(self, number, table: Table, company_name, customer_name, bank_account_number):
        super().__init__(number, table)
        self.company_name = company_name
        self.customer_name = customer_name
        self.bank_account_number = bank_account_number

    def get_formatted(self):
        return f'Invoice number: {self.id}\n Mr/Ms {self.customer_name}' \
               f' Company name: "{self.company_name}"\n' \
               f' by waiter: {self.table.waiter.name}'
