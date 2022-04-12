from tkinter import ttk
import tkinter as tk

from Entities.users import Waiter, Administrator, Manager
from controller.users_controller import UserController
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

        self.tree = ItemList(self.frame, list(self.users_controller.user_service.users_repo.find_all()))
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
            self.users_controller.delete_staff_id(idx)

        return self.refresh()


    def refresh(self):
        self.users_controller.load()
        return ItemList(self.frame, list(self.users_controller.user_service.users_repo.find_all()))





class Entries(tk.Toplevel):
    def __init__(self, parent, controller, labels: list):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.entries = []

        self.labels = labels


        for i in range(len(labels)):
            my_label = tk.Label(self,text=self.labels[i])
            my_label.grid(row=i, column=0)
            my_entry = tk.Entry(self)
            my_entry.grid(row=i, column=1)
            self.entries.append(my_entry)

        self.create_butt = tk.Button(self, text= 'Create', command = lambda: [self.submit(), self.parent.refresh()])
        self.create_butt.grid(row=4, column=1)

        #Modeled
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
            self.controller.add_new_staff(wt)
            self.destroy()
        elif self.entries[1].get() == 'Administrator':
            wt = Administrator(self.entries[0].get(), int(self.entries[2].get()))
            self.controller.add_new_staff(wt)
            self.destroy()

        elif self.entries[1].get() == 'Manager':
            wt = Manager(self.entries[0].get(), int(self.entries[2].get()))
            self.controller.add_new_staff(wt)
            self.destroy()
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