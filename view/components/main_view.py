import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController
from controller.users_controller import UserController
#from view.commands.login_command import LoginCommand
from view.components.administrators.admin_view import AdminView
from view.components.managers.manager_view import ManagerView
from view.components.waiters.waiter_view import WaiterView

class MainView(ttk.Frame):
    def __init__(self, parent, user_controller: UserController, table_controller: TableController, product_controller: ProductController, invoice_controller: InvoiceController):
        super().__init__(parent, padding='3 3 12 12')
        self.invoice_controller = invoice_controller
        self.product_controller = product_controller
        self.user_controller = user_controller
        self.table_controller = table_controller
        self.parent = parent

        img= self.parent.iconbitmap('pizza_icon.ico')


        self.parent.title('Restaurant Managment')
        self.grid(column=0, row=0, sticky=tk.NSEW)



        username_lbl = ttk.Label(text='Username').grid(row=0, column=0)
        password_lbl = ttk.Label(text='Key').grid(row=1, column=0)
        username = ttk.Entry()
        username.grid(row=0, column=1, sticky='WE')
        password = ttk.Entry(show='*')
        password.grid(row=1, column=1, sticky='WE')

        admin = ttk.Button(text='Login as admin', command=lambda : self.check_login(username.get(), password.get(), 'Administrator'))
        manager = ttk.Button(text='Login as manager', command=lambda : self.check_login(username.get(), password.get(), 'Manager'))
        waiter = ttk.Button(text='Login as waiter', command=lambda : self.check_login(username.get(), password.get(), 'Waiter'))
        admin.grid(row=2, column=0)
        manager.grid(row=2, column=1)
        waiter.grid(row=2, column=2)




    def check_login(self, username, key, role):
        try:
            key = int(key)
        except ValueError:
            messagebox.showerror(message='Key must be digits')
        user = self.user_controller.user_service.users_repo.find_by_key(key)
        if user is not None and user.name == username and user.role == role:
            self.logged = True
            if user.role == 'Administrator':
                return AdminView(self, self.user_controller, self.product_controller, user)
            elif user.role == 'Waiter':
                return WaiterView(self, self.user_controller, self.table_controller, self.product_controller, self.invoice_controller, user)
            elif user.role == 'Manager':
                return ManagerView(self, self.user_controller, self.table_controller, self.product_controller, self.invoice_controller, user)
        messagebox.showerror(message='Wrong user credentials')














