## Hiểu rõ coroutine qua một ví dụ nhỏ

Coroutine có lẽ là một trong những điểm kiến thức khiến người mới học Python bối rối nhất, và nó cũng là một phương thức quan trọng để thực hiện lập trình đồng thời (concurrency) trong Python. Trong Python, chúng ta có thể sử dụng đa luồng (multi-threading) và đa tiến trình (multi-processing) để thực hiện tính đồng thời, hai cách này tương đối quen thuộc với mọi người. Trên thực tế, còn có một cách thực hiện đồng thời khác được gọi là lập trình bất đồng bộ (asynchronous programming), và coroutine chính là phương thức tất yếu để hiện thực hóa lập trình bất đồng bộ.

Khái niệm coroutine có thể hiểu một cách đơn giản là nhiều chương trình con (subroutine) cộng tác lẫn nhau. Trong cùng một luồng, khi một chương trình con bị nghẽn (block), chúng ta có thể chuyển ngay lập tức từ chương trình con này sang một chương trình con khác, từ đó tránh việc CPU bị nhàn rỗi do chương trình bị block. Nhờ vậy, hiệu suất sử dụng CPU được nâng cao, tương đương với việc dùng phương thức cộng tác để tăng tốc độ thực thi của chương trình. Do đó, chúng ta có thể đúc kết ngắn gọn: **coroutine thực hiện tính đồng thời theo cơ chế cộng tác (cooperative concurrency)**.

Tiếp theo, một ví dụ nhỏ sẽ giúp bạn hiểu rõ thế nào là tính đồng thời theo cơ chế cộng tác. Hãy cùng xem đoạn code dưới đây:

```Python
import time


def display(num):
    time.sleep(1)
    print(num)


for num in range(10):
    display(num)
```

Đoạn code trên chắc hẳn mọi người đều rất dễ hiểu. Chương trình sẽ in ra các số từ 0 đến 9, cứ cách 1 giây lại in ra một con số, do đó toàn bộ chương trình mất khoảng 10 giây để thực thi xong. Điều đáng chú ý là vì không sử dụng đa luồng hay đa tiến trình, trong chương trình chỉ có một đơn vị thực thi duy nhất, và thao tác tạm dừng `time.sleep(1)` sẽ làm toàn bộ luồng dừng lại 1 giây. Đối với đoạn code trên, trong khoảng thời gian đó CPU hoàn toàn nhàn rỗi và không làm bất cứ việc gì cả.

Bây giờ chúng ta hãy xem điều gì sẽ xảy ra khi sử dụng coroutine. Từ Python 3.5 trở đi, việc dùng coroutine để thực hiện tính đồng thời theo cơ chế cộng tác đã có cú pháp thuận tiện hơn nhiều: chúng ta có thể dùng `async` để định nghĩa một hàm bất đồng bộ, và dùng `await` để yêu cầu một chương trình con đang bị nghẽn nhường CPU cho chương trình con cộng tác với nó. Đến Python 3.7, `async` và `await` đã chính thức trở thành các từ khóa tiêu chuẩn, mang lại sự phấn khởi lớn cho cộng đồng lập trình viên. Trước tiên chúng ta hãy xem cách định nghĩa một hàm bất đồng bộ:

```Python
import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)
```

Dưới đây là điểm mấu chốt cần lưu ý: Hàm bất đồng bộ khác với hàm thông thường. Khi gọi hàm thông thường, ta nhận được giá trị trả về, còn khi gọi hàm bất đồng bộ, ta sẽ nhận được một đối tượng coroutine (coroutine object). Chúng ta cần đưa đối tượng coroutine vào trong một event loop (vòng lặp sự kiện) thì mới đạt được hiệu quả cộng tác với các đối tượng coroutine khác, bởi vì event loop sẽ chịu trách nhiệm xử lý thao tác chuyển đổi qua lại giữa các chương trình con; nói một cách đơn giản là để chương trình con bị nghẽn nhường CPU lại cho chương trình con sẵn sàng thực thi.

Trước tiên, chúng ta dùng list comprehension (biểu thức tạo danh sách) dưới đây để tạo ra 10 đối tượng coroutine, tương tự như việc gọi hàm display trong vòng lặp lúc nãy:

```Python
coroutines = [display(num) for num in range(10)]
```

Thông qua đoạn code dưới đây, chúng ta có thể lấy event loop và đưa các đối tượng coroutine vào trong đó:

```Python
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()
```

Khi thực thi đoạn code trên bạn sẽ nhận thấy rằng: 10 coroutine, vốn mỗi coroutine bị nghẽn 1 giây, nhưng tổng cộng cả thảy chỉ mất khoảng 1 giây để hoàn tất. Điều này chứng minh rằng **một khi đối tượng coroutine bị nghẽn, nó sẽ nhường CPU thay vì để CPU rơi vào trạng thái nhàn rỗi**, qua đó **nâng cao đáng kể hiệu suất sử dụng CPU**. Hơn nữa, chúng ta cũng sẽ nhận thấy các số từ 0 đến 9 không hề được in ra theo đúng thứ tự mà chúng ta tạo đối tượng coroutine, và đó chính xác là kết quả chúng ta mong muốn; ngoài ra, chạy chương trình nhiều lần bạn sẽ thấy mỗi lần in ra kết quả lại có chút khác nhau, đó chính là kết quả của tính bất định về thứ tự thực thi vốn có trong các chương trình đồng thời.

Ví dụ trên được trích từ cuốn sách bìa hoa nổi tiếng (*Using Asyncio in Python* / *Lập trình đồng thời nâng cao với Python*). Để giúp bạn có cảm nhận sâu sắc hơn về coroutine, tôi đã sửa đổi đôi chút so với code gốc của sách. Dù ví dụ này rất đơn giản nhưng nó đã giúp bạn cảm nhận được sức hấp dẫn của cơ chế đồng thời mang tính cộng tác. Trong các dự án thực tế, nếu cần dùng đồng thời theo cơ chế cộng tác, bạn còn có thể thay thế event loop mặc định của hệ thống bằng event loop do `uvloop` cung cấp, từ đó đạt được hiệu năng cao hơn nữa, bởi vì `uvloop` được xây dựng dựa trên thư viện I/O bất đồng bộ đa nền tảng nổi tiếng libuv. Ngoài ra, nếu muốn lập trình mạng dựa trên HTTP, thư viện bên thứ ba **aiohttp** là một lựa chọn rất tốt, nó dựa trên asyncio để xây dựng HTTP server và client bất đồng bộ.