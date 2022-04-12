from Entities.products import Beverage, Dish

from tkinter import ttk
import tkinter as tk

from Entities.users import Waiter, Administrator, Manager



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

        elif self.entries[-1].get() == 'Beverage':
            pr = Beverage(self.entries[0].get(), float(self.entries[1].get()), float(self.entries[2].get()))
            self.controller.add_new_product(pr)
            self.destroy()

        elif self.entries[-1].get() == 'Dish':
            pr = Dish(self.entries[0].get(), float(self.entries[1].get()), float(self.entries[2].get()))
            self.controller.add_new_product(pr)
            self.destroy()