from tkinter import ttk
import tkinter as tk

from Entities.products import Beverage
from controller.product_controller import ProductController
from view.components.administrators.users_stored import Entries


class ProductsStored(tk.Toplevel):
    def __init__(self, parent, products_controller: ProductController):
        super().__init__(parent)
        self.parent = parent

        self.products_controller = products_controller

        self.title('All products')
        self.geometry('800x400')

        self.tree = self.create_tree_widget()

        self.create_prod = tk.Button(self, text='Add to menu',
                                     command=lambda: ProdEntries(self, self.products_controller, ['name', 'price', 'quantity', 'type']))
        self.create_prod.grid(row=1, column=0)

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

class ProdEntries(Entries):
    def __init__(self, parent, controller, labels: list):
        super().__init__(parent, controller, labels)

    def submit(self):
        if self.entries[-1].get() == 'Beverage':
            pr = Beverage(self.entries[0].get(), float(self.entries[1].get()), float(self.entries[2].get()))
            self.controller.add_new_product(pr)

        elif self.entries[-1].get() == 'Dish':
            pr = Beverage()
            self.controller.add_new_product(pr)
        print(pr)
        self.destroy()