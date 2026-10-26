## Ví dụ tham khảo tài liệu API

0. Đăng nhập người dùng - **POST** `/api/login/`

      Nhà phát triển: jackfrued

      Số phiên bản: v1

      Thời gian sửa đổi lần cuối:

      Mô tả API: Sau khi đăng nhập thành công, token người dùng sẽ được tạo mới hoặc cập nhật.

      Hướng dẫn sử dụng: Trong cơ sở dữ liệu kiểm thử đã thiết lập sẵn 4 tài khoản có thể sử dụng, như bảng dưới đây:

      | Tên người dùng | Mật khẩu | Vai trò |
      | --- | --- | --- |
      | jackfrued | 123456 | Quản trị viên |
      | wangdachui | 123123 | Người dùng thông thường |
      | hellokitty | 123123 | Môi giới bất động sản |
      | wuzetian | 123456 | Chủ nhà |

      Tham số yêu cầu:

      | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
      | --- | --- | --- | --- | --- |
      | username | Chuỗi | Có | Message body | Tên người dùng |
      | password | Chuỗi | Có | Message body | Mật khẩu người dùng |

      Thông tin phản hồi:

      - Đăng nhập thành công:

        ```JSON
        {
            "code": 30000,
            "message": "Đăng nhập người dùng thành công",
            "token": "f83e0f624e2311e9af1f00163e02b646"
        }
        ```

      - Đăng nhập thất bại:

        ```JSON
        {
            "code": 30001,
            "message": "Sai tên người dùng hoặc mật khẩu"
        }
        ```

1. Gửi mã xác thực SMS - **GET** `/api/mobile_code/{số điện thoại trong nước}/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: API gửi mã xác thực SMS đến số điện thoại chỉ định, số điện thoại phải là số di động nội địa, được truyền dưới dạng tham số đường dẫn (path parameter) trong URL. Khi API hiển thị gửi tin nhắn thành công, số điện thoại chỉ định sẽ không nhận được tin nhắn thực tế, vì số lượng SMS thử nghiệm miễn phí do nền tảng SMS bên thứ ba cung cấp đã được dùng hết.

   Hướng dẫn sử dụng: Số điện thoại nội địa tạm thời không hỗ trợ mã vùng quốc tế.

   Tham số yêu cầu: Không có.

   Thông tin phản hồi:

   - Yêu cầu thành công:

     ```JSON
     {
         "code": 10001,
         "msg": "Gửi mã xác thực SMS thành công"
     }
     ```

   - Khoảng cách giữa hai lần yêu cầu nhỏ hơn 60 giây:

     ```JSON
     {
         "code": 10002,
         "msg": "Vui lòng không gửi lại mã xác thực điện thoại trong vòng 60 giây"
     }
     ```

   - Số điện thoại không hợp lệ:

     ```JSON
     {
         "code": 10003,
         "msg": "Vui lòng cung cấp số điện thoại hợp lệ"
     }
     ```

   - Nền tảng dịch vụ SMS gặp sự cố:

     ```JSON
     {
         "code": 10004,
         "msg": "Dịch vụ SMS tạm thời không khả dụng"
     }
     ```

2. Lấy tất cả đơn vị hành chính cấp tỉnh - **GET** `/api/districts/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: Tạm thời chưa có.

   Hướng dẫn sử dụng: Tạm thời chưa có.

   Tham số yêu cầu: Tạm thời chưa có.

   Thông tin phản hồi:

   ```JSON
   [
       {
           "distid": 110000,
           "name": "Bắc Kinh"
       },
       {
           "distid": 120000,
           "name": "Thiên Tân"
       }
   ]
   ```

