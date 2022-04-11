from service.invoice_service import InvoiceService


class InvoiceController:
    def __init__(self, invoice_service: InvoiceService):
        self.invoice_service = invoice_service

    def get_the_bill(self, table_id):
        return self.invoice_service.get_bill(table_id)

    def _get_the_invoice(self, table_id):
        return self.invoice_service.get_invoice(table_id)


