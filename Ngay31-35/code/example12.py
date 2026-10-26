"""
Ba trụ cột của hướng đối tượng: Đóng gói, Kế thừa, Đa hình
Nguyên tắc thiết kế hướng đối tượng: Nguyên tắc SOLID
Mẫu thiết kế hướng đối tượng: Mẫu thiết kế GoF (Singleton, Factory, Proxy, Strategy, Iterator)
Hệ thống tính lương tháng - Trưởng phòng 15000/tháng, Lập trình viên 200/giờ, Nhân viên kinh doanh 1800 lương cứng cộng 5% hoa hồng doanh số
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """Nhân viên (lớp trừu tượng)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """Tính lương tháng (phương thức trừu tượng)"""
        pass


class Manager(Employee):
    """Trưởng phòng"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """Lập trình viên"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """Nhân viên kinh doanh"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """Factory tạo nhân viên (Factory pattern - giảm liên kết giữa nơi sử dụng và đối tượng)"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """Tạo nhân viên"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
