# # import tkinter as tk
# # from tkinter import ttk
# #
# # from Entities.products import Product
# # from Entities.table import Table
# # from Entities.users import Waiter
# # from Repository.id_gen_int import IdGeneratorProd
# # from Repository.products_repository import ProductsRepository
# #
# #
# # class TableView(tk.Tk):
# #     def __init__(self, products_repository: ProductsRepository):
# #         super().__init__()
# #
# #         self.products_repository = products_repository
# #         self.title('Items')
# #         self.geometry('620x200')
# #         self.columns = ('name', 'price', 'quantity')
# #         self.tree = self.create_tree_widget()
# #
# #     def create_tree_widget(self):
# #
# #         columns = ('name', 'price', 'quantity')
# #
# #         tree = ttk.Treeview(self, columns=columns, show='headings')
# #
# #         #define headings
# #         tree.heading('name', text='Name')
# #         tree.heading('price',text='Price')
# #         tree.heading('quantity',text='Quantity')
# #
# #         tree.grid(row=0, column=0, sticky=tk.NSEW)
# #
# #         # adding an item
# #         for prod in self.products_repository:
# #
# #             tree.insert('', tk.END, values=(prod.name, prod.price, prod.quantity))
# #
# #         # # insert a the end
# #         # tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))
# #         #
# #         # # insert at the beginning
# #         # tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))
# #
# #         return tree
# #
# #
# # # class ProductsOnTAble(App):
# # #     def __init__(self, products_repository: ProductsRepository):
# # #         super().__init__(products_repository)
# # #         self.top = tk.Toplevel()
# # #         self.title('prods')
# # #         columns = self.columns
# # #         self.create_tree_widget(columns)
# # #
# # #         tk.Button(self.top, text = 'Add', command=App(self.products_repository))
# #
# #
# #
# #
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     id_gen = IdGeneratorProd()
# #     products_repository = ProductsRepository(id_gen, 'products_db.json')
# #     products_repository.load()
# #
# #     app = TableView(products_repository)
# #     # prods_table = ProductsOnTAble(products_repository)
# #     app.mainloop()
# #
# import tkinter as tk
# from tkinter import ttk
#
#
# class Window(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         self.geometry('300x100')
#         self.title('Toplevel Window')
#
#         ttk.Button(self,
#                 text='Close',
#                 command=self.destroy).pack(expand=True)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.geometry('300x200')
#         self.title('Main Window')
#
#         # place a button on the root window
#         ttk.Button(self,
#                 text='Open a window',
#                 command=self.open_window).pack(expand=True)
#
#     def open_window(self):
#         window = Window(self)
#         window.grab_set()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Company")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('1', 'Honda'))
tree.insert('', 'end', text="2", values=('2', 'Hyundai'))
tree.insert('', 'end', text="3", values=('3', 'Tesla'))
tree.insert('', 'end', text="4", values=('4', 'Wolkswagon'))
tree.insert('', 'end', text="5", values=('5', 'Tata Motors'))
tree.insert('', 'end', text="6", values=('6', 'Renault'))

tree.pack()

def edit():
   # Get selected item to Edit
   selected_item = tree.selection()
   print(selected_item)
   tree.item(selected_item, text="blub", values=("foo", "bar"))

def delete():
   # Get selected item to Delete
   selected_item = tree.selection()
   print(selected_item)
   tree.delete(selected_item)

# Add Buttons to Edit and Delete the Treeview items
edit_btn = ttk.Button(win, text="Edit", command=edit)
edit_btn.pack()
del_btn = ttk.Button(win, text="Delete", command=delete)
del_btn.pack()

win.mainloop()