"""
Giao tiếp giữa các luồng (chia sẻ dữ liệu) rất đơn giản vì có thể dùng chung bộ nhớ trong cùng tiến trình
Giao tiếp giữa các tiến trình (chia sẻ dữ liệu) phức tạp hơn vì hệ điều hành bảo vệ bộ nhớ cấp cho mỗi tiến trình
Để giao tiếp giữa các tiến trình thường dùng đường ống hệ thống (pipe), socket, dịch vụ bên thứ ba
multiprocessing.Queue
Luồng daemon - daemon thread
Tiến trình daemon - firewalld / httpd / mysqld
Tiến trình không được giữ lại khi hệ thống tắt máy - không cản trở hệ thống tắt vì tiến trình chưa chạy xong
"""
from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')


def main():
    Thread(target=output, args=('Ping', ), daemon=True).start()
    Thread(target=output, args=('Pong', ), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
