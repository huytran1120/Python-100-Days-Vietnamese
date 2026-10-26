## Các chiến lược chống crawler phổ biến và giải pháp đối phó

1. Xây dựng HTTP header hợp lý.
   - Accept

   - User-Agent

   - Referer
   
   - Accept-Encoding
   
   - Accept-Language
2. Kiểm tra Cookie do trang web tạo ra.
   - Tiện ích mở rộng hữu ích: [EditThisCookie](http://www.editthiscookie.com/)
   - Cách xử lý Cookie được script tạo động
3. Thu thập nội dung động.
   - Selenium + WebDriver
   - Chrome / Firefox - Driver
4. Giới hạn tốc độ thu thập dữ liệu (cào web).
5. Xử lý trường ẩn (hidden field) trong biểu mẫu (form).
   - Không gửi biểu mẫu trước khi đọc được trường ẩn
   - Dùng các công cụ như RoboBrowser để hỗ trợ gửi biểu mẫu
6. Xử lý mã xác thực (CAPTCHA) trong biểu mẫu.
   - OCR (Tesseract) - các dự án thương mại thường không xem xét đến 

   - Nền tảng nhận diện chuyên nghiệp - Chaojiying (超级鹰) / Yundama (云打码)

     ```Python
     from hashlib import md5
     
     class ChaoClient(object):
     
         def __init__(self, username, password, soft_id):
             self.username = username
             password =  password.encode('utf-8')
             self.password = md5(password).hexdigest()
             self.soft_id = soft_id
             self.base_params = {
                 'user': self.username,
                 'pass2': self.password,
                 'softid': self.soft_id,
             }
             self.headers = {
                 'Connection': 'Keep-Alive',
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
             }
     
         def post_pic(self, im, codetype):
             params = {
                 'codetype': codetype,
             }
             params.update(self.base_params)
             files = {'userfile': ('captcha.jpg', im)}
             r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
             return r.json()
     
     
     if __name__ == '__main__':
         client = ChaoClient('username', 'password', 'soft_id')
         with open('captcha.jpg', 'rb') as file:                                                
             print(client.post_pic(file, 1902))                                          
     ```

7. Né tránh "bẫy".
   - Trên trang web có các liên kết ẩn dụ dỗ crawler thu thập dữ liệu (bẫy hoặc honeypot)
   - Thông qua Selenium+WebDriver+Chrome để phán đoán xem liên kết có hiển thị hoặc nằm trong vùng hiển thị hay không
8. Ẩn danh tính.
   - Dịch vụ proxy - KuaiProxy (快代理) / XunProxy (讯代理) / ZhimaProxy (芝麻代理) / MoguProxy (蘑菇代理) / YunProxy (云代理)

     [《Proxy cho crawler bên nào mạnh? Đánh giá so sánh chi tiết top 10 proxy trả phí!》](https://cuiqingcai.com/5094.html)

   - Mạng ẩn danh Onion (Tor) - Tại Trung Quốc cần vượt tường lửa mới có thể sử dụng

     ```Shell
     yum -y install tor
     useradd admin -d /home/admin
     passwd admin
     chown -R admin:admin /home/admin
     chown -R admin:admin /var/run/tor
     tor
     ```
