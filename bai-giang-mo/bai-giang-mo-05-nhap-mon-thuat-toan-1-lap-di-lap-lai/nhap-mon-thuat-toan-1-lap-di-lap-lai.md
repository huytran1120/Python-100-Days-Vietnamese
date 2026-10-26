## Khóa học nhập môn thuật toán 1 - Lặp đi lặp lại

### Tổng quan về thuật toán

1. Thuật toán là gì?

   Phương pháp chính xác và các bước thực hiện cụ thể để giải quyết một vấn đề.

   Ví dụ 1: Làm thế nào để kéo một sợi dây nối giữa hai phòng của hai tòa nhà cách nhau 50m (cả hai phòng đều có cửa sổ)?

   - Nuôi một con chim (như bồ câu) mang sợi dây qua
   - Dùng một cây sào thật dài để đưa sợi dây qua
   - Dùng flycam (thiết bị bay điều khiển từ xa) để đưa sợi dây qua

   Làm sao để đánh giá phương pháp nào tốt hơn? **Tốn ít chi phí, không tốn công sức**!

   Ví dụ 2: Trong một giảng đường lớn có hàng trăm sinh viên đang ngồi nghe giảng, làm sao để đếm nhanh số lượng sinh viên?

   Ví dụ 3: Chèn **ngược** 100.000 phần tử vào container danh sách (list).

   - Phương pháp 1:

     ```Python
     nums = []
     for i in range(100000):
         nums.append(i)
     nums.reverse()
     ```

   - Phương pháp 2:

     ```Python
     nums = []
     for i in range(100000):
         nums.insert(0, i)
     ```

   Ví dụ 4: Tạo dãy số Fibonacci (100 số Fibonacci đầu tiên).

   - Phương pháp 1 - Truy hồi:

     ```Python
     a, b = 0, 1
     for num in range(1, 101):
         a, b = b, a + b
         print(f'{num}: {a}')
     ```

   - Phương pháp 2 - Đệ quy:

     ```Python
     def fib(num):
         if num in (1, 2):
             return 1
         return fib(num - 1) + fib(num - 2)
     
     
     for num in range(1, 101):
         print(f'{num}: {fib(num)}')
     ```

   - Phương pháp 3 - Đệ quy cải tiến:

     ```Python
     def fib(num, temp={}):
         if num in (1, 2):
             return 1
         elif num not in temp:
             temp[num] = fib(num - 1) + fib(num - 2)
         return temp[num]
     ```

   - Phương pháp 4 - Đệ quy cải tiến:

     ```Python
     from functools import lru_cache
     
     
     @lru_cache()
     def fib(num):
         if num in (1, 2):
             return 1
         return fib(num - 1) + fib(num - 2)
     ```

2. Làm thế nào để đánh giá thuật toán tốt hay xấu?

   [Độ phức tạp thời gian tiệm cận](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%99_ph%E1%BB%A9c_t%E1%BA%A1p_th%E1%BB%9Di_gian) và độ phức tạp không gian tiệm cận.

3. Ý nghĩa của ký hiệu Big *O*?

   Biểu thị tốc độ tăng trưởng của một hàm số tương ứng với quy mô đầu vào, còn có thể gọi là bậc độ lớn của hàm số.

   | Ký hiệu Big *O* | Giải thích | Ví dụ |
   | --------------- | ------------------ | -------------------------------------------- |
   | $$O(c)$$ | Độ phức tạp thời gian hằng số | Bloom filter / Lưu trữ băm (hash) |
   | $$O(\log_2n)$$ | Độ phức tạp thời gian logarit | Tìm kiếm nhị phân |
   | $$O(n)$$ | Độ phức tạp thời gian tuyến tính | Tìm kiếm tuần tự / Sắp xếp theo thùng (bucket sort) |
   | $$O(n \cdot \log_2n)$$ | Độ phức tạp thời gian tuyến tính logarit | Thuật toán sắp xếp nâng cao (merge sort, quick sort) |
   | $$O(n^2)$$ | Độ phức tạp thời gian bậc hai | Thuật toán sắp xếp đơn giản (selection sort, insertion sort, bubble sort) |
   | $$O(n^3)$$ | Độ phức tạp thời gian bậc ba | Thuật toán Floyd / Phép nhân ma trận |
   | $$O(2^n)$$ | Độ phức tạp thời gian cấp số nhân | Tháp Hà Nội |
   | $$O(n!)$$ | Độ phức tạp thời gian giai thừa | Bài toán người bán hàng (Traveling Salesperson Problem) |

