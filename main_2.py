from Entities.invoice import Invoicing, Bill, Invoice
from Entities.products import Beverage, Dish, Product
from Entities.table import Table
from Entities.users import Waiter, Administrator, Manager, Users
from Repository.id_gen_int import IdGenerator, IdGeneratorProd
from Repository.invoicing_repository import InvoiceRepository
from Repository.products_repository import ProductsRepository
from Repository.table_repository import TableRepository
from Repository.user_repository import UserRepository
from service.invoice_service import InvoiceService
from service.table_service import TableService
from service.user_service import UserService


def print_all(repo):
    print()
    it2 = iter(repo)
    try:
        while True:
            p2 = next(it2)
            print(p2.get_formatted())
    except StopIteration:
        pass
    print()


if __name__ == '__main__':

    print('USER SERVICE')

    p1 = Waiter('Ivan', 1200)
    p2 = Manager('Dimitar', 1300)
    p3 = Administrator('Mariya', 1400)
    persons = [p1, p2, p3]

    id_gen = IdGenerator()
    persons_repo = UserRepository(id_gen, 'users_database.json')

    for p in persons:
        persons_repo.create(p)

    tables_repo = TableRepository()

    user_service = UserService(persons_repo, tables_repo)
    waiter, table = user_service.waiter_open_table_by_waiter_key_table_id(1200, 14)
    print(waiter.get_formatted())
    print(table.get_formatted())
    print()

    #
    # user_service.delete_table_by_waiter_key_table_id(1200, 14)
    # print(waiter.get_formatted())


    print('TABLE SERVICE')

    prod1 = Beverage('Wine', 10, 120)
    prod2 = Dish('Margaritta', 15, 800)
    prod3 = Dish('Hawaii', 20, 800)
    prod4 = Beverage('Strawberry Lemonade', 6.50, 300)

    products = [prod1, prod2, prod3, prod4]

    id_gen = IdGeneratorProd()
    products_repo = ProductsRepository(id_gen, 'products_db.json')

    for pr in products:
        products_repo.create(pr)

    for pr in products_repo.find_all():
        print(pr.get_formatted())

    print_all(tables_repo)
    print()
    table_service = TableService(tables_repo, products_repo)
    table = table_service.add_product_by_table_id_and_product_name(14,'Hawaii')
    print(table.get_formatted())
    table = table_service.add_product_by_table_id_and_product_name(14,'Margaritta')
    print(table_service.print_products_table_by_id(14))

    print()
    print(table.get_formatted())

    invoice_repo = InvoiceRepository()
    inv1 = Bill(15000,table)
    invoice_repo.create(inv1)

    # invoice_service = InvoiceService(tables_repo, invoice_repo)
    # invoice_service.get_bill(14)
    # print()
    # print(invoice_repo.income)
    # print(waiter._invoicement)
    # print(waiter.get_formatted())
    # print_all(tables_repo)
    #
    # inv2 = Invoice(16000,table,'Racheti','Ivan Ivanov', '12312412412421')
    # invoice_repo.create(inv2)
    # invoice_service = InvoiceService(tables_repo, invoice_repo)
    # invoice_service.get_invoice(14)

    #print_all(persons_repo)

    # persons_repo.save()
    # persons_repo.load()
    # print('\n', 'After Loading:')
    # print_all(persons_repo.find_all())

    products_repo.save()
    products_repo.load()
    print('\n', 'After Loading: prods_repo')
    print_all(products_repo.find_all())

    #
    tables_repo.save()
    tables_repo.load()
    print('\n', 'After Loading: tables_repo')
    print_all(tables_repo.find_all())


    #
    # invoice_repo.save()
    # invoice_repo.load()
    # print('\n', 'After Loading: inv_repo')
    # print_all(invoice_repo.find_all())



