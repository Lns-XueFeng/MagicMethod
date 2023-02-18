"""
使用@property装饰器来创建只读属性，
@property装饰器会将方法转换为相同名称的只读属性,
可以与所定义的属性配合使用，这样可以防止属性被修改.
"""


class Model:
    def __init__(self, password):
        self.password = password


class User(Model):
    __password_hash = ''

    @property
    def password(self):
        """ 可使此函数成为一个只读属性 """
        return self.__password_hash

    @password.setter
    def password(self, plain_text_password):
        """ 在得到password属性之前做些什么 """
        self.__password_hash = hex(int(plain_text_password))


if __name__ == "__main__":
    user = User("123456")   # 实际项目中不是明文密码传入：一般为form.password.data
    print(user.password)
