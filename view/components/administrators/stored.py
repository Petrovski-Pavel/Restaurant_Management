from tkinter import ttk
import tkinter as tk

from view.components.administrators.entries import Entries
from view.components.item_list import ItemList


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
        self.create_user = tk.Button(self, text='Add',width=8,height=3,bg='green', command=lambda: Entries(self, self.controller, self.entry_labels))
        self.create_user.grid(pady=10, padx=2)

        self.delete_butt = tk.Button(self, text='Delete',width=8,height=3,bg='red', command=lambda: self.delete())
        self.delete_butt.grid(pady=15, padx=3)

        # Modal dialog
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def dismiss(self):
        self.grab_release()
        self.destroy()

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


