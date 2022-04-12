from tkinter import ttk
import tkinter as tk

from Entities.users import Waiter, Administrator, Manager
from controller.users_controller import UserController
from view.components.administrators.entries import Entries
from view.components.administrators.item_list import ItemList


class Stored(tk.Toplevel):
    def __init__(self, parent, controller, entry_labels):
        super().__init__(parent)
        self.entry_labels = entry_labels
        self.controller = controller
        self.parent = parent

        self.title = self.parent.title
        self.geometry('700x400')

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky = tk.NSEW)

        #Create TreeView
        self.tree = ItemList(self.frame, list(self.controller.find_all()))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Buttons
        self.create_user = tk.Button(self, text='Add staff', command=lambda: Entries(self, self.controller, self.entry_labels))
        self.create_user.grid(row=1, column=0)

        self.delete_butt = tk.Button(self, text='Delete', command=lambda: self.delete())
        self.delete_butt.grid()



    def delete(self):
        self.controller.save()
        self.controller.load()
        items = None
        items = self.tree.get_selected_tems()
        print(items)
        for item in items:
            idx = item[0]
            if type(idx) == int:
                idx = int(idx)
            #print(idx)
            #print(self.users_controller.user_service.users_repo.find_by_id(idx))
            #print(self.controller.find_by_id(idx))
            print()
            self.controller.delete_by_id(idx)

        return self.refresh()


    def refresh(self):
        self.controller.load()
        return ItemList(self.frame, list(self.controller.find_all()))


