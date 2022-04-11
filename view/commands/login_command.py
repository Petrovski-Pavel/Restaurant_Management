# from Repository.products_repository import ProductsRepository
# from Repository.user_repository import UserRepository
# from controller.table_controller import TableController
# from controller.users_controller import UserController
# from view.components.admin_view import AdminView
# from view.components.main_view import MainView
# from view.components.waiter_view import WaiterView
#
#
#
#
# class LoginCommand(MainView):
#     def __init__(self, user_repo: UserRepository, user_controller: UserController, parent, login_command: LoginCommand,
#                  table_controller: TableController, product_repo: ProductsRepository):
#         super().__init__(parent, login_command, user_controller, table_controller, product_repo)
#         self.user_controller = user_controller
#         self.user_repo = user_repo
#         self.logged = None
#
#
#     def login(self, username: str, password: int, role):
#         # self.user_repo.load()
#         password = int(password)
#
#         user = self.user_repo.find_by_key(password)
#         if user is not None and user.name == username and user.role == role:
#             self.logged = True
#             if user.role == 'Administrator':
#                 return AdminView(self.user_controller, user)
#             elif user.role == 'Waiter':
#                 return WaiterView(self.user_controller, user)
#         raise Exception('Wrong user credentials')
#
