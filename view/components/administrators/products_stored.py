from tkinter import ttk
import tkinter as tk

from controller.product_controller import ProductController


class ProductsStored(tk.Toplevel):
    def __init__(self, parent, products_controller: ProductController):
        super().__init__(parent)
        self.parent = parent

        self.products_controller = products_controller

        self.title('All products')
        self.geometry('800x400')

        self.tree = self.create_tree_widget()

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

