# from Entities.invoice import Invocing, Bill, Invoice
# from Entities.products import Beverage, Dish, Product
# from Entities.table import Table
# from Entities.users import Waiter, Administrator, Manager, Users
# from Repository.id_gen_int import IdGenerator, IdGeneratorProd
# from Repository.invoicing_repository import InvoiceRepository
# from Repository.products_repository import ProductsRepository
# from Repository.table_repository import TableRepository
# from Repository.user_repository import UserRepository
#
#
# def print_all(repo):
#     print()
#     it2 = iter(repo)
#     try:
#         while True:
#             p2 = next(it2)
#             print(p2.get_formatted())
#     except StopIteration:
#         pass
#     print()
#
# if __name__ == '__main__':
#     print("USERS")
#
#     p1 = Waiter('Ivan', 1200)
#     p2 = Manager('Dimitar', 1300)
#     p3 = Administrator('Mariya', 1400)
#     persons = [p1, p2, p3]
#
#     id_gen = IdGenerator()
#     persons_repo = UserRepository(id_gen)
#
#     for p in persons:
#         persons_repo.create(p)
#
#     for p in persons_repo.find_all():
#         print(p.get_formatted())
#
#     second: Users = persons_repo.find_by_name('Dimitar')
#     second.role = 'Administrator'
#
#     third: Users = persons_repo.find_by_id(1)
#     third.name = 'Georgi'
#
#     persons_repo.update(third)
#     persons_repo.update(second)
#     print_all(persons_repo)
#
#     persons_repo.create(Waiter('Ralica', 1201))
#     print_all(persons_repo)
#
#     persons_repo.delete_by_id(2)
#     print_all(persons_repo)
#
#     persons_repo.delete_by_name('Georgi')
#     print_all(persons_repo)
#
#     persons_repo.delete_by_key(1201)
#     print_all(persons_repo)
#
#     other_repo = UserRepository(id_gen)
#     other_repo.create(Waiter('John', 1202))
#     other_repo.create(Manager('Jordan', 1302))
#     print_all(other_repo)
#
#     persons_repo += other_repo
#     print_all(persons_repo)
#
#
#     print('PRODUCTS')
#
#
#     prod1 = Beverage('Wine', 10, 120)
#     prod2 = Dish('Margaritta', 15, 800)
#     prod3 = Dish('Hawaii', 20, 800)
#     prod4 = Beverage('Strawberry Lemonade', 6.50, 300)
#
#     products = [prod1, prod2, prod3, prod4]
#
#     id_gen = IdGeneratorProd()
#     products_repo = ProductsRepository(id_gen)
#
#     for pr in products:
#         products_repo.create(pr)
#
#     for pr in products_repo.find_all():
#         print(pr.get_formatted())
#
#     second: Product = products_repo.find_by_name('Margaritta')
#     second.quantity = 1000
#
#     third: Product = products_repo.find_by_id(101)
#     third.price = 10.50
#
#     print()
#     prods = products_repo.find_by_type('Beverage')
#     for pr in prods:
#         print(pr.get_formatted())
#
#     products_repo.update(third)
#     products_repo.update(second)
#     print_all(products_repo)
#
#     products_repo.create(Dish('Spaghetti Meatballs', 11.99, 430))
#     print_all(products_repo)
#
#     products_repo.delete_by_id(103)
#     print_all(products_repo)
#
#     products_repo.delete_by_name('Wine')
#     print_all(products_repo)
#
#     other_products_repo = ProductsRepository(id_gen)
#     other_products_repo.create(Dish('Spaghetti Trapanese', 13.60, 300))
#     other_products_repo.create(Dish('Caesar salad', 12.30, 350))
#     other_products_repo.create(Beverage('Budweiser', 4.90, 500))
#     print_all(other_products_repo)
#
#     products_repo += other_products_repo
#     print_all(products_repo)
#
#     print("TABLES")
#     t1 = Table(59)
#     t2 = Table(42)
#     t3 = Table(14)
#     tables = [t1, t2, t3]
#
#     tables_repo = TableRepository(None)
#
#     for t in tables:
#         tables_repo.create(t)
#
#     for t in tables_repo.find_all():
#         print(t.get_formatted())
#
#
#     print()
#     second: Table = tables_repo.find_by_id(59)
#
#     tables_repo.update(second)
#     print_all(tables_repo)
#
#     tables_repo.create(Table(61))
#     print_all(tables_repo)
#
#     tables_repo.delete_by_id(42)
#     tables_repo.delete_by_id(14)
#     print_all(tables_repo)
#
#     other_table_repo = TableRepository()
#     other_table_repo.create(Table(14))
#     # other_table_repo.create(Table(14))
#     other_table_repo.create(Table(102))
#     other_table_repo.create(Table(2))
#     print_all(other_table_repo)
#
#     tables_repo += other_table_repo
#     print_all(tables_repo)
#
#     w1 = Waiter('Dancho',1507)
#     w2 = Waiter('Simon', 1506)
#     table1 = Table(6)
#     table2 = Table(7)
#     inv1 = Bill(15000, w1, table1)
#     inv2 = Invoice(16000, w2, table2,'Technopolis','Gerogi Georgiev', 'BG53STSA1634980')
#     invoice_repo = InvoiceRepository()
#     invoice_repo.create(inv1)
#     invoice_repo.create(inv2)
#
#     for inv in invoice_repo.find_all():
#         print(inv.get_formatted())
#
#     created_inv: Invocing = invoice_repo.find_by_id(15000)
#     created_inv.waiter = Waiter('Nikolay',1503)
#     invoice_repo.update(created_inv)
#     print_all(invoice_repo)
#     print()
#     invoice_repo.delete_by_id(15000)
#     print_all(invoice_repo)
#
#
from Entities.users import Waiter, Manager, Administrator
from Repository.id_generator_uuid import IdGeneratorUuid
from Repository.user_repository import UserRepository

# p1 = Waiter('Ivan', 1200)
# p2 = Manager('Dimitar', 1300)
# p3 = Administrator('Mariya', 1400)
# persons = [p1, p2, p3]

id_gen = IdGeneratorUuid()
    #id_gen_prod = IdGeneratorProd()

persons_repo = UserRepository(id_gen, 'users_database.json')
persons_repo.load()
for person in persons_repo.find_all():
    print(person)
print()
# key = int(1301)
# print(persons_repo.find_by_key(key))
# print(persons_repo.delete_by_key(key))
# print()
# for person in persons_repo.find_all():
#     print(person)
#
# # print()
# print(persons_repo.find_by_key(1200))
# print()
# print(persons_repo.delete_by_key(1300))
# print()
# for person in persons_repo.find_all():
#     print(person)
