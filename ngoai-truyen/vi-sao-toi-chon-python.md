## Vì sao tôi chọn Python

Hiện tại, đà phát triển của ngôn ngữ Python ở cả trong và ngoài nước đều không thể ngăn cản. Nhờ cú pháp đơn giản, tao nhã cùng hệ sinh thái mạnh mẽ, Python đã nổi bật lên giữa vô vàn ngôn ngữ và hiện đã vững vàng đứng trong top 3 bảng xếp hạng ngôn ngữ lập trình. Rất nhiều nhà phát triển Python trong nước đều chuyển nghề từ Java sang, và bản thân tôi cũng không ngoại lệ. Tôi xin chia sẻ ngắn gọn với các bạn vì sao tôi lại chọn Python.

### Python vs. Java

Chúng ta hãy cùng so sánh qua một vài ví dụ xem khi làm cùng một công việc thì mã nguồn Java và Python được viết như thế nào.

Ví dụ 1: In "hello, world" ra terminal.

Mã nguồn Java:

```Java
class Test {
	
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

Mã nguồn Python:

```Python
print('hello, world')
```

Ví dụ 2: Tính tổng từ 1 đến 100.

Mã nguồn Java:

```Java
class Test {
    
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 100; i += 1) {
            total += i;
        }
        System.out.println(total);
    }
}
```

Mã nguồn Python:

```Python
print(sum(range(1, 101)))
```

Ví dụ 3: Chọn số ngẫu nhiên cho xổ số bóng hai màu.

Mã nguồn Java:

```Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test {

    /**
     * Tạo số nguyên ngẫu nhiên trong khoảng [min, max)
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        // Khởi tạo các quả bóng đỏ dự tuyển
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        // Chọn ra sáu quả bóng đỏ
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        // Sắp xếp các quả bóng đỏ
        Collections.sort(selectedBalls);
        // Thêm một quả bóng xanh
        selectedBalls.add(randomInt(1, 17));
        // Xuất dãy số ngẫu nhiên được chọn
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}
```

Mã nguồn Python:

```Python
from random import randint, sample

# Khởi tạo các quả bóng đỏ dự tuyển
red_balls = [x for x in range(1, 34)]
# Chọn ra sáu quả bóng đỏ
selected_balls = sample(red_balls, 6)
# Sắp xếp các quả bóng đỏ
selected_balls.sort()
# Thêm một quả bóng xanh
selected_balls.append(randint(1, 16))
# Xuất dãy số ngẫu nhiên được chọn
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
```

Tôi tin rằng, sau khi xem xong những ví dụ này, bạn nhất định sẽ cảm thấy việc tôi lựa chọn Python là hoàn toàn có lý do chính đáng.