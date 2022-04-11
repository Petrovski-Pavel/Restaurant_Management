from tkinter import ttk

from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController

import tkinter as tk

from view.components.waiters.products_view import ProductsView


class TableView(tk.Toplevel):
    def __init__(self,parent, table_id, table_controller: TableController, products_controller: ProductController, invoice_controller: InvoiceController):
        super().__init__(parent)
        self.parent = parent

        self.invoice_controller = invoice_controller
        self.products_controller = products_controller
        self.table_controller = table_controller
        self.title(table_id)
        self.geometry('800x400')
        self.table_id = table_id

        self.table = self.table_controller.table_service.tables_repo.find_by_id(table_id)

        self.tree = self.create_tree_widget(self.table_id)


        tk.Button(self, text='Add product',
                  command=lambda: ProductsView(self,self.table_id, self.table_controller,
                                               self.products_controller)).grid()
        tk.Button(self, text='Get Bill',
                  command=lambda: [self.invoice_controller.get_the_bill(table_id), self.destroy(), self.parent.show_tables()]).grid()

    def create_tree_widget(self, table_id):

        columns = ('name', 'price', 'quantity')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('name', text='Name')
        tree.heading('price', text='Price')
        tree.heading('quantity', text='Quantity')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        for prod, quant in self.table.products.items():
            tree.insert('', tk.END, values=(prod.name, prod.price, quant))

        return tree
