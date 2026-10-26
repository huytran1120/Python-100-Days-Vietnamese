"""
-- Tạo cơ sở dữ liệu có tên address
create database address default charset utf8;

-- Chuyển sang cơ sở dữ liệu address
use address;

-- Tạo bảng người liên hệ tb_contacter
create table tb_contacter
(
conid int auto_increment comment 'Mã số',
conname varchar(31) not null comment 'Họ và tên',
contel varchar(15) default '' comment 'Điện thoại',
conemail varchar(255) default'' comment 'Email',
primary key (conid)
);
"""
import pymysql

INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail) 
values (%s, %s, %s)
"""
DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s 
where conid=%s
"""
SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class Contacter(object):

    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email


def input_contacter_info():
    name = input('Họ và tên: ')
    tel = input('Số điện thoại: ')
    email = input('Email: ')
    return name, tel, email


def add_new_contacter(con):
    name, tel, email = input_contacter_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_CONTACTER,
                              (name, tel, email)) == 1:
                print('Thêm người liên hệ thành công!')
    except pymysql.MySQLError as err:
        print(err)
        print('Thêm người liên hệ thất bại!')


def delete_contacter(con, contacter):
    try:
        with con.cursor() as cursor:
            if cursor.execute(DELETE_CONTACTER, (contacter.id, )) == 1:
                print('Người liên hệ đã được xóa!')
    except pymysql.MySQLError as err:
        print(err)
        print('Xóa người liên hệ thất bại!')


def edit_contacter_info(con, contacter):
    name, tel, email = input_contacter_info()
    contacter.name = name or contacter.name
    contacter.tel = tel or contacter.tel
    contacter.email = email or contacter.email
    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_CONTACTER,
                              (contacter.name, contacter.tel,
                               contacter.email, contacter.id)) == 1:
                print('Thông tin người liên hệ đã được cập nhật!')
    except pymysql.MySQLError as err:
        print(err)
        print('Cập nhật thông tin người liên hệ thất bại!')


def show_contacter_detail(con, contacter):
    print('Họ và tên:', contacter.name)
    print('Số điện thoại:', contacter.tel)
    print('Email:', contacter.email)
    choice = input('Có chỉnh sửa thông tin người liên hệ không?(yes|no)')
    if choice == 'yes':
        edit_contacter_info(con, contacter)
    else:
        choice = input('Có xóa thông tin người liên hệ không?(yes|no)')
        if choice == 'yes':
            delete_contacter(con, contacter)


def show_search_result(con, cursor):
    contacters_list = []
    for index, row in enumerate(cursor.fetchall()):
        contacter = Contacter(**row)
        contacters_list.append(contacter)
        print('[%d]: %s' % (index, contacter.name))
    if len(contacters_list) > 0:
        choice = input('Có xem chi tiết người liên hệ không?(yes|no)')
        if choice.lower() == 'yes':
            index = int(input('Vui lòng nhập số thứ tự: '))
            if 0 <= index < cursor.rowcount:
                show_contacter_detail(con, contacters_list[index])


def find_all_contacters(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total = cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_CONTACTERS,
                               (size, (page - 1) * size))
                show_search_result(con, cursor)
                if page * size < total:
                    choice = input('Tiếp tục xem trang sau?(yes|no)')
                    if choice.lower() == 'yes':
                        page += 1
                    else:
                        break
                else:
                    print('Không có bản ghi ở trang tiếp theo!')
                    break
    except pymysql.MySQLError as err:
        print(err)


def find_contacters_by_name(con):
    name = input('Tên người liên hệ: ')
    try:
        with con.cursor() as cursor:
            cursor.execute(SELECT_CONTACTERS_BY_NAME,
                           ('%' + name + '%', ))
            show_search_result(con, cursor)
    except pymysql.MySQLError as err:
        print(err)


def find_contacters(con):
    while True:
        print('1. Xem tất cả người liên hệ')
        print('2. Tìm kiếm người liên hệ')
        print('3. Thoát tìm kiếm')
        choice = int(input('Vui lòng chọn: '))
        if choice == 1:
            find_all_contacters(con)
        elif choice == 2:
            find_contacters_by_name(con)
        elif choice == 3:
            break


def main():
    con = pymysql.connect(host='1.2.3.4', port=3306,
                          user='yourname', passwd='yourpass',
                          db='address', charset='utf8',
                          autocommit=True,
                          cursorclass=pymysql.cursors.DictCursor)
    while True:
        print('===== Danh bạ =====')
        print('1. Thêm người liên hệ')
        print('2. Tìm người liên hệ')
        print('3. Thoát hệ thống')
        print('===================')
        choice = int(input('Vui lòng chọn: '))
        if choice == 1:
            add_new_contacter(con)
        elif choice == 2:
            find_contacters(con)
        elif choice == 3:
            con.close()
            print('Cảm ơn bạn đã sử dụng, tạm biệt!')
            break


if __name__ == '__main__':
    main()
