from tkinter import ttk
import tkinter as tk

from controller.product_controller import ProductController
from controller.table_controller import TableController


class ProductsView(tk.Toplevel):
    def __init__(self, parent, table_id, tables_controller: TableController, products_controller: ProductController):
        super().__init__(parent)
        self.parent = parent


        self.products_controller = products_controller
        self.tables_controller = tables_controller
        self.tables_repo = self.tables_controller.table_service.tables_repo

        self.title('All products')
        self.geometry('800x400')

        self.tree = self.create_tree_widget()

        entry_frame = tk.Frame()
        entry_frame.grid()
        product_name_entry = tk.Entry(self)
        product_name_entry.grid()
        tk.Button(self, text='Add product', command=lambda : [self.tables_controller.add_product(table_id, product_name_entry.get()), self.parent.create_tree_widget(table_id)]).grid()

    def create_tree_widget(self):
        self.products_controller.load()

        columns = ('name', 'price', 'quantity')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('name', text='Name')
        tree.heading('price', text='Price')
        tree.heading('quantity', text='Quantity')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        for prod in self.products_controller.product_service.products_repository:
            tree.insert('', tk.END, values=(prod.name, prod.price, prod.quantity))

        return tree

