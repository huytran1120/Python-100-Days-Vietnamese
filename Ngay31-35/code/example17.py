"""
Đa kế thừa - Một lớp có từ hai lớp cha trở lên
MRO - Thứ tự phân giải phương thức - Method Resolution Order
Khi xuất hiện kế thừa hình thoi (kế thừa kim cương), lớp con kế thừa phương thức của lớp cha nào
Python 2.x - Tìm kiếm theo chiều sâu (DFS)
Python 3.x - Thuật toán C3 - Tương tự như tìm kiếm theo chiều rộng (BFS)
"""
class A():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """Mixin tự định nghĩa"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """Dict tự định nghĩa"""
    pass


def main():
    print(D.mro())
    # print(D.__mro__)
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict= SetOnceDict()
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    main()
