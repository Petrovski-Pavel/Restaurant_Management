from tkinter import ttk
import tkinter as tk

from Entities.users import Waiter, Administrator, Manager
from controller.users_controller import UserController


class UsersStored(tk.Toplevel):
    def __init__(self, parent, users_controller: UserController):
        super().__init__(parent)
        self.users_controller = users_controller
        self.parent = parent

        self.title('All users')
        self.geometry('800x400')

        self.tree = self.create_tree_widget()

        self.create_user = tk.Button(self, text='Add staff', command=lambda: Entries(self, self.users_controller))
        self.create_user.grid(row=1, column=0)

        self.delete_butt = tk.Button(self, text='Delete', command=lambda : self.delete()).grid()


    def create_tree_widget(self):
        self.users_controller.save()
        self.users_controller.load()

        columns = ('id', 'name','role', 'key')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('id', text='ID')
        tree.heading('name', text='Name')
        tree.heading('role', text='Role')
        tree.heading('key', text='Key')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        for person in self.users_controller.user_service.users_repo:
            tree.insert('', tk.END, values=(person.id, person.name,person.role, person.password))

        return tree

    def delete(self):
        # Get selected item to Delete
        selected_item = self.tree.selection()
        print(selected_item)
        self.tree.delete(selected_item)

class Entries(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.user_controller = controller
        self.parent = parent
        self.entries = []
        self.labels = ['Name','Role', 'Key']


        for i in range(3):
            my_label = tk.Label(self,text=self.labels[i])
            my_label.grid(row=i, column=0)
            my_entry = tk.Entry(self)
            my_entry.grid(row=i, column=1)
            self.entries.append(my_entry)

        self.create_butt = tk.Button(self, text= 'Create', command = lambda: [self.submit(), self.parent.create_tree_widget()])
        self.create_butt.grid(row=4, column=1)

        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def dismiss(self):
        self.grab_release()
        self.destroy()


    def submit(self):
        if self.entries[1].get() == 'Waiter':
            wt = Waiter(self.entries[0].get(), int(self.entries[2].get()))
            self.user_controller.add_new_staff(wt)
            self.destroy()
        elif self.entries[1].get() == 'Administrator':
            wt = Administrator(self.entries[0].get(), int(self.entries[2].get()))
            self.user_controller.add_new_staff(wt)
            self.destroy()

        elif self.entries[1].get() == 'Manager':
            wt = Manager(self.entries[0].get(), int(self.entries[2].get()))
            self.user_controller.add_new_staff(wt)
            self.destroy()



