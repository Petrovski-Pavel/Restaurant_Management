from Entities.table import Table



class Invoicing:
    def __init__(self, number=None, table: Table = None):
        self.id = number
        self.table = table
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def get_formatted(self):
        return f'Invoice {self.__class__.__name__} number: {self.id} for table: {self.table._id} by waiter: {self.table.waiter.name}'



class Bill(Invoicing):
    def __init__(self, number=None, table: Table=None):
        super().__init__(number, table)

class Invoicee(Invoicing):
    def __init__(self, number=None, table: Table=None, company_name=None, customer_name=None, bank_account_number=None):
        super().__init__(number, table)
        self.company_name = company_name
        self.customer_name = customer_name
        self.bank_account_number = bank_account_number

    def get_formatted(self):
        return f'Invoice number: {self.id}\n Mr/Ms {self.customer_name}' \
               f' Company name: "{self.company_name}"\n' \
               f' by waiter: {self.table.waiter.name}'
