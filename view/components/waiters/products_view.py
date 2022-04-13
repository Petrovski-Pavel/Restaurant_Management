from tkinter import ttk
import tkinter as tk

from controller.product_controller import ProductController
from controller.table_controller import TableController
from view.components.item_list import ItemList


class ProductsView(tk.Toplevel):
    def __init__(self, parent, table_id, tables_controller: TableController, products_controller: ProductController):
        super().__init__(parent)
        self.parent = parent
        self.table_id = table_id


        self.products_controller = products_controller
        self.tables_controller = tables_controller
        self.table = self.tables_controller.find_by_id(table_id)
        #self.tables_repo = self.tables_controller.table_service.tables_repo

        #Load Controllers
        self.products_controller.load()

        self.title('All products')
        self.geometry('800x450')

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Create TreeView

        self.tree = ItemList(self.frame, list(self.products_controller.find_all()))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        entry_frame = tk.Frame()
        entry_frame.grid()
        product_name_entry = tk.Entry(self)
        product_name_entry.grid()


        tk.Button(self, text='Add', command = self.add_prod).grid()
        tk.Button(self, text='Add product by name', command=lambda : [self.tables_controller.add_product_by_name(table_id, product_name_entry.get()), self.refresh()]).grid()

    def add_prod(self):
        self.products_controller.save()
        self.products_controller.load()
        items = None
        items = self.tree.get_selected_tems()
        # print(items)
        for item in items:
            try:
                idx = int(item[0])
            except Exception:
                idx = item[0]
            # print(idx)
            # print()
            prod = self.products_controller.find_by_id(idx)
            self.tables_controller.add_product_by_id(self.table_id, idx)
            #print(prod)
            return self.refresh()



    def refresh(self):
        self.products_controller.load()
        return ItemList(self.parent.frame, list(self.table.products), ('id','name', 'price', 'qunatity', 'type'))

