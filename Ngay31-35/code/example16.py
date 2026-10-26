"""
Phương thức đặc biệt (Magic method)
Nếu muốn đưa đối tượng tự định nghĩa vào set hoặc dùng làm khóa của dict,
thì bắt buộc phải ghi đè hai phương thức đặc biệt __hash__ và __eq__.
Cái trước dùng để tính mã băm của đối tượng, cái sau dùng để kiểm tra hai đối tượng có giống nhau hay không.
Các đối tượng có mã băm khác nhau chắc chắn là đối tượng khác nhau, nhưng mã băm giống nhau chưa chắc là cùng một đối tượng (xung đột mã băm).
Vì vậy khi mã băm giống nhau, cần dựa vào __eq__ để xác định đối tượng có bằng nhau hay không.
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, 'Vương Đại Chùy'))
    # students.add(Student(1001, 'Vương Đại Chùy'))
    # students.add(Student(1001, 'Bạch Nguyên Phương'))
    # print(len(students))
    # print(students)
    stu = Student(1234, 'jackfrued')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('Qianfeng Education')
    school[1001] = Student(1001, 'Vương Đại Chùy')
    school[1002] = Student(1002, 'Bạch Nguyên Phương')
    school[1003] = Student(1003, 'Bạch Khiết')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()

