class Object:
    def __init__(self):
        self.counter = 0

    def __getattr__(self, attr):
        """ Called when an instance object attempts to access a property that does not exist """
        return "No This Attribute"

    def __getattribute__(self, attr):
        """ This magic method is called whenever the properties of the instance object are accessed """
        if attr == "data":
            self.counter += 1
        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        """ Called when attribute is set (including modification) """
        print(f"set: {attr}: {value}")
        super().__setattr__(attr, value)

    def __delattr__(self, attr):
        """ Called when attempting to delete a property with the keyword 'del' """
        print(f"del {attr}")
        super().__delattr__(attr)


class A:
    def __init__(self):
        self.val = 0

    def __get__(self, instance, owner=None):
        return self.val

    def __set__(self, instance, value):
        self.val = value

    def __delete__(self, instance):
        print("[del b.a] delete a.val")


class B:
    a = A()


b = B()
print(f"[b.a get a.val] get {b.a}")
b.a = 1
print(f"[b.a=1 set a.val=1] a.val: {b.a}")
del b.a
print("-----------------------")


if __name__ == "__main__":
    obj = Object()
    print(obj.test)
    print(obj.data)
    print(obj.data)
    print(f"attr `data` counter: {obj.counter}")
    del obj.counter
