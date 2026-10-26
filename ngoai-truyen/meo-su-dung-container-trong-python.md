## Mẹo sử dụng kiểu container trong Python

Python cung cấp hệ thống kiểu dữ liệu container vô cùng phong phú, quen thuộc nhất với mọi người có thể kể đến `list`, `tuple`, `set`, `dict`, v.v. Dưới đây xin chia sẻ cùng các bạn một số mẹo nhỏ khi sử dụng các kiểu dữ liệu này, hy vọng sẽ giúp bạn viết code theo phong cách Pythonic hơn.

#### 1. Lấy giá trị lớn nhất từ từ điển

Giả sử biến đại diện cho đối tượng từ điển có tên là `my_dict`.

- Lấy ra giá trị (value) lớn nhất:

    ```Python
    max(my_dict.values())
    ```

- Lấy ra khóa (key) có giá trị lớn nhất:

    ```Python
    max(my_dict, key=my_dict.get)
    ```

- Lấy ra cả khóa và giá trị lớn nhất:

    ```python
     max(my_dict.items(), key=lambda x: x[1])
    ```

    hoặc:

    ```Python
    import operator
    
    max(my_dict.items(), key=operator.itemgetter(1))
    ```
    
    > **Giải thích**: Đoạn code trên sử dụng hàm `itemgetter` của module `operator`, tác dụng của hàm này như dưới đây. Trong code phía trên, `itemgetter` giúp chúng ta lấy phần tử thứ 2 trong tuple 2 phần tử.
    >
    > ```Python
    > def itemgetter(*items):
    >     if len(items) == 1:
    >         item = items[0]
    >         def g(obj):
    >             return obj[item]
    >     else:
    >         def g(obj):
    >             return tuple(obj[item] for item in items)
    >     return g
    > ```

#### 2. Thống kê số lần xuất hiện của các phần tử trong danh sách

Giả sử biến đại diện cho đối tượng danh sách có tên là `my_list`.

```Python
{x: my_list.count(x) for x in set(my_list)}
```

hoặc:

```Python
from itertools import groupby

{key: len(list(group)) for key, group in groupby(sorted(my_list))}
```

> **Giải thích**: Hàm `groupby` sẽ gom các phần tử liền kề giống nhau vào cùng một nhóm, vì vậy dùng hàm `sorted` để sắp xếp trước chính là nhằm đưa các phần tử giống nhau lại cạnh nhau.

hoặc:

```Python
from collections import Counter

dict(Counter(my_list))
```

#### 3. Cắt bớt phần tử trong danh sách

Giả sử biến đại diện cho đối tượng danh sách có tên là `my_list`, thông thường mọi người sẽ nghĩ đến cách dùng sau để cắt bớt danh sách:

```Python
my_list = my_list[:i]
my_list = my_list[j:]
```

Tuy nhiên, cách tốt hơn là sử dụng thao tác dưới đây, các bạn hãy thử suy nghĩ kỹ xem vì sao nhé:

```Python
del my_list[i:]
del my_list[:j]
```

#### 4. Thực hiện thao tác zip theo danh sách dài nhất

Hàm tích hợp sẵn `zip` của Python có thể tạo ra một đối tượng generator, generator này ghép các phần tử của hai hoặc nhiều iterable lại với nhau như dưới đây:

```Python
list(zip('abc', [1, 2, 3, 4]))
```

Thực thi đoạn code trên sẽ nhận được một danh sách như sau. Chắc hẳn bạn cũng nhận thấy, số lượng phần tử trong danh sách được quyết định bởi iterable có độ dài nhỏ nhất trong hàm `zip`, vì thế danh sách dưới đây chỉ có 3 phần tử:

```Python
[('a', 1), ('b', 2), ('c', 3)]
```

Nếu muốn số lượng phần tử lặp ra sau cùng được quyết định bởi iterable có độ dài lớn nhất trong hàm `zip`, bạn có thể thử hàm `zip_longest` của module `itertools`, cách dùng như sau:

```Python
from itertools import zip_longest

list(zip_longest('abc', [1, 2, 3, 4]))
```

Đối tượng danh sách được tạo ra từ đoạn code trên như sau:

```Python
[('a', 1), ('b', 2), ('c', 3), (None, 4)]
```

#### 5. Sao chép nhanh một danh sách

Nếu muốn sao chép nhanh một đối tượng danh sách, bạn có thể thực hiện thông qua thao tác cắt lát (slicing). Tuy nhiên thao tác cắt lát chỉ thực hiện sao chép nông (shallow copy), nói một cách đơn giản là phép cắt lát tạo ra một đối tượng danh sách mới, nhưng các phần tử trong danh sách mới vẫn dùng chung tham chiếu với danh sách cũ. Nếu muốn thực hiện sao chép sâu (deep copy), bạn có thể dùng hàm `deepcopy` của module `copy`.

- Sao chép nông:

    ```Python
    thy_list = my_list[:]
    ```

    hoặc:

    ```Python
    import copy
    
    thy_list = copy.copy(my_list)
    ```

- Sao chép sâu:

    ```Python
    import copy
    
    thy_list = copy.deepcopy(my_list)
    ```

#### 6. Thao tác trên các phần tử tương ứng của hai hay nhiều danh sách

Hàm `map` tích hợp sẵn trong Python có thể thực hiện phép "ánh xạ" lên các phần tử trong một iterable, hàm này vô cùng hữu ích khi xử lý dữ liệu hàng loạt. Nhưng rất nhiều người không biết rằng hàm này còn có thể áp dụng cho nhiều iterable cùng lúc, thông qua hàm truyền vào để xử lý các phần tử tương ứng ở cùng vị trí của nhiều iterable, như dưới đây:

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
list(map(lambda x, y: x + y, my_list, thy_list))
```

Thao tác trên sẽ cho kết quả là danh sách sau:

```Python
[13, 17, 21, 25]
```

Tất nhiên, thao tác tương tự cũng có thể hoàn thành bằng cách kết hợp hàm `zip` với list comprehension:

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
[x + y for x, y in zip(my_list, thy_list)]
```

#### 7. Xử lý các giá trị rỗng và số 0 trong danh sách

Giả sử biến đại diện cho đối tượng danh sách có tên là `my_list`, nếu trong danh sách có giá trị rỗng (`None`) và giá trị 0, chúng ta có thể loại bỏ chúng bằng cách sau:

```Python
list(filter(bool, my_list))
```

Cú pháp list comprehension tương đương như sau:

```Python
[x for x in my_list if x]
```

#### 8. Trích xuất cột chỉ định từ danh sách lồng nhau

Giả sử `my_list` là một danh sách lồng nhau như dưới đây, danh sách này có thể dùng để biểu diễn một ma trận trong toán học. Nếu muốn lấy ra các phần tử ở cột thứ nhất của ma trận để tạo thành một danh sách, chúng ta có thể viết như sau:

```Python
my_list = [
    [1, 1, 2, 2],
    [5, 6, 7, 8],
    [3, 3, 4, 4],
]
col1, *_ = zip(*my_list)
list(col1)
```

Ở đây chúng ta sẽ nhận được danh sách như sau, vừa vặn là cột đầu tiên của ma trận:

```Python
[1, 5, 3]
```

Tương tự như vậy, nếu muốn lấy ra các phần tử ở cột thứ hai của ma trận để tạo thành một danh sách, ta có thể dùng phương pháp sau:

```Python
_, col2, *_ = zip(*my_list)
list(col2)
```

Từ đây, nếu muốn thực hiện phép chuyển vị ma trận (matrix transpose), chúng ta cũng có thể dựa theo hướng tư duy trên để viết đoạn code sau:

```Python
[list(x) for x in zip(*my_list)]
```

Qua thao tác trên, chúng ta sẽ nhận được danh sách như sau:

```Python
[[1, 5, 3], 
 [1, 6, 3], 
 [2, 7, 4], 
 [2, 8, 4]]
```