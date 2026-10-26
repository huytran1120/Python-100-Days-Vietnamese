"""
Tìm kiếm - Tìm kiếm tuần tự và tìm kiếm nhị phân
Thuật toán: Phương pháp (các bước) giải quyết vấn đề
Đánh giá một thuật toán tốt hay xấu chủ yếu dựa vào hai chỉ số: độ phức tạp thời gian tiệm cận và độ phức tạp không gian tiệm cận; thông thường một thuật toán rất khó đồng thời có cả độ phức tạp thời gian lẫn không gian đều rất thấp (vì thời gian và không gian là hai yếu tố đánh đổi nhau)
Biểu diễn độ phức tạp thời gian tiệm cận thường sử dụng ký hiệu Big-O
O(c): Độ phức tạp thời gian hằng số - Lưu trữ băm (hash storage) / Bloom filter
O(log_2 n): Độ phức tạp thời gian logarit - Tìm kiếm nhị phân
O(n): Độ phức tạp thời gian tuyến tính - Tìm kiếm tuần tự
O(n * log_2 n): - Độ phức tạp thời gian tuyến tính logarit - Thuật toán sắp xếp nâng cao (Merge sort, Quick sort)
O(n ** 2): Độ phức tạp thời gian bậc hai (bình phương) - Thuật toán sắp xếp đơn giản (Bubble sort, Selection sort, Insertion sort)
O(n ** 3): Độ phức tạp thời gian bậc ba (lập phương) - Thuật toán Floyd / Phép nhân ma trận
Cũng được gọi là độ phức tạp thời gian đa thức
O(2 ** n): Độ phức tạp thời gian cấp số nhân - Tháp Hà Nội
O(3 ** n): Độ phức tạp thời gian cấp số nhân
Cũng được gọi là độ phức tạp thời gian hàm mũ
O(n!): Độ phức tạp thời gian giai thừa - Bài toán người bán hàng (TSP) - NP
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """Tìm kiếm tuần tự"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """Tìm kiếm nhị phân"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """Hàm chính (điểm vào của chương trình)"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['Logarit', 'Tuyến tính', 'Tuyến tính logarit', 'Bình phương', 'Lập phương', 'Cấp số nhân', 'Giai thừa']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
