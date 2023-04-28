"""
Use @property decorators to create read-only properties,
@property decorator converts the method to a read-only property of the same name
"""


class Model:
    def __init__(self, password):
        # This property has two setting
        # the one is set it can read-only, the other can set it when it is assigned
        self.password = password


class User(Model):
    __password_hash = ''

    @property
    def password(self):
        """ This function is a read-only property """
        return self.__password_hash

    @password.setter
    def password(self, plain_text_password):
        """ What to do before getting the password attribute """
        self.__password_hash = hex(int(plain_text_password))


if __name__ == "__main__":
    user = User("123456")   # In fact, we usually write 'form.password.data' like this
    print(user.password)
