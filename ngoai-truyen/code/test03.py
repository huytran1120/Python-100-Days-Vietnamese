from random import randint, sample

# Khởi tạo danh sách bóng đỏ dự tuyển
red_balls = [x for x in range(1, 34)]
# Chọn ra 6 bóng đỏ
selected_balls = sample(red_balls, 6)
# Sắp xếp bóng đỏ
selected_balls.sort()
# Thêm 1 bóng xanh
selected_balls.append(randint(1, 16))
# In ra các số ngẫu nhiên đã chọn
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()