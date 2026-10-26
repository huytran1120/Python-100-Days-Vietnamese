-- Tạo cơ sở dữ liệu có tên hrs
drop database if exists `hrs`;
create database `hrs` default charset utf8mb4;

-- Chuyển sang cơ sở dữ liệu hrs
use `hrs`;

-- Tạo bảng phòng ban
create table `tb_dept`
(
`dno` int not null comment 'Mã số',
`dname` varchar(10) not null comment 'Tên phòng ban',
`dloc` varchar(20) not null comment 'Địa điểm',
primary key (dno)
);

-- Chèn 4 phòng ban
insert into `tb_dept` values 
    (10, '会计部', '北京'),
    (20, '研发部', '成都'),
    (30, '销售部', '重庆'),
    (40, '运维部', '深圳');

-- Tạo bảng nhân viên
create table `tb_emp`
(
`eno` int not null comment 'Mã nhân viên',
`ename` varchar(20) not null comment 'Tên nhân viên',
`job` varchar(20) not null comment 'Chức danh',
`mgr` int comment 'Mã người quản lý',
`sal` int not null comment 'Lương tháng',
`comm` int comment 'Trợ cấp hàng tháng',
`dno` int comment 'Mã phòng ban',
primary key (eno),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- Chèn 14 nhân viên
insert into `tb_emp` values 
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
    (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
    (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
    (3211, '张无忌', '程序员', 2056, 3200, null, 20),
    (3233, '丘处机', '程序员', 2056, 3400, null, 20),
    (3251, '张翠山', '程序员', 2056, 4000, null, 20),
    (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
    (5234, '郭靖', '出纳', 5566, 2000, null, 10),
    (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
    (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
    (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
    (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
    (3577, '杨过', '会计', 5566, 2200, null, 10),
    (3588, '朱九真', '会计', 5566, 2500, null, 10);


-- Truy vấn tên và lương tháng của nhân viên có mức lương tháng cao nhất

-- Truy vấn tên và lương năm của nhân viên (lương năm = (sal + comm) * 13)

-- Truy vấn mã phòng ban và số lượng nhân viên của các phòng ban có nhân viên

-- Truy vấn tên và số lượng nhân viên của tất cả các phòng ban

-- Truy vấn tên và lương tháng của nhân viên có lương tháng vượt mức trung bình

-- Truy vấn tên, mã phòng ban và lương tháng của nhân viên có lương tháng vượt mức trung bình của phòng ban đó

-- Truy vấn tên, lương tháng và tên phòng ban của người có lương tháng cao nhất trong phòng ban

-- Truy vấn tên và chức danh của người quản lý

-- Truy vấn thứ hạng, tên và lương tháng của nhân viên xếp hạng từ 4 đến 6 về mức lương

-- Truy vấn tên, lương tháng và mã phòng ban của 2 nhân viên có mức lương cao nhất trong mỗi phòng ban
