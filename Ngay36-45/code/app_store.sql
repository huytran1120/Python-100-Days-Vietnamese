drop database if exists `app_store`;

create database `app_store` default character set utf8mb4;

use `app_store`;

create table `app_info` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng, ID của app',
`app_name` varchar(255) default '' comment 'Tên app',
`icon_url` varchar(255) default '' comment 'Địa chỉ icon',
`version` varchar(32) default '' comment 'Số phiên bản',
`app_size` varchar(32) default '' comment 'Kích thước gói cài đặt',
`banner_info` varchar(4096) default '' comment 'Thông tin banner',
`developer_id` varchar(255) default '' comment 'ID nhà phát triển',
`summary` varchar(512) default '' comment 'Giới thiệu ngắn',
`app_desc` text comment 'Thông tin chi tiết',
`download_url` varchar(255) default '' comment 'Liên kết tải xuống',
`price` int(10) default '0' comment 'Giá bán, đơn vị: xu',
`status` tinyint(4) unsigned default '0' comment 'Trạng thái, 1: Chờ duyệt, 2: Đã duyệt, 3: Đã gỡ xuống',
`version_desc` varchar(4096) default '' comment '',
`create_time` datetime not null default '0000-00-00 00:00:00' comment 'Thời gian tạo',
`update_time` datetime not null default '0000-00-00 00:00:00' comment 'Thời gian cập nhật',
primary key (`id`)
) engine=innodb auto_increment=100000 default charset=utf8mb4 comment='Bảng thông tin cơ bản của app';

create table `app_ext_info` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`app_id` bigint(20) not null default '0' comment 'ID của app',
`install_count` bigint(20) unsigned not null default '0' comment 'Lượt cài đặt app',
`score` int(10) unsigned not null default '0' comment 'Điểm đánh giá',
`comment_count` int(10) unsigned not null default '0' comment 'Lượt bình luận',
`create_time` int(10) not null default 0 comment 'Thời gian tạo',
`update_time` int(10) not null default 0 comment 'Thời gian cập nhật',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='Bảng thông tin mở rộng của App';

create table `app_category` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`parent_id` bigint(20) not null default '0' comment 'ID danh mục cha',
`name` varchar(64) not null default '' comment 'Tên danh mục',
`icon` varchar(512) not null default '' comment 'Địa chỉ icon',
`category_desc` text comment 'Mô tả danh mục',
`category_level` tinyint(4) unsigned not null default '0' comment 'Cấp danh mục',
`status` tinyint(4) unsigned not null default '0' comment 'Trạng thái hiện tại, 1: Đang dùng, 0: Ẩn',
`display_order` int(10) unsigned not null default '0' comment 'Thứ tự hiển thị, giá trị càng lớn càng ưu tiên trước',
`create_time` int(10) not null default 0 comment 'Thời gian tạo',
`update_time` int(10) not null default 0 comment 'Thời gian cập nhật',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='Bảng thông tin danh mục';

create table `app_category_rel` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`app_id` bigint(20) not null default '0' comment 'ID của app',
`category_id` bigint(20) unsigned not null default '0' comment 'ID danh mục cấp thấp nhất',
primary key (`id`),
unique key `idx_category_app` (`category_id`,`app_record_id`),
) engine=innodb default charset=utf8mb4 comment='Bảng liên kết App và danh mục';

create table `app_comment` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`app_id` bigint(20) not null default '0' comment 'ID của app',
`title` varchar(255) default '' comment 'Tiêu đề bình luận',
`content` varchar(2048) default '' comment 'Nội dung bình luận',
`parent_id` bigint(20) default '0' comment 'ID bình luận cha',
`commenter_uid` bigint(20) default '0' comment 'ID người dùng bình luận',
`commenter_name` varchar(255) default '' comment 'Tên người dùng bình luận',
`commenter_avatar` varchar(255) default '' comment 'Ảnh đại diện người dùng bình luận',
`top_flag` tinyint(4) default '0' comment 'Có ghim lên đầu hay không',
`like_count` int(10) default '0' comment 'Số lượt thích bình luận',
`status` tinyint(4) default '0' comment 'Trạng thái bình luận',
`create_time` int(10) not null default 0 comment 'Thời gian tạo',
`update_time` int(10) not null default 0 comment 'Thời gian cập nhật',
primary key (`id`),
key `idx_app_status` (`app_id`, `status`, `top_flag`)
) engine=innodb default charset=utf8mb4 comment='Bảng thông tin bình luận';

create table `user_app_relation` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`user_id` bigint(20) unsigned not null default '0' comment 'ID người dùng',
`app_id` bigint(20) not null default '0' comment 'ID của app',
`create_time` int(10) not null default 0 comment 'Thời gian tạo',
`update_time` int(10) not null default 0 comment 'Thời gian cập nhật',
`is_del` tinyint(4) not null default '0' comment '1: Đã xóa, 0: Chưa xóa',
primary key (`id`),
key `idx_user_app` (`user_id`,`app_id`)
) engine=innodb auto_increment=8063 default charset=utf8mb4 comment='Bảng quan hệ mua hàng của người dùng';

create table `bot_score` (
`id` bigint(20) not null auto_increment comment 'ID tự tăng',
`app_id` bigint(20) not null default '0' comment 'ID của app',
`score` int(10) default '0' comment 'Điểm người dùng đánh giá',
`commenter_uid` bigint(20) default '0' comment 'ID người dùng đánh giá',
`status` tinyint(4) default '0' comment 'Trạng thái đánh giá',
`create_time` int(10) not null default 0 comment 'Thời gian tạo',
`update_time` int(10) not null default 0 comment 'Thời gian cập nhật',
primary key (`id`),
unique key `idx_uid_score` (`app_id`,`commenter_uid`)
) engine=innodb default charset=utf8mb4 comment='Bảng đánh giá App';