from Entities.invoice import Invoicee
from Entities.table import Table
from Repository.id_generator_uuid import IdGeneratorUuid
from Repository.invoicing_repository import InvoiceRepository
from Repository.table_repository import TableRepository
from Repository.user_repository import UserRepository
import os

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice


class InvoiceService:
    def __init__(self, tables_repo: TableRepository, invoice_repo: InvoiceRepository, user_repository: UserRepository):
        self.user_repository = user_repository
        self.invoice_repo = invoice_repo
        self.tables_repo = tables_repo


    def get_bill(self, tbl_id):
        table = self.tables_repo.find_by_id(tbl_id)

        invoice = self.invoice_repo.find_by_table_id(table._id)


        total = 0
        print("\n-------------------------Bill-------------------------")
        #print(f'{invoice.id}')
        for product, quantity in table.products.items():
            print(f"\n{product.name} x {quantity} -> {product.price}lv")
            total += product.price * quantity
        print(f"\n-------------Total: {total}")
        print(f"Waiter: {table.waiter.name}")

        self.invoice_repo.income += total
        table.waiter._invoicement += total

        print(table.waiter._invoicement)
        print(self.invoice_repo.income)

        self.tables_repo.delete_by_id(tbl_id)
        self.user_repository.save()
        return

    def get_invoice(self, tbl_id, company_name = 'Company Name', customer_name = 'Customer Name', bank_acc='Imaginary Bank Acc Number'):
        id_gen = IdGeneratorUuid()
        table: Table = self.tables_repo.find_by_id(tbl_id)
        self.invoice_repo.create(Invoicee(id_gen,table, company_name,customer_name, bank_acc))
        invoice1 = self.invoice_repo.find_by_table_id(table._id)
        print(invoice1)
        total = 0
        # if invoice1.__class__.__name__ == 'Invoice':

        # choosing English as the document language

        os.environ["INVOICE_LANG"] = "en"

        client = Client(invoice1.company_name)

        provider = Provider('PPRestaurant', bank_account=invoice1.bank_account_number, bank_code='9001')

        creator = Creator(table.waiter.name)

        invoice = Invoice(client, provider, creator)

        for prod, quantity in table.products.items():
            total += prod.price * quantity
            invoice.add_item(Item(quantity, prod.price, description=prod.name))

        # invoice.add_item(Item(26, 780, description="Milk"))
        #
        # invoice.add_item(Item(14, 460, description="Fruits"))
        #
        # invoice.add_item(Item(10, 290, description="Nuts"))
        #
        # invoice.add_item(Item(3, 165, description="Biscuits"))

        invoice.currency = "BGN."

        invoice.number = invoice1.id

        docu = SimpleInvoice(invoice)

        docu.gen("invoice2.pdf",generate_qr_code=False)  # you can put QR code by setting the #qr_code parameter to ‘True’

        # docu.gen("invoice.xml")  ## We can also generate an XML file of this invoice
        self.invoice_repo.income += total
        table.waiter._invoicement += total

        print(table.waiter._invoicement)
        print(self.invoice_repo.income)

        self.tables_repo.delete_by_id(tbl_id)
        self.user_repository.save()
        return

    def get_financial_statement(self):
        return self.invoice_repo.get_financial_statement()