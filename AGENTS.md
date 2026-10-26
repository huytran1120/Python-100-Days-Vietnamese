# AGENTS.md

Tệp này là hướng dẫn cho các trợ lý AI (Claude, Gemini, Copilot, Cursor, ...) và người đóng góp khi làm việc trong kho này.

## Dự án này là gì

Kho này là **bản dịch tiếng Việt đầy đủ** của [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) (nguyên bản tiếng Trung).

- **Tác giả gốc**: jackfrued. Nội dung gốc và mọi bản quyền thuộc về tác giả.
- Kho gốc không có giấy phép mã nguồn mở nên kho này cũng không cấp thêm giấy phép nào; xem `NOTICE.md`.
- Dịch **trực tiếp từ bản tiếng Trung**. Bản tiếng Thổ Nhĩ Kỳ [himmetcanumutlu/Python-100-Days-Turkish](https://github.com/himmetcanumutlu/Python-100-Days-Turkish) chỉ được dùng để tham khảo cấu trúc.

## Quy tắc dịch

### Văn phong
- Tiếng Việt tự nhiên, rõ ràng, giọng giảng dạy thân thiện. Xưng hô với người đọc là "bạn"; tác giả tự xưng "tôi" (原文 "我"), "chúng ta" (原文 "我们").
- Dịch ý, không dịch word-by-word. Thành ngữ/điển tích tiếng Trung → diễn đạt tương đương bằng tiếng Việt (có thể thêm chú thích ngắn khi cần).
- Giữ nguyên cấu trúc Markdown: tiêu đề, danh sách, bảng, khối trích dẫn `>`, chú thích `**Gợi ý**`, `**Lưu ý**`, `**Giải thích**` (原文 `**提示**`, `**注意**`, `**说明**`).
- Dùng dấu câu tiếng Việt/Latin: `，` → `, `; `。` → `. `; `：` → `: `; `（）` → `()`; `“”` → `""`; `、` → `, `; `！` → `!`; `？` → `?`.

### Không được thay đổi
- **Mã nguồn**: tên biến, hàm, lớp, module, từ khóa, cú pháp. Chỉ dịch **chú thích (comment)**, **docstring**, và **chuỗi hiển thị cho người dùng** (vd. `print('你好')` → `print('Xin chào')`).
- **Kết quả in ra** trong khối code/chú thích `# 输出:` phải khớp với chuỗi đã dịch trong code.
- Đường dẫn ảnh, liên kết, URL, tên file, lệnh shell, mã SQL (ngoại trừ comment và chuỗi dữ liệu minh họa nếu không ảnh hưởng tới kết quả truy vấn được nêu trong bài).
- Công thức LaTeX.
- Thẻ HTML/thuộc tính trong Markdown.

### Cố ý GIỮ NGUYÊN tiếng Trung — KHÔNG dịch
- Tên tác giả `jackfrued` và tên nhân vật giả định (được Việt hóa thành `Vương Đại Chùy`, `Bạch Nguyên Phương`).
- **Tên cột/giá trị trong file dữ liệu** (CSV, Excel, SQL dump) mà code đọc vào, vd. `df['销售额']`. Nếu dịch sẽ làm code hỏng. Có thể thêm chú thích nghĩa bên cạnh, vd. `# 销售额 = doanh thu`.
- Tên tỉnh/thành Trung Quốc dùng trong bản đồ pyecharts, tên font như `微软雅黑`.
- Dữ liệu thử nghiệm tiếng Trung cho jieba / bộ tách từ ik (Ngày 89, 97).
- Văn bản trong hình ảnh (không sửa được).

Khi để lại tiếng Trung có chủ ý ở những chỗ người đọc có thể thắc mắc, thêm ghi chú ngắn dạng: `> **Ghi chú của người dịch**: ...` (trong Markdown) hoặc `# Ghi chú người dịch: ...` (trong code).

### Không thêm nội dung
Đây chỉ là bản dịch. Không thêm bài mới, không viết lại nội dung, không "sửa" kiến thức của tác giả. Chỉ được thêm **Ghi chú của người dịch** ngắn khi thực sự cần (vd. dịch vụ chỉ có ở Trung Quốc như 微信/WeChat, 支付宝/Alipay, 知乎/Zhihu, 阿里云/Alibaba Cloud).

### Liên kết nội bộ
Tên thư mục/file đã được đổi sang tiếng Việt không dấu (vd. `Ngay01-20/01.lam-quen-voi-python.md`) và các liên kết tương đối đã được cập nhật. **Không đổi tên file** và **không sửa đường dẫn liên kết** khi dịch; chỉ dịch phần chữ hiển thị `[...]`.

## Bảng thuật ngữ (dùng thống nhất)

| Tiếng Trung | Tiếng Việt | Ghi chú |
|---|---|---|
| 变量 | biến | |
| 数据类型 | kiểu dữ liệu | |
| 整型 / 浮点型 / 字符串型 / 布尔型 | kiểu số nguyên / số thực (số dấu phẩy động) / chuỗi / boolean | |
| 运算符 | toán tử | |
| 表达式 | biểu thức | |
| 语句 | câu lệnh | |
| 分支结构 | cấu trúc rẽ nhánh | |
| 循环结构 | cấu trúc vòng lặp | |
| 列表 | danh sách (list) | ghi `(list)` lần đầu |
| 元组 | tuple | |
| 字符串 | chuỗi (string) | |
| 集合 | tập hợp (set) | |
| 字典 | từ điển (dict) | |
| 元素 | phần tử | |
| 索引 / 切片 | chỉ mục (index) / cắt lát (slicing) | |
| 遍历 | duyệt | |
| 生成式 / 推导式 | biểu thức tạo (comprehension) | vd. "list comprehension" |
| 函数 | hàm | |
| 参数 / 实参 / 形参 | tham số / đối số / tham số hình thức | |
| 返回值 | giá trị trả về | |
| 模块 / 包 | module / package (gói) | |
| 高阶函数 | hàm bậc cao | |
| 匿名函数 | hàm ẩn danh (lambda) | |
| 装饰器 | decorator | |
| 闭包 | closure | |
| 递归 | đệ quy | |
| 面向对象编程 | lập trình hướng đối tượng | |
| 类 / 对象 / 实例 | lớp / đối tượng / thể hiện (instance) | |
| 属性 / 方法 | thuộc tính / phương thức | |
| 封装 / 继承 / 多态 | đóng gói / kế thừa / đa hình | |
| 父类 / 子类 | lớp cha / lớp con | |
| 抽象类 | lớp trừu tượng | |
| 静态方法 / 类方法 | phương thức tĩnh / phương thức lớp | |
| 魔术方法 | phương thức đặc biệt (magic method) | |
| 迭代器 / 生成器 | iterator / generator | |
| 协程 | coroutine | |
| 异常 / 异常处理 | ngoại lệ / xử lý ngoại lệ | |
| 序列化 / 反序列化 | tuần tự hóa / giải tuần tự hóa | |
| 正则表达式 | biểu thức chính quy (regex) | |
| 并发 / 并行 | đồng thời (concurrency) / song song (parallelism) | |
| 线程 / 进程 | luồng (thread) / tiến trình (process) | |
| 异步 | bất đồng bộ | |
| 爬虫 | crawler / trình thu thập dữ liệu web | |
| 数据库 / 关系型数据库 | cơ sở dữ liệu (CSDL) / CSDL quan hệ | |
| 表 / 字段 / 记录 | bảng / trường (cột) / bản ghi | |
| 主键 / 外键 / 索引 | khóa chính / khóa ngoại / chỉ mục | |
| 视图 / 存储过程 / 触发器 | view / thủ tục lưu trữ / trigger | |
| 事务 | giao dịch (transaction) | |
| 前端 / 后端 | front-end / back-end | |
| 框架 | framework | |
| 中间件 | middleware | |
| 缓存 | bộ nhớ đệm (cache) | |
| 部署 / 上线 | triển khai / đưa lên production | |
| 数据分析 / 数据可视化 | phân tích dữ liệu / trực quan hóa dữ liệu | |
| 数组 | mảng | |
| 机器学习 / 深度学习 | học máy / học sâu | |
| 训练集 / 测试集 | tập huấn luyện / tập kiểm tra | |
| 特征 / 标签 | đặc trưng / nhãn | |
| 过拟合 / 欠拟合 | quá khớp (overfitting) / chưa khớp (underfitting) | |
| 神经网络 | mạng nơ-ron | |
| 回归 / 分类 / 聚类 | hồi quy / phân loại / phân cụm | |
| 决策树 / 随机森林 | cây quyết định / rừng ngẫu nhiên | |
| 解释器 | trình thông dịch | |
| 编辑器 / 集成开发环境 | trình soạn thảo / môi trường phát triển tích hợp (IDE) | |
| 终端 / 命令行 | terminal / dòng lệnh | |
| 注释 | chú thích (comment) | |
| 缩进 | thụt lề | |
| 提示 / 注意 / 说明 | Gợi ý / Lưu ý / Giải thích | |
| 练习 / 例子 | bài tập / ví dụ | |
| 总结 | tổng kết | |

Thuật ngữ tiếng Anh phổ biến trong giới lập trình Việt Nam (framework, cache, deploy, debug, log, API, request, response, ...) có thể giữ nguyên tiếng Anh nếu tự nhiên hơn.

## Dịch file code
- `.py`, `.java`, `.html`, `.sql`: chỉ dịch comment, docstring và chuỗi hiển thị. Không động vào dữ liệu `INSERT` trừ khi đó là dữ liệu minh họa không liên quan tới bài viết. Với các file dump dữ liệu lớn (`order.sql`, `dist.sql`, `stock.sql`) chỉ dịch comment.
- `.ipynb`: chỉ dịch ô Markdown và comment trong ô code; **không sửa outputs**, không chạy lại notebook. Sửa bằng script JSON để giữ nguyên định dạng.
- Sau khi sửa code Python, kiểm tra cú pháp: `python3 -m py_compile <file>`.

## Kiểm tra sau khi dịch
- Tìm ký tự Hán còn sót: `grep -nP '[\x{4e00}-\x{9fff}]' <file>` (hoặc script Python tương đương). Chỉ được còn lại những chỗ thuộc danh sách "Cố ý giữ nguyên".
- Số khối code ```` ``` ```` phải bằng bản gốc.
