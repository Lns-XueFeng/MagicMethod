class AddDescr:
    LNS = "Lns-"

    def __str__(self):
        return f"{self.__class__.__name__}: Add Some..."

    def __call__(self, func):
        def add_name():
            def add_li(*args, **kwargs):
                return self.LNS + func()
            return add_li
        return add_name()


@AddDescr()
def show_name():
    return "XueFeng"


print(show_name)
print(show_name())
