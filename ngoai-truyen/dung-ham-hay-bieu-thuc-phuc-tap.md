## Dùng hàm hay biểu thức phức tạp

Tác giả ban đầu của ngôn ngữ Perl, *Larry Wall*, từng nói rằng các lập trình viên vĩ đại đều có ba đức tính: lười biếng, nóng nảy và tự phụ. Thoạt nhìn, cả ba từ này đều chẳng mang nghĩa tích cực, nhưng trong thế giới của lập trình viên, chúng lại mang những hàm ý rất khác. Trước hết, sự lười biếng sẽ thôi thúc lập trình viên viết ra những chương trình tiết kiệm công sức để hỗ trợ bản thân hoặc người khác hoàn thành công việc tốt hơn, nhờ đó chúng ta không cần phải làm những công việc lặp đi lặp lại và tẻ nhạt; cũng tương tự như vậy, việc gì có thể giải quyết bằng 3 dòng code thì chúng ta tuyệt đối không viết tới 10 dòng. Thứ hai, sự nóng nảy khiến lập trình viên chủ động hoàn thành những công việc mà bạn thậm chí còn chưa đề ra, luôn tối ưu hóa mã nguồn để nó đạt hiệu suất cao hơn; một tác vụ có thể hoàn thành trong 3 giây thì chúng ta tuyệt đối không thể kiên nhẫn chờ đợi 1 phút. Cuối cùng, sự tự phụ thôi thúc lập trình viên viết ra những dòng code chuẩn xác, không chút tì vết; chúng ta viết code không phải để chịu những lời chỉ trích, phàn nàn, mà là để người khác phải trầm trồ thán phục.

Vậy thì tiếp theo đây có một câu hỏi rất thú vị đáng để chúng ta cùng thảo luận: chúng ta cần một chương trình tìm ra số lớn nhất trong ba số được nhập vào. Chương trình này đối với bất kỳ ai biết lập trình đều chỉ là chuyện nhỏ, thậm chí một người chưa từng học lập trình sau 10 phút làm quen cũng có thể xử lý được. Dưới đây là đoạn code Python dùng để giải quyết bài toán này:

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
	the_max = a
else:
	the_max = b
if c > the_max:
	the_max = c
print('The max is:', the_max)
```

Thế nhưng như chúng ta vừa nói, lập trình viên vốn lười biếng, rất nhiều người sẽ dùng toán tử ba ngôi (ternary conditional operator) để viết lại đoạn code trên:

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a if a > b else b
the_max = c if c > the_max else the_max
print('The max is:', the_max)
```

Cần giải thích thêm rằng, trước phiên bản Python 2.5, ngôn ngữ này chưa có toán tử điều kiện ba ngôi được dùng ở dòng thứ 4 và thứ 5 trong đoạn code trên. Nguyên nhân sâu xa là Guido van Rossum (cha đẻ của Python) cho rằng toán tử ba ngôi không thực sự giúp Python trở nên ngắn gọn hơn. Do đó, những lập trình viên quen dùng toán tử ba ngôi trong C/C++ hoặc Java (trong các ngôn ngữ này, toán tử ba ngôi còn được gọi là "toán tử Elvis", vì ký hiệu `?:` đặt cạnh nhau trông rất giống mái tóc phồng đặc trưng của danh ca nhạc rock Elvis Presley) đã cố gắng tận dụng tính chất đoản mạch (short-circuit) của các toán tử `and` và `or` để mô phỏng toán tử ba ngôi. Vào thời điểm đó, đoạn code trên thường được viết như sau:

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a > b and a or b
the_max = c > the_max and c or the_max
print('The max is:', the_max)
```

Tuy nhiên, cách làm này trong một số trường hợp sẽ không hoạt động đúng, hãy xem đoạn code dưới đây:

```Python
a = 0
b = -100
# Đoạn code dưới đây vốn dĩ kỳ vọng in ra giá trị của a, nhưng kết quả lại nhận được giá trị của b
# Bởi vì giá trị 0 của a khi thực hiện phép toán logic sẽ được coi là False để xử lý
print(True and a or b)
# print(a if True else b)
```

Vì vậy, từ Python 2.5 trở đi, toán tử điều kiện ba ngôi đã được đưa vào để tránh rủi ro nói trên (chính là dòng cuối cùng bị comment trong đoạn code trên). Vậy thì câu hỏi tiếp theo đặt ra là: đoạn code trên có thể viết ngắn gọn hơn nữa không? Câu trả lời chắc chắn là có.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', (a if a > b else b) if (a if a > b else b) > c else c)
```

Thế nhưng, làm như vậy có thực sự tốt không? Một biểu thức phức tạp như thế này liệu có làm cho mã nguồn trở nên tối nghĩa và khó hiểu hơn rất nhiều không? Chúng ta nhận thấy rằng, trong thực tế phát triển phần mềm, nhiều lập trình viên rất thích lạm dụng các tính năng ngôn ngữ hoặc cú pháp ngọt ngào (syntactic sugar), biến nhiều dòng code đơn giản thành một biểu thức phức tạp trên một dòng duy nhất. Làm như vậy có thực sự tốt không? Câu hỏi này bản thân tôi cũng đã tự hỏi không biết bao nhiêu lần, và câu trả lời mà hiện tại tôi có thể đưa ra chính là đoạn code bên dưới, sử dụng một hàm bổ trợ (helper function).

```Python
def the_max(x, y):
	return x if x > y else y


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', the_max(the_max(a, b), c))
```

Trong đoạn code trên, tôi đã định nghĩa một hàm bổ trợ `the_max` dùng để tìm ra giá trị lớn hơn trong hai giá trị truyền vào qua tham số. Nhờ vậy, câu lệnh in bên dưới có thể gọi hàm `the_max` hai lần để tìm ra số lớn nhất trong ba số. Giờ đây tính dễ đọc của đoạn code chẳng phải đã tốt hơn rất nhiều rồi sao? Dùng hàm bổ trợ để thay thế biểu thức phức tạp thực sự là một lựa chọn tuyệt vời; điều cốt lõi là khi logic so sánh lớn nhỏ được tách ra thành hàm bổ trợ này, nó không chỉ có thể được gọi lặp đi lặp lại nhiều lần mà còn có thể thực hiện thao tác lồng nhau (cascading).

Tất nhiên, trong nhiều ngôn ngữ, hàm so sánh lớn nhỏ hoàn toàn không cần chúng ta phải tự cài đặt (thường đã là các hàm tích hợp sẵn), và Python cũng không ngoại lệ. Hàm `max` tích hợp sẵn của Python tận dụng khả năng hỗ trợ đối số biến đổi (variable arguments) của Python, cho phép truyền vào nhiều giá trị cùng lúc hoặc một iterator để tìm ra giá trị lớn nhất. Do đó, vấn đề được thảo luận ở trên trong Python thực ra chỉ gói gọn trong đúng một câu lệnh:

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', max(a, b, c))
```

Thế nhưng tư tưởng chuyển từ biểu thức phức tạp sang việc dùng hàm bổ trợ để đơn giản hóa biểu thức phức tạp là một điều rất đáng để chúng ta suy ngẫm, vì vậy tôi xin chia sẻ để cùng trao đổi với mọi người.
