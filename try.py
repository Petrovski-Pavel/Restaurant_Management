from tkinter import Tk

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
#from view.commands.login_command import LoginCommand

from view.components.main_view import MainView


class TablesRepository:
    pass


if __name__ == "__main__":
    root = Tk()
    center_resize_window(root, 300, 300)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

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

    invoice_repo = InvoiceRepository()
    invoice_service = InvoiceService(tables_repo, invoice_repo)
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
