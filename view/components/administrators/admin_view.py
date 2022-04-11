from tkinter import ttk, Tk
import tkinter as tk

from Entities.users import Administrator, Waiter, Manager
from controller.product_controller import ProductController
from controller.users_controller import UserController
from util.tk_utils import center_resize_window
from view.components.administrators.products_stored import ProductsStored
from view.components.administrators.users_stored import UsersStored


class AdminView(tk.Toplevel):
    def __init__(self, parent, user_controller: UserController, product_controller: ProductController,
                 user: Administrator):
        super().__init__(parent)
        self.parent = parent
        center_resize_window(self)


        self.geometry('300x100')
        self.title(f'Administrator {user.name}')

        self.user = user
        self.product_controller = product_controller
        self.user_controller = user_controller

        #self.frame = ttk.Frame(self, padding='30 30 12 12')

        self.list_users = tk.Button(self, text='Show all staff.', command=lambda: UsersStored(self, self.user_controller).create_tree_widget())
        self.list_users.grid(row=0, column=0)
        self.list_products = tk.Button(self, text='Show all products', command=lambda : ProductsStored(self,self.product_controller))
        self.list_products.grid(row=0, column=1)