### Phương pháp vét cạn (brute-force)

Trong khoa học máy tính, **phương pháp vét cạn** (exhaustive search) hoặc **tìm kiếm thô bạo (brute-force search)** là một phương pháp giải quyết vấn đề hết sức trực quan. Phương pháp này lần lượt liệt kê tất cả các ứng viên tiềm năng của tập giải pháp và kiểm tra từng ứng viên xem có thỏa mãn mô tả bài toán hay không, từ đó tìm ra lời giải của vấn đề.

Mặc dù tìm kiếm vét cạn rất dễ thực hiện và nếu lời giải tồn tại thì chắc chắn nó sẽ tìm ra, nhưng cái giá phải trả của nó tỷ lệ thuận với số lượng phương án ứng viên. Do điểm này, trong nhiều vấn đề thực tế, chi phí tiêu hao sẽ tăng rất nhanh khi quy mô bài toán mở rộng. Vì vậy, khi quy mô vấn đề có hạn hoặc khi có cách thu hẹp tập hợp giải pháp ứng viên xuống kích thước có thể quản lý được, ta có thể dùng tìm kiếm vét cạn. Ngoài ra, khi tính đơn giản trong khâu triển khai quan trọng hơn tốc độ thực thi, ta cũng có thể cân nhắc sử dụng phương pháp này.

### Các ví dụ kinh điển

1. Bài toán **trăm tiền trăm gà**: Gà trống 5 tệ một con, gà mái 3 tệ một con, gà con 1 tệ ba con. Dùng 100 tệ mua 100 con gà, hỏi có bao nhiêu gà trống, gà mái, gà con?

   ```Python
   for x in range(21):
       for y in range(34):
           z = 100 - x - y
           if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
               print(x, y, z)
   ```

2. Bài toán **năm người chia cá**: Năm người A, B, C, D, E vào một đêm nọ cùng nhau đi bắt cá, sau đó mệt lử nên ai về chỗ nấy đi ngủ. Sáng hôm sau, A thức dậy đầu tiên, anh ta chia số cá thành 5 phần bằng nhau, vứt đi 1 con cá thừa ra và mang phần của mình đi; B thức dậy thứ hai, cũng chia số cá còn lại thành 5 phần bằng nhau, vứt đi 1 con cá thừa và mang phần của mình đi; sau đó C, D, E lần lượt thức dậy và cũng chia cá theo cách tương tự. Hỏi ban đầu họ đã bắt được ít nhất bao nhiêu con cá?

   ```Python
   fish = 6
   while True:
       total = fish
       enough = True
       for _ in range(5):
           if (total - 1) % 5 == 0:
               total = (total - 1) // 5 * 4
           else:
               enough = False
               break
       if enough:
           print(fish)
           break
       fish += 5
   ```

3. **Bẻ khóa mật khẩu bằng vét cạn**:

   ```Python
   import re

   import PyPDF2

   with open('Python_Tricks_encrypted.pdf', 'rb') as pdf_file_stream:
       reader = PyPDF2.PdfFileReader(pdf_file_stream)
       with open('dictionary.txt', 'r') as txt_file_stream:
           file_iter = iter(lambda: txt_file_stream.readline(), '')
           for word in file_iter:
               word = re.sub(r'\s', '', word)
               if reader.decrypt(word):
                   print(word)
                   break
   ```