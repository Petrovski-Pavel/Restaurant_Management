from typing import Iterator


from Repository.Repository import Repository
from Repository.json_repository import JsonRepository

from exceptions.entity_not_found_exc import EntityNotFoundException
from exceptions.invoice_exceptins import InvoiceNotFoundException, InvoiceAlreadyCreated
from util.func_utils import find_first

class InvoiceRepository(JsonRepository):
    def __init__(self, idGenerator=None):
        super().__init__(idGenerator,db_filename='invoice_db.json')
        self.income = 0

    def create(self, invoice):
        if invoice.id in self._entities:
            raise InvoiceAlreadyCreated(f'Invoice with number: {invoice.id} already exist.')
        self._entities[invoice.id] = invoice
        return invoice

    def find_by_table_id(self, tbl_id):
        return find_first(lambda inv: inv.table._id == tbl_id, self.find_all())

    def get_financial_statement(self):
        return self.income










