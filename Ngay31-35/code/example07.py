"""
Bản tóm lược băm (Hash digest) - Chữ ký số / Dấu vân tay số - Hàm băm một chiều (không thể đảo ngược)
Lĩnh vực ứng dụng:
1. Lưu thông tin nhạy cảm của người dùng trong cơ sở dữ liệu dưới dạng mã băm
2. Tạo chữ ký cho dữ liệu để xác minh dữ liệu không bị sửa đổi trái phép
3. Tính năng tải lên tức thì (chống trùng lặp dữ liệu) của dịch vụ lưu trữ đám mây
"""


class StreamHasher():
    """Bộ tạo bản tóm lược băm"""

    def __init__(self, algorithm='md5', size=4096):
        """Phương thức khởi tạo
        @params:
            algorithm - Thuật toán hàm băm
            size - Kích thước dữ liệu đọc mỗi lần
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """Tạo chuỗi tóm lược băm ở hệ thập lục phân (hex digest)"""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """Hàm chính"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
