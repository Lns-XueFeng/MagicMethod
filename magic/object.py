class Object:
    def __init__(self):
        self.counter = 0

    def __getattr__(self, attr):
        """ 当实例对象试图访问一个不存在的属性时被调用 """
        return "No This Attribute"

    def __getattribute__(self, attr):
        """ 实例对象只要访问了属性它均会被调用 """
        if attr == "data":
            self.counter += 1
        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        """ 当设置attribute时被调用(包括修改) """
        print(f"set: {attr}: {value}")
        super().__setattr__(attr, value)

    def __delattr__(self, attr):
        """ 当试图用关键字del删除一个属性时被调用 """
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
