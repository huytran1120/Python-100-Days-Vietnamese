"""
Kiểm thử đơn vị - Kiểm thử nhắm vào mô-đun chức năng nhỏ nhất (hàm và phương thức) trong chương trình
Phương pháp kiểm thử:
- Kiểm thử hộp trắng: Lập trình viên tự viết bài kiểm thử
- Kiểm thử hộp đen: Nhân viên kiểm thử hoặc QA, không biết chi tiết triển khai code, chỉ quan tâm chức năng
Viết kiểm thử đơn vị Python - Định nghĩa lớp kế thừa TestCase, viết phương thức kiểm thử (bắt đầu bằng test_)
Thực thi kiểm thử đơn vị:
- unittest.main()
- python3 -m unittest test_example01.py
Thư viện bên thứ ba - nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Test case kiểm thử các hàm tìm kiếm"""

    # Phương thức thực thi trước mỗi hàm kiểm thử
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # Phương thức thực thi sau mỗi hàm kiểm thử
    def tearDown(self):
        pass

    def test_seq_search(self):
        """Kiểm thử tìm kiếm tuần tự"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """Kiểm thử tìm kiếm nhị phân"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
