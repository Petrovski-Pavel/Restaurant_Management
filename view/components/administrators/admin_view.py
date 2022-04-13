from tkinter import ttk, Tk
import tkinter as tk

from Entities.users import Administrator, Waiter, Manager
from controller.product_controller import ProductController
from controller.users_controller import UserController
from util.tk_utils import center_resize_window
from view.components.administrators.stored import Stored


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

        #Loading Repos
        self.user_controller.load()
        self.product_controller.load()


        self.list_users = tk.Button(self, text='Show all staff.',width=10, height=2 ,bg='white',command=lambda: Stored(self, self.user_controller, ['Name', 'Role', 'Key']))
        #self.list_users.grid(row=1, column=0, sticky=tk.SE)
        self.list_users.pack(anchor='center')
        self.list_products = tk.Button(self, text='Show all products',width=15, height=2,bg='white', command=lambda : Stored(self,self.product_controller, ['Name', 'Price', 'Quantity', 'Type']))
        #self.list_products.grid(row=1, column=2, sticky=tk.SW)
        self.list_products.pack(anchor='center')











