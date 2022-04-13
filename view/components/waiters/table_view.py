from tkinter import ttk

from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController

import tkinter as tk

from view.components.item_list import ItemList
from view.components.waiters.products_view import ProductsView


class TableView(tk.Toplevel):
    def __init__(self,parent, table_id, table_controller: TableController, products_controller: ProductController, invoice_controller: InvoiceController, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user


        self.invoice_controller = invoice_controller
        self.products_controller = products_controller
        self.table_controller = table_controller
        self.title(table_id)
        self.geometry('800x400')
        self.table_id = table_id

        self.table = self.table_controller.table_service.tables_repo.find_by_id(table_id)

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Create TreeView

        self.tree = ItemList(self.frame, list(self.table.products), ('id','name', 'price', 'qunatity', 'type'))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)



        tk.Button(self, text='Add product',
                  command=lambda: ProductsView(self,self.table_id, self.table_controller,
                                               self.products_controller)).grid()

        tk.Button(self, text='Get Bill',
                  command=lambda: [self.invoice_controller.get_the_bill(table_id), self.destroy(), self.parent.show_tables()]).grid()
        tk.Button(self, text='Make invoice',
                  command= lambda : [self.invoice_controller.get_the_invoice(table_id), self.destroy(), self.parent.show_tables()]).grid()

        if self.user.role == 'Manager':
            tk.Button(self, text= 'Delete product', command = lambda : self.del_prod_from_table()).grid()

            # Modal dialog
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def dismiss(self):
        self.grab_release()
        self.destroy()

    def del_prod_from_table(self):
        self.products_controller.save()
        self.products_controller.load()
        items = None
        items = self.tree.get_selected_tems()
        #print(items)
        for item in items:
            try:
                name = int(item[0])
            except Exception:
                name = item[0]
            # print(idx)
            # print()
            prod = self.products_controller.find_by_id(name)
            self.table_controller.delete_product(self.table_id, name)
            #print(prod)
            return self.refresh()

    def refresh(self):
        self.products_controller.load()
        return ItemList(self.frame, list(self.table.products),('id','name', 'price', 'qunatity', 'type'))
