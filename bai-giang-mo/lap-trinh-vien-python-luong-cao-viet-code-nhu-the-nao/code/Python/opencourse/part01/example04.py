from random import randint, sample


def generate():
    """Tạo một bộ số ngẫu nhiên"""
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def display(balls):
    """Xuất một bộ số xổ số hai màu (bóng đỏ và xanh)"""
    for index, ball in enumerate(balls):
        print(f'{ball:0>2d}', end=' ')
        if index == len(balls) - 2:
            print('|', end=' ')
    print()


num = int(input('Chọn ngẫu nhiên bao nhiêu vé: '))
for _ in range(num):
    display(generate())
