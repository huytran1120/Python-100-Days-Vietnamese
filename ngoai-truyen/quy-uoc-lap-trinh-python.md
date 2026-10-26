## Quy ước lập trình Python

Từ "quy ước" ở đây chỉ "cách làm theo thói quen, biện pháp thông thường, cách làm thường dùng", từ tương ứng trong tiếng Anh là "idiom". Do Python có những khác biệt khá rõ rệt so với nhiều ngôn ngữ lập trình khác về cú pháp cũng như cách sử dụng, vì vậy nếu một nhà phát triển Python không nắm vững những quy ước này thì sẽ không thể viết ra mã nguồn chuẩn "Pythonic". Dưới đây chúng tôi tổng hợp một số đoạn code mang tính quy ước thường dùng trong quá trình lập trình Python.

1. Giúp code vừa có thể import vừa có thể thực thi độc lập.

   ```Python
   if __name__ == '__main__':
   ```


2. Dùng cách sau để kiểm tra logic "đúng" (True) hoặc "sai" (False).

   ```Python
   if x:
   if not x:
   ```

   Code **tốt**:

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': 'jackfrued', '1002': 'Vương Đại Chùy'}
   if name and fruits and owners:
       print('I love fruits!')
   ```

   Code **chưa tốt**:

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': 'jackfrued', '1002': 'Vương Đại Chùy'}
   if name != '' and len(fruits) > 0 and owners != {}:
       print('I love fruits!')
   ```

3. Tận dụng toán tử in.

   ```Python
   if x in items: # chứa
   for x in items: # lặp
   ```

   Code **tốt**:

   ```Python
   name = 'Hao LUO'
   if 'L' in name:
       print('The name has an L in it.')
   ```

   Code **chưa tốt**:

   ```Python
   name = 'Hao LUO'
   if name.find('L') != -1:
       print('This name has an L in it!')
   ```

4. Hoán đổi hai giá trị mà không dùng biến tạm.

   ```Python
   a, b = b, a
   ```

5. Dùng chuỗi trình tự để tạo chuỗi.

   Code **tốt**:

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''.join(chars)
   print(name)  # jackfrued
   ```

   Code **chưa tốt**:

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''
   for char in chars:
       name += char
   print(name)  # jackfrued
   ```

6. EAFP tốt hơn LBYL.

   EAFP - **E**asier to **A**sk **F**orgiveness than **P**ermission (Xin tha thứ dễ hơn xin phép).

   LBYL - **L**ook **B**efore **Y**ou **L**eap (Nhìn trước khi nhảy).

   Code **tốt**:

   ```Python
   d = {'x': '5'}
   try:
       value = int(d['x'])
       print(value)
   except (KeyError, TypeError, ValueError):
       value = None
   ```

   Code **chưa tốt**:

   ```Python
   d = {'x': '5'}
   if 'x' in d and isinstance(d['x'], str) \
   		and d['x'].isdigit():
       value = int(d['x'])
       print(value)
   else:
       value = None
   ```

7. Sử dụng enumerate khi lặp.

   Code **tốt**:

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   for index, fruit in enumerate(fruits):
   	print(index, ':', fruit)
   ```

   Code **chưa tốt**:

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   index = 0
   for fruit in fruits:
       print(index, ':', fruit)
       index += 1
   ```

8. Dùng comprehension để tạo danh sách.

   Code **tốt**:

   ```Python
   data = [7, 20, 3, 15, 11]
   result = [num * 3 for num in data if num > 10]
   print(result)  # [60, 45, 33]
   ```

   Code **chưa tốt**:

   ```Python
   data = [7, 20, 3, 15, 11]
   result = []
   for i in data:
       if i > 10:
           result.append(i * 3)
   print(result)  # [60, 45, 33]
   ```

9. Dùng zip kết hợp khóa và giá trị để tạo từ điển.

   Code **tốt**:

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['jackfrued', 'Vương Đại Chùy', 'Bạch Nguyên Phương']
   d = dict(zip(keys, values))
   print(d)
   ```

   Code **chưa tốt**:

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['jackfrued', 'Vương Đại Chùy', 'Bạch Nguyên Phương']
   d = {}
   for i, key in enumerate(keys):
       d[key] = values[i]
   print(d)
   ```

> **Giải thích**: Nội dung của bài viết này được tổng hợp từ internet, độc giả quan tâm có thể đọc [bản gốc](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf).
