"""
Thuật toán tham lam: Khi giải quyết vấn đề, luôn đưa ra lựa chọn tốt nhất ở thời điểm hiện tại,
không theo đuổi lời giải tối ưu, nhanh chóng tìm ra lời giải thỏa đáng.
"""
class Thing(object):
    """Vật phẩm"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """Tỷ số giá / trọng lượng"""
        return self.price / self.weight


def input_thing():
    """Nhập thông tin vật phẩm"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """Hàm chính"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'Tên trộm đã lấy đi {thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'Tổng giá trị: {total_price} USD')


if __name__ == '__main__':
    main()
