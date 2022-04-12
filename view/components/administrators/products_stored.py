from tkinter import ttk
import tkinter as tk

from Entities.products import Beverage, Dish
from controller.product_controller import ProductController
from view.components.administrators.entries import Entries
from view.components.administrators.item_list import ItemList


class ProductsStored(tk.Toplevel):
    def __init__(self, parent, products_controller: ProductController):
        super().__init__(parent)
        self.parent = parent

        self.products_controller = products_controller


        self.title('All products')
        self.geometry('800x400')
        #


        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.products_controller.load()

        self.tree = ItemList(self.frame, list(self.products_controller.product_service.products_repository.find_all()))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.create_prd = tk.Button(self, text='Add to menu',
                                     command=lambda: ProdEntries(self, self.products_controller, ['Name', 'Price', 'Quantity', 'Type']))
        self.create_prd.grid(row=1, column=0)

        self.delete_prod = tk.Button(self, text='Delete', command=lambda: self.delete())
        self.delete_prod.grid()

        # self.create_prod = tk.Button(self, text='Add to menu',
        #                              command=lambda: ProdEntries(self, self.products_controller, ['name', 'price', 'quantity', 'type']))
        # self.create_prod.grid(row=1, column=0)

    def delete(self):
        self.products_controller.save()
        self.products_controller.load()

        items = self.tree.get_selected_tems()
        print(items)
        for item in items:
            idx = item[0]
            #print(idx)
            #print(self.users_controller.user_service.users_repo.find_by_id(idx))
            #print(self.products_controller.find_by_id(idx))
            print()
            self.products_controller.delete_by_id(idx)

        return self.refresh()


    def refresh(self):
        self.products_controller.load()
        return ItemList(self.frame, list(self.products_controller.product_service.products_repository.find_all()))

class ProdEntries(Entries):
    def __init__(self, parent, controller, labels: list):
        super().__init__(parent, controller, labels)

    def submit(self):
        if self.entries[-1].get() == 'Beverage':
            pr = Beverage(self.entries[0].get(), float(self.entries[1].get()), float(self.entries[2].get()))
            self.controller.add_new_product(pr)
            self.destroy()

        elif self.entries[-1].get() == 'Dish':
            pr = Dish(self.entries[0].get(), float(self.entries[1].get()), float(self.entries[2].get()))
            self.controller.add_new_product(pr)
            self.destroy()
        print(pr)


# def create_tree_widget(self):
#     self.products_controller.load()
#
#     columns = ('name', 'price', 'quantity')
#
#     tree = ttk.Treeview(self, columns=columns, show='headings')
#
#     # define headings
#     tree.heading('name', text='Name')
#     tree.heading('price', text='Price')
#     tree.heading('quantity', text='Quantity')
#
#     tree.grid(row=0, column=0, sticky=tk.NSEW)
#
#     # adding an item
#     for prod in self.products_controller.product_service.products_repository:
#         tree.insert('', tk.END, values=(prod.name, prod.price, prod.quantity))
#
#     return tree