3. Lấy thông tin chi tiết đơn vị hành chính chỉ định và các đơn vị hành chính trực thuộc - **GET** `/api/districts/{mã đơn vị hành chính}/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: Chỉ định mã đơn vị hành chính thông qua tham số URL. Nếu mã đơn vị hành chính là cấp tỉnh, trả về thông tin tỉnh đó và các đơn vị hành chính cấp thành phố trực thuộc; nếu mã đơn vị hành chính là cấp thành phố, trả về thông tin thành phố đó và các quận/huyện trực thuộc; nếu mã đơn vị hành chính là cấp quận/huyện, trả về thông tin quận/huyện đó và thuộc tính `cities` của đơn vị hành chính cấp dưới sẽ có giá trị là `[]`.

   Hướng dẫn sử dụng: Trong cơ sở dữ liệu, ngoại trừ tỉnh Tứ Xuyên, dữ liệu "intro" của các đơn vị hành chính khác đều chưa được nhập, trường này có thể là một chuỗi rỗng.

   Tham số yêu cầu: Tạm thời chưa có.

   Thông tin phản hồi:

   ```JSON
   {
       "distid": 510000,
       "name": "Tỉnh Tứ Xuyên",
       "intro": "Nằm sâu trong nội địa khu vực Tây Nam Trung Quốc, phía đông giáp Trùng Khánh, phía nam giáp Vân Nam, Quý Châu, phía tây giáp Tây Tạng, phía bắc giáp Thiểm Tây, Cam Túc, Thanh Hải. Tổng diện tích tỉnh Tứ Xuyên là 486.000 km², tỉnh lỵ là Thành Đô. Tính đến cuối năm 2018, tỉnh Tứ Xuyên quản lý 18 thành phố trực thuộc tỉnh, 3 châu tự trị, 17 thành phố cấp huyện, 108 huyện, 4 huyện tự trị và 54 quận trực thuộc thành phố.",
       "cities": [
           {
               "distid": 510100,
               "name": "Thành phố Thành Đô"
           },
           {
               "distid": 510300,
               "name": "Thành phố Tự Cống"
           },
           {
               "distid": 510400,
               "name": "Thành phố Phan Chi Hoa"
           }
       ]
   }
   ```

4. Lấy danh sách thành phố phổ biến - **GET** `/api/hotcities/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: Tạm thời chưa có.

   Hướng dẫn sử dụng: Tạm thời chưa có.

   Tham số yêu cầu: Tạm thời chưa có.

   Thông tin phản hồi:

   ```JSON
   [
       {
           "distid": 110100,
           "name": "Bắc Kinh"
       },
       {
           "distid": 120100,
           "name": "Thiên Tân"
       },
       {
           "distid": 130100,
           "name": "Thạch Gia Trang"
       }
   ]
   ```

5. Lấy thông tin người môi giới bất động sản theo phân trang - **GET** `/api/agents/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: Tên người môi giới được xử lý theo phương thức khớp tiền tố mờ (fuzzy match); xếp hạng sao dịch vụ của người môi giới nghĩa là xếp hạng sao dịch vụ không được thấp hơn mức sao này; người môi giới có chứng chỉ hành nghề hay không chỉ có hai lựa chọn là 0 (chưa có chứng chỉ hành nghề) và 1 (đã có chứng chỉ hành nghề). Ba tham số đại diện cho các điều kiện lọc liên kết theo quan hệ VÀ (AND). Kết quả trả về là thông tin người môi giới bất động sản sau khi phân trang.

   Hướng dẫn sử dụng: Tạm thời chưa có.

   Tham số yêu cầu:

   | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
   | --- | --- | --- | --- | --- |
   | name | Chuỗi | Không | Query param | Tên người môi giới |
   | key | Chuỗi | Không | Query param | Xếp hạng sao dịch vụ người môi giới |
   | cert | Chuỗi | Không | Query param | Người môi giới có chứng chỉ hay không |
   | page | Số nguyên | Không | Query param | Số trang, mặc định là 1 |
   | size | Số nguyên | Không | Query param | Kích thước trang, mặc định là 5, tối đa không quá 50 |

   Thông tin phản hồi:

   ```JSON
   {
       "count": 1,
       "next": null,
       "previous": null,
       "results": [
           {
               "agentid": 6,
               "estates": [
                   {
                       "estateid": 11,
                       "name": "Linh Chi Tân Thôn",
                       "hot": 20
                    }
               ],
               "name": "Tiêu Lợi Lệ",
               "tel": "13040813886",
               "servstar": 4,
               "realstar": 4,
               "profstar": 4,
               "certificated": false
           }
       ]
   }
   ```

6. Thêm mới người môi giới bất động sản - **POST** `/api/agents/`

   Nhà phát triển: jackfrued

   Số phiên bản: v1

   Mô tả API: Tạm thời chưa có.

   Hướng dẫn sử dụng: Cần đăng nhập và có quyền quản trị viên, token danh tính người dùng được cung cấp trong Header yêu cầu.

   Tham số yêu cầu:

   | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
   | --- | --- | --- | --- | --- |
   | name | Chuỗi | Có | Message body | Tên người môi giới |
   | tel | Chuỗi | Có | Message body | Số điện thoại người môi giới |
   | servstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
   | realstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
   | profstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
   | certificated | Số nguyên | Không | Message body | Giá trị mặc định 0 |
   | token | Chuỗi | Có | Header yêu cầu | Token xác thực danh tính người dùng |

   Thông tin phản hồi:

   - Thêm mới thành công - Mã trạng thái **201**:

     ```JSON
     {
         "agentid": 8,
         "estates": [],
         "name": "Tôn Tiểu Mỹ",
         "tel": "13800991234",
         "servstar": 0,
         "realstar": 0,
         "profstar": 0,
         "certificated": false
     }
     ```

   - Không cung cấp thông tin xác thực - Mã trạng thái **401**:

     ```JSON
     {
         "detail": "Thông tin xác thực danh tính không chính xác."
     }
     ```

   - Người dùng hiện tại không có quyền thao tác - Mã trạng thái **403**:

     ```JSON
     {
         "detail": "Bạn không có quyền thực hiện thao tác này."
     }
     ```

7. Chỉnh sửa thông tin người môi giới bất động sản - **PUT** `/api/agents/{mã người môi giới}/`

    Nhà phát triển: jackfrued

    Số phiên bản: v1

    Mô tả API: Tạm thời chưa có.

    Hướng dẫn sử dụng: Cần đăng nhập và có quyền quản trị viên, token danh tính người dùng được cung cấp trong Header yêu cầu.

    Tham số yêu cầu:

    | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
    | --- | --- | --- | --- | --- |
    | name | Chuỗi | Có | Message body | Tên người môi giới |
    | tel | Chuỗi | Có | Message body | Số điện thoại người môi giới |
    | servstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
    | realstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
    | profstar | Số nguyên | Không | Message body | Giá trị mặc định 0 |
    | certificated | Số nguyên | Không | Message body | Giá trị mặc định 0 |
    | token | Chuỗi | Có | Header yêu cầu | Token xác thực danh tính người dùng |

    Thông tin phản hồi:

    - Cập nhật thành công - Mã trạng thái **200**:
      
     ```JSON
     {
         "agentid": 1,
         "estates": [
             {
                 "estateid": 1,
                 "name": "Kim Nhật Gia Viên",
                 "hot": 20
             },
             {
                 "estateid": 2,
                 "name": "Phỉ Thúy Viên",
                 "hot": 30
             },
             {
                 "estateid": 3,
                 "name": "Vạn Khoa Thành Thị Hoa Viên",
                 "hot": 22
             }
         ],
         "name": "Viên Hiểu Mộng",
         "tel": "158173555285",
         "servstar": 5,
         "realstar": 4,
         "profstar": 3,
         "certificated": true
     }
     ```

    - Không cung cấp thông tin xác thực - Mã trạng thái **403** - Tương tự thêm mới
    - Người dùng hiện tại không có quyền thao tác - Mã trạng thái **403** - Tương tự thêm mới

8. Xóa người môi giới bất động sản - **DELETE** `/api/agents/{mã người môi giới}/`

    Nhà phát triển: jackfrued

    Số phiên bản: v1

    Mô tả API: Tạm thời chưa có.

    Hướng dẫn sử dụng: Tạm thời chưa có.

    Tham số yêu cầu:

    | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
    | --- | --- | --- | --- | --- |
    | token | Chuỗi | Có | Header yêu cầu | Token xác thực danh tính người dùng |

    Thông tin phản hồi:

    - Xóa thành công - Mã trạng thái **204**
    - Không cung cấp thông tin xác thực - Mã trạng thái **403** - Tương tự thêm mới
    - Người dùng hiện tại không có quyền thao tác - Mã trạng thái **403** - Tương tự thêm mới

9. Lấy thông tin dự án bất động sản theo phân trang - **GET** `/api/estates/`

    Nhà phát triển: jackfrued

    Số phiên bản: v1

    Mô tả API: Tên người môi giới được xử lý theo phương thức khớp tiền tố mờ; xếp hạng sao dịch vụ của người môi giới nghĩa là xếp hạng sao dịch vụ không được thấp hơn mức sao này; người môi giới có chứng chỉ hành nghề hay không chỉ có hai lựa chọn là 0 (chưa có chứng chỉ hành nghề) và 1 (đã có chứng chỉ hành nghề). Ba tham số đại diện cho các điều kiện lọc liên kết theo quan hệ VÀ. Kết quả trả về là thông tin người môi giới bất động sản sau khi phân trang.

    Hướng dẫn sử dụng: Tạm thời chưa có.

    Tham số yêu cầu:

    | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
    | --- | --- | --- | --- | --- |
    | name | Chuỗi | Không | Query param | Tên dự án (khớp mờ) |
    | dist | Chuỗi | Không | Query param | Mã khu vực nơi dự án tọa lạc |
    | page | Số nguyên | Không | Query param | Số trang, mặc định là 1 |
    | size | Số nguyên | Không | Query param | Kích thước trang, mặc định là 5, tối đa không quá 50 |

    Thông tin phản hồi:

    ```JSON
    {
        "count": 16,
        "next": "https://120.77.222.217/api/estates/?page=2",
        "previous": null,
        "results": [
            {
                "estateid": 6,
                "district": {
                    "distid": 440303,
                    "name": "Quận La Hồ"
                },
                "agents": [
                    {
                        "agentid": 2,
                        "name": "Dương Vĩ",
                        "tel": "13352939550",
                        "servstar": 3
                    },
                    {
                        "agentid": 4,
                        "name": "Quách Chí Bằng",
                        "tel": "13686810707",
                        "servstar": 4
                    }
                ],
                "name": "Hạnh Phúc Lý",
                "hot": 300,
                "intro": ""
            }
        ]
    }
    ```

10. Thêm mới dự án bất động sản - **POST** `/api/estates/`

  Nhà phát triển: jackfrued

  Số phiên bản: v1

  Mô tả API: Tạm thời chưa có.

  Hướng dẫn sử dụng: Cần đăng nhập và có quyền quản trị viên, token danh tính người dùng được cung cấp trong Header yêu cầu.

  Tham số yêu cầu:

  | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
  | --- | --- | --- | --- | --- |
  | name | Chuỗi | Có | Message body | Tên dự án |
  | hot | Số nguyên | Không | Message body | Độ "nóng" của dự án, mặc định 0 |
  | intro | Chuỗi | Không | Message body | Giới thiệu dự án, mặc định là chuỗi rỗng |
  | distid | Số nguyên | Có | Message body | Mã khu vực nơi dự án tọa lạc |
  | token | Chuỗi | Có | Header yêu cầu | Token xác thực danh tính người dùng |

  Thông tin phản hồi:

  - Thêm mới thành công - Mã trạng thái **201**:
     ```JSON
     {
         "estateid": 17,
         "district": 510107,
         "name": "Thế Kỷ Cẩm Uyển",
         "hot": 100,
         "intro": ""
     }
     ```

  - Không cung cấp thông tin xác thực - Mã trạng thái **403**:
     ```JSON
     {
         "detail": "Vui lòng cung cấp thông tin xác thực danh tính hợp lệ"
     }
     ```

  - Người dùng hiện tại không có quyền thao tác - Mã trạng thái **403**:
     ```JSON
     {
         "detail": "You do not have permission to perform this action."
     }
     ```

11. Chỉnh sửa thông tin dự án bất động sản - **PUT** `/api/estates/{mã dự án}`

12. Xóa thông tin dự án bất động sản - **DELETE** `/api/estates/{mã dự án}`

13. Lấy tất cả thông tin loại căn hộ - **GET** `/api/housetypes/`

14. Thêm mới loại căn hộ - **POST** `/api/housetypes/`

15. Chỉnh sửa thông tin loại căn hộ - **PUT** `/api/housetypes/{mã loại căn hộ}`

16. Xóa loại căn hộ - **DELETE** `/api/housetypes/{mã loại căn hộ}`

17. Lấy danh sách bất động sản theo phân trang - **GET** `/api/houseinfos/`

     Nhà phát triển: jackfrued

     Số phiên bản: v1

     Mô tả API: Tạm thời chưa có.

     Hướng dẫn sử dụng: Tạm thời chưa có.

     Tham số yêu cầu:    

     | Tên tham số | Kiểu | Bắt buộc | Vị trí tham số | Mô tả |
     | --- | --- | --- | --- | --- |
     | title | Chuỗi | Không | Query param | Từ khóa tiêu đề bất động sản |
     | dist | Số nguyên | Không | Query param | Mã khu vực nơi dự án tọa lạc |
     | min_price | Số nguyên | Không | Query param | Giới hạn dưới của khoảng giá |
     | max_price | Số nguyên | Không | Query param | Giới hạn trên của khoảng giá |
     | type | Số nguyên | Không | Query param | Mã loại căn hộ |
     | page | Số nguyên | Không | Query param | Số trang, mặc định là 1 |
     | size | Số nguyên | Không | Query param | Kích thước trang, mặc định là 5, tối đa không quá 50 |

     Thông tin phản hồi:
     ```JSON
     {
         "count": 7,
         "next": "http://localhost:8000/api/houseinfos/?dist=440303&page=2",
         "previous": null,
         "results": [
     
         ]
     }
     ```

18. Xem chi tiết bất động sản - **GET** `/api/houseinfos/{mã bất động sản}`

19. Thêm mới bất động sản - **POST** `/api/houseinfos/`

20. Chỉnh sửa thông tin bất động sản - **PUT** `/api/houseinfos/{mã bất động sản}`

21. Xóa bất động sản - **DELETE** `/api/houseinfos/{mã bất động sản}`

22. Lấy ngẫu nhiên số lượng thẻ gắn bất động sản chỉ định - **GET** `/api/tags/`

23. Xem thẻ gắn bất động sản theo phân trang - **GET** `/api/tags/`

24. Thêm mới thẻ gắn bất động sản - **POST** `/api/tags/`

25. Xóa thẻ gắn bất động sản - **DELETE**  `/api/tags/{mã bất động sản}`

26. Xem hình ảnh của bất động sản - **GET** `/api/houseinfos/{mã bất động sản}/photos/`

27. Thêm hình ảnh cho bất động sản - **POST** `/api/houseinfos/{mã bất động sản}/photos/`

28. Xóa hình ảnh bất động sản - **DELETE** `/api/houseinfos/{mã bất động sản}/photos/{mã hình ảnh}`