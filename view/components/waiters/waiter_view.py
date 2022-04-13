import functools
import tkinter as tk
from tkinter import ttk

from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController
from controller.users_controller import UserController

# from view.components.main_view import MainView
from view.components.waiters.table_view import TableView


class WaiterView(tk.Toplevel):
    MAXBUTT=3
    def __init__(self, parent, user_controller: UserController, table_controller: TableController,
                 products_controller: ProductController, invoice_controller, user):
        super().__init__(parent)
        self.geometry('375x150')
        self.title(f'Waiter {user.name}')

        self.invoice_controller = invoice_controller
        self.product_controller = products_controller
        self.table_controller = table_controller
        self.user_controller = user_controller
        self.user = user

        #Load
        self.user_controller.save()
        #self.user_controller.load()
        self.product_controller.load()

        #Get all tables
        for table in self.user.tables:
            print(table)
        self.tables = self.show_tables()

        self.table_num_label = ttk.Label(self, text='Table Number')
        self.table_num_label.grid(row=0, column=0)

        self.table_num = ttk.Entry(self)
        self.table_num.grid(row=1, column=0)

        self.open_table_button = ttk.Button(self, text='Add Table', command=lambda: [
            self.user_controller.open_table(user.password, int(self.table_num.get())), self.show_tables()])

        self.open_table_button.grid(row=2, column=0)

        # self.root.mainloop()

    def show_tables(self):

        for slave in self.grid_slaves():
            if slave == self.open_table_button or slave == self.table_num_label or slave == self.table_num:
                pass
            else:
                slave.destroy()
        row = 0
        column = 1
        for idx, tb in enumerate(self.user.tables):
            if idx!= 0 and idx % self.MAXBUTT == 0:
                column=1
                row+=1
            self.table_buttn = ttk.Button(self, text=tb, command=functools.partial(self.create_table_view,tb))
            self.table_buttn.grid(row=row, column=column)
            column += 1

    def create_table_view(self, table_id):
        TableView(self, table_id, self.table_controller, self.product_controller, self.invoice_controller, self.user)