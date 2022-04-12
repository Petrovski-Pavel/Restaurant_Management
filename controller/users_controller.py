from Entities.users import Users
from service.user_service import UserService




class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def open_table(self, key, table_id):
        return self.user_service.waiter_open_table_by_waiter_key_table_id(key, table_id)

    def delete_table(self, key, table_id):
        return self.user_service.delete_table_by_waiter_key_table_id(key, table_id)

    def add_new_staff(self, person):
        return self.user_service.add_staff(person)

    def delete_staff_id(self, id):
        return self.user_service.delete_staff_by_id(id)

    def delete_staff_by_key(self, key):
        self.user_service.delete_staff_by_key(key)

    def find_staff(self, key):
        return self.user_service.find_by_key(key)

    def find_by_id(self, id):
        return self.user_service.find_by_id(id)

    def load(self):
        return self.user_service.load()

    def save(self):
        return self.user_service.save()

    def find_all(self):
        return self.user_service.find_all()



    # def show_add_book(self):
    #     form = ItemForm(self.view,
    #                     Users('', ''),
    #                     AddStaffCommand(self))





