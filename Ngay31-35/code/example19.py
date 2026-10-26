"""
Mở rộng hiệu năng hệ thống
- Mở rộng theo chiều dọc - Tăng năng lực xử lý của nút đơn lẻ
- Mở rộng theo chiều ngang - Biến nút đơn lẻ thành nhiều nút (tách đọc-ghi / cụm phân tán)
Lập trình đồng thời - Tăng tốc thực thi chương trình / Cải thiện trải nghiệm người dùng
Nhiệm vụ tốn thời gian nên được thực thi độc lập tối đa, không chặn các phần khác của code
- Đa luồng
1. Tạo đối tượng Thread, chỉ định target và args rồi khởi chạy bằng phương thức start
2. Kế thừa lớp Thread và ghi đè phương thức run để định nghĩa nhiệm vụ thực thi của luồng
3. Tạo đối tượng pool luồng ThreadPoolExecutor và nộp nhiệm vụ thực thi qua submit
Cách thứ 3 có thể nhận kết quả thực thi trong tương lai qua phương thức result của đối tượng Future
Cũng có thể dùng phương thức done để xác định luồng đã thực thi xong chưa
- Đa tiến trình
- I/O bất đồng bộ
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()

#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnails/{filename}_{size}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args=(infile, ))
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'Thời gian chạy: {end - start} giây')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # Phương thức submit là phương thức không chặn 
        # Ngay cả khi số luồng làm việc đã dùng hết, submit vẫn tiếp nhận nhiệm vụ được nộp
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # Phương thức result là phương thức chặn, nếu luồng chưa kết thúc
        # tạm thời chưa lấy được kết quả thì code sẽ bị chặn tại đây
        future.result()
    end = time.time()
    print(f'Thời gian chạy: {end - start} giây')
    # shutdown cũng là phương thức không chặn, nhưng nếu nhiệm vụ đã nộp chưa thực hiện xong
    # thì pool luồng sẽ không dừng hoạt động. Nộp thêm nhiệm vụ sau shutdown sẽ gây ra ngoại lệ
    pool.shutdown()


if __name__ == '__main__':
    main()







