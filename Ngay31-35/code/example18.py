"""
Meta
Metadata - Dữ liệu mô tả dữ liệu
Metaclass - Lớp mô tả lớp - Kế thừa từ type
"""
import threading


class SingletonMeta(type):
    """Metaclass tự định nghĩa"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """Tổng thống (Lớp Singleton)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """Hàm chính"""
    p1 = President('Trump', 'Mỹ')
    p2 = President('Obama', 'Mỹ')
    p3 = President.__call__('Clinton', 'Mỹ')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()
