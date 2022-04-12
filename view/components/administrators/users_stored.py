from tkinter import ttk
import tkinter as tk

from Entities.users import Waiter, Administrator, Manager
from controller.users_controller import UserController
from view.components.administrators.entries import Entries
from view.components.administrators.item_list import ItemList


class UsersStored(tk.Toplevel):
    def __init__(self, parent, users_controller: UserController):
        super().__init__(parent)
        self.users_controller = users_controller
        self.parent = parent

        self.title('All users')
        self.geometry('800x400')

        # self.tree = self.create_tree_widget()
        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        #self.users_controller.load()

        self.tree = ItemList(self.frame, list(self.users_controller.find_all()))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.create_user = tk.Button(self, text='Add staff', command=lambda: Entries(self, self.users_controller, ['Name', 'Role', 'Key']))
        self.create_user.grid(row=1, column=0)

        self.delete_butt = tk.Button(self, text='Delete', command= lambda : self.delete())
        self.delete_butt.grid()



    def delete(self):
        self.users_controller.save()
        self.users_controller.load()
        items = None
        items = self.tree.get_selected_tems()
        print(items)
        for item in items:
            idx = item[0]
            if type(idx) == int:
                idx = int(idx)
            #print(idx)
            #print(self.users_controller.user_service.users_repo.find_by_id(idx))
            print(self.users_controller.find_by_id(idx))
            print()
            self.users_controller.delete_by_id(idx)

        return self.refresh()


    def refresh(self):
        self.users_controller.load()
        return ItemList(self.frame, list(self.users_controller.user_service.users_repo.find_all()))





        # self.parent.refresh()




    # def create_tree_widget(self):
    #     self.users_controller.save()
    #     self.users_controller.load()
    #     self.frame = ttk.Frame(self)
    #     self.frame.grid(row=0, column=0,sticky=tk.NSEW)
    #
    #     columns = ('id', 'name','role', 'key')
    #
    #     tree = ttk.Treeview(self.frame, columns=columns, show='headings',selectmode='extended')
    #
    #     # define headings
    #     tree.heading('id', text='ID')
    #     tree.heading('name', text='Name')
    #     tree.heading('role', text='Role')
    #     tree.heading('key', text='Key')
    #
    #     tree.grid(row=0, column=0, sticky=tk.NSEW)
    #
    #     # adding an item
    #     for person in self.users_controller.user_service.users_repo.find_all():
    #         tree.insert('', tk.END, values=(person.id, person.name, person.role, person.password))
    #
    #     return tree
    # #
    # def get_selected_tems(self):
    #     items = []
    #     print(self.tree.selection())
    #     for sel_item in self.tree.selection():
    #         items.append(self.tree.item(sel_item, 'values'))
    #     print(items)
    #     print(self.tree.selection())
    #     return items
    #