"""
Phạm vi biến và thứ tự tìm kiếm biến của Python
LEGB: Local --> Enclosing (Embedded) --> Global --> Built-in
global - khai báo hoặc định nghĩa biến toàn cục (dùng trực tiếp biến toàn cục có sẵn hoặc đặt biến vào phạm vi toàn cục)
nonlocal - khai báo sử dụng biến ở phạm vi lồng nhau (nếu phạm vi lồng nhau không có biến tương ứng sẽ báo lỗi)
"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
