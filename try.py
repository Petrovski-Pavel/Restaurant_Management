import tkinter as tk
#from tkinter import Tk

from tkinter import PhotoImage
from PIL import ImageTk, Image


from Entities.users import Waiter, Manager, Administrator
from Repository.id_gen_int import IdGenerator, IdGeneratorProd
from Repository.id_generator_uuid import IdGeneratorUuid
from Repository.invoicing_repository import InvoiceRepository
from Repository.products_repository import ProductsRepository
from Repository.table_repository import TableRepository
from Repository.user_repository import UserRepository
from controller.invoice_controller import InvoiceController
from controller.product_controller import ProductController
from controller.table_controller import TableController
from controller.users_controller import UserController
from service.invoice_service import InvoiceService
from service.products_service import ProductsService
from service.table_service import TableService
from service.user_service import UserService
from util.tk_utils import center_resize_window

from view.components.main_view import MainView


class TablesRepository:
    pass


if __name__ == "__main__":
    root = tk.Tk()
    center_resize_window(root, 300, 300)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    image1 = Image.open("pizza_label.png")
    image1 = image1.resize((150, 150))
    test = ImageTk.PhotoImage(image1)

    image1 = Image.open("pizza_label_2.png")
    image1 = image1.resize((150, 150))
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test

    # Position image
    label1.place(relx=0.5, rely=0.5, anchor='center')

    #Configure doamin repos and services
    # p1 = Waiter('Ivan', 1200)
    # p2 = Manager('Dimitar', 1300)
    # p3 = Administrator('Mariya', 1400)
    # persons = [p1, p2, p3]

    id_gen = IdGeneratorUuid()
    #id_gen_prod = IdGeneratorProd()

    persons_repo = UserRepository(id_gen, 'users_database.json')
    persons_repo.load()

    #
    # for p in persons:
    #     persons_repo.create(p)


    tables_repo = TableRepository()
    products_repo = ProductsRepository(id_gen, 'products_db.json')
    products_repo.load()

    invoice_repo = InvoiceRepository()
    invoice_service = InvoiceService(tables_repo, invoice_repo, persons_repo)
    invoice_controller = InvoiceController(invoice_service)


    products_service = ProductsService(products_repo)
    products_controller = ProductController(products_service)

    user_service = UserService(persons_repo, tables_repo)
    user_controller = UserController(user_service)

    table_serivce = TableService(tables_repo, products_repo)
    table_controller = TableController(table_serivce)

    main_view = MainView(root, user_controller, table_controller, products_controller, invoice_controller)

    # Start the app event loop
    root.mainloop()
