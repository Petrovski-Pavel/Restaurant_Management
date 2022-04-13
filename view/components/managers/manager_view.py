import functools
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController
from controller.users_controller import UserController
from view.components.waiters.table_view import TableView


class ManagerView(tk.Toplevel):
    def __init__(self, parent, user_controller: UserController, table_controller: TableController,
                 products_controller: ProductController, invoice_controller, user):
        super().__init__(parent)

        self.user = user
        self.invoice_controller = invoice_controller
        self.products_controller = products_controller
        self.table_controller = table_controller
        self.user_controller = user_controller


        #Load controllers
        # self.user_controller.save()
        # self.user_controller.load()
        self.products_controller.load()

        #Configure widget
        self.geometry('500x150')
        self.title(f'Manager {user.name}')


        # Adding buttons and labels
        key_label = tk.Label(self, text= "Enter waiter's key").grid(row = 0, column = 0, sticky=tk.NE)
        table_id_label = tk.Label(self, text= "Enter table number").grid(row = 1, column = 0, sticky=tk.NE)
        self.key_entry = tk.Entry(self)
        self.key_entry.grid(row=0, column=1)
        self.table_id_entry = tk.Entry(self)
        self.table_id_entry.grid(row=1, column=1)


        self.show_all_tables_button = tk.Button(self, text='Show all tables', command = lambda : AllTablesView(self, self.table_controller, self.user_controller,self.products_controller, self.invoice_controller))
        self.show_all_tables_button.grid(row=2, column= 0, sticky=tk.E)

        self.get_waiter_invoice_button = tk.Button(self, text='Get waiter finances', command = lambda : [print(self.user_controller.get_waiter_invoice(self.get_entry(self.key_entry)))])
        self.get_waiter_invoice_button.grid(row=2, column= 1, sticky=tk.E)

        self.get_waiter_invoice_button = tk.Button(self, text='Get total finances', command = lambda : print(self.invoice_controller.get_financial_statement()))
        self.get_waiter_invoice_button.grid(row=2, column= 2, sticky=tk.E)

        self.delete_table_button = tk.Button(self, text = 'Delete table', command = lambda: self.table_controller.delete_table(self.get_entry(self.table_id_entry))).grid()

        # for table in self.table_controller.find_all():
        #     print(table)

    def get_entry(self, entry):
        try:
            self.entry = int(entry.get())
            return self.entry
        except ValueError as ex:
            messagebox.showerror(title='Error', message='Input must be digits.')


class AllTablesView(tk.Toplevel):
    def __init__(self, parent, tables_controller: TableController, users_controller: UserController, products_controller: ProductController, invoice_controller: InvoiceController):
        super().__init__(parent)

        self.parent = parent
        self.invoice_controller = invoice_controller
        self.products_controller = products_controller
        self.users_controller = users_controller
        self.tables_controller = tables_controller

        self.geometry('500x150')
        self.title(f'All tables')

        self.tables = self.show_tables()


    def show_tables(self):
        for slave in self.grid_slaves():
            slave.destroy()

        for idx, tb in enumerate(self.tables_controller.find_all()):
            #obj = TableView(self, tb, self.table_controller, self.product_controller, self.invoice_controller)
            self.table_buttn = ttk.Button(self, text=tb._id, command=functools.partial(self.create_table_view,tb._id))
            self.table_buttn.grid(row=0, column=idx)

    def create_table_view(self, table_id):
        TableView(self, table_id, self.tables_controller, self.products_controller, self.invoice_controller, self.parent.user)
