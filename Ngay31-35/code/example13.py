from example12 import EmployeeFactory


def main():
    """Hàm chính"""
    emps = [
        EmployeeFactory.create('M', 'Tào Tháo'), 
        EmployeeFactory.create('P', 'Tuân Úc', 120),
        EmployeeFactory.create('P', 'Quách Gia', 85), 
        EmployeeFactory.create('S', 'Điển Vi', 123000),
    ]
    for emp in emps:
        print('%s: %.2f đồng' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
