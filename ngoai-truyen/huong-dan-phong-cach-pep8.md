## Hướng dẫn phong cách PEP 8

PEP là viết tắt của Python Enhancement Proposal, thường được dịch là "Đề xuất cải tiến Python". Mỗi PEP là một tài liệu kỹ thuật cung cấp cho cộng đồng Python nhằm định hướng Python phát triển theo chiều hướng tốt hơn. Trong đó, Đề xuất cải tiến số 8 (PEP 8) là hướng dẫn phong cách code được biên soạn dành riêng cho ngôn ngữ Python. Mặc dù chúng ta có thể tùy ý viết mã Python miễn là đảm bảo không vi phạm cú pháp, nhưng trong thực tế công việc, việc áp dụng phong cách nhất quán để viết ra mã nguồn có tính dễ đọc cao là điều mà mọi lập trình viên chuyên nghiệp nên làm, và đây cũng là yêu cầu bắt buộc trong quy chuẩn lập trình của mỗi công ty. Điều này đặc biệt quan trọng khi nhiều người cùng cộng tác phát triển một dự án (làm việc nhóm). Chúng ta có thể tìm thấy tài liệu này từ [liên kết PEP 8](https://www.python.org/dev/peps/pep-0008/) trên trang chủ chính thức của Python. Dưới đây chúng tôi xin tóm tắt ngắn gọn các phần cốt lõi của tài liệu này.

### Sử dụng khoảng trắng

1. <u>Sử dụng khoảng trắng (space) để biểu thị thụt lề chứ không dùng phím Tab.</u> Điểm này đối với những người đã quen với các ngôn ngữ lập trình khác có thể thấy khó hiểu, vì đa số lập trình viên đều quen dùng Tab để thụt lề. Nhưng bạn cần biết rằng Python không có cú pháp dùng dấu ngoặc nhọn `{}` để tạo khối mã như C/C++ hay Java. Trong Python, cấu trúc rẽ nhánh và vòng lặp đều dùng thụt lề để xác định các dòng code thuộc cùng một cấp độ. Do đó, mã nguồn Python phụ thuộc vào việc thụt lề và độ rộng thụt lề mạnh hơn rất nhiều so với nhiều ngôn ngữ khác. Trong các trình soạn thảo khác nhau, độ rộng của phím Tab có thể là 2, 4 hoặc 8 ký tự, thậm chí là những giá trị bất thường khác. Việc dùng Tab để thụt lề có thể trở thành một thảm họa đối với mã nguồn Python.
2. <u>Mỗi cấp độ thụt lề liên quan đến cú pháp đều dùng 4 khoảng trắng.</u>
3. <u>Mỗi dòng không nên vượt quá 79 ký tự. Nếu biểu thức quá dài phải trải trên nhiều dòng, ngoại trừ dòng đầu tiên, các dòng còn lại nên thụt lề thêm 4 khoảng trắng so với mức thụt lề bình thường.</u>
4. <u>Định nghĩa hàm và lớp cần được ngăn cách với code xung quanh bằng hai dòng trống ở phía trước và phía sau.</u>
5. <u>Trong cùng một lớp, giữa các phương thức nên được ngăn cách bằng một dòng trống.</u>
6. <u>Hai bên của toán tử hai ngôi nên chừa một khoảng trắng, và chỉ cần đúng một khoảng trắng là đủ.</u>

### Đặt tên định danh

PEP 8 chủ trương dùng các phong cách đặt tên khác nhau cho các định danh khác nhau trong Python, để khi đọc mã nguồn có thể thông qua tên định danh mà xác định được định danh đó đóng vai trò gì trong Python (về điểm này, ngay cả các module tích hợp sẵn của Python và một số module bên thứ ba cũng chưa làm thật sự tốt).

1. <u>Biến, hàm và thuộc tính nên viết bằng chữ thường; nếu có nhiều từ thì dùng dấu gạch dưới `_` để nối.</u>
2. <u>Thuộc tính thể hiện (instance attribute) được bảo vệ (protected) trong lớp nên bắt đầu bằng một dấu gạch dưới `_`.</u>
3. <u>Thuộc tính thể hiện riêng tư (private) trong lớp nên bắt đầu bằng hai dấu gạch dưới `__`.</u>
4. <u>Tên của lớp và ngoại lệ nên viết hoa chữ cái đầu tiên của mỗi từ (PascalCase).</u>
5. <u>Hằng số ở cấp module nên dùng toàn bộ chữ in hoa; nếu có nhiều từ thì dùng dấu gạch dưới để nối.</u>
6. <u>Phương thức thể hiện của lớp nên đặt tên cho tham số đầu tiên là `self` để đại diện cho chính đối tượng đó.</u>
7. <u>Phương thức lớp (class method) của lớp nên đặt tên cho tham số đầu tiên là `cls` để đại diện cho chính lớp đó.</u>

### Biểu thức và câu lệnh

Trong "Triết lý của Python" (The Zen of Python, có thể xem bằng cách chạy lệnh `import this`) có một câu danh ngôn: "There should be one-- and preferably only one --obvious way to do it.", dịch sang tiếng Việt là "Nên có một — và tốt nhất chỉ một — cách rõ ràng để thực hiện việc đó". Tư tưởng mà câu nói này truyền tải cũng xuất hiện ở khắp mọi nơi trong PEP 8.

1. <u>Sử dụng từ phủ định ở dạng nội tuyến (inline), thay vì đặt từ phủ định ở phía trước toàn bộ biểu thức.</u> Ví dụ `if a is not b` sẽ dễ hiểu hơn nhiều so với `if not a is b`.
2. Không nên dùng cách kiểm tra độ dài để xác định chuỗi, danh sách, v.v. có phải là `None` hay rỗng hay không, mà nên dùng cách viết như `if not x` để kiểm tra.
3. <u>Ngay cả khi nhánh `if`, vòng lặp `for`, bắt ngoại lệ `except`, v.v. chỉ có một dòng code, cũng không nên viết chung code đó trên cùng một dòng với `if`, `for`, `except`, v.v.; tách riêng ra từng dòng mới giúp mã nguồn rõ ràng hơn.</u>
4. <u>Câu lệnh `import` luôn đặt ở phần đầu của tệp.</u>
5. <u>Khi import module, `from math import sqrt` tốt hơn là `import math`.</u>
6. <u>Nếu có nhiều câu lệnh `import`, nên chia thành ba phần, từ trên xuống dưới lần lượt là: **module tiêu chuẩn của Python**, **module của bên thứ ba** và **module tự định nghĩa**; trong nội bộ mỗi phần nên sắp xếp theo **thứ tự bảng chữ cái** của tên module.</u>
