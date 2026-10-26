-- Bảng giao dịch
CREATE TABLE `transaction` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã giao dịch',
  `member_id` bigint(20) NOT NULL COMMENT 'ID người dùng giao dịch',
  `amount` decimal(8,2) NOT NULL COMMENT 'Số tiền giao dịch',
  `integral` int(11) NOT NULL DEFAULT '0' COMMENT 'Điểm tích lũy sử dụng',
  `pay_state` tinyint(4) NOT NULL COMMENT 'Hình thức thanh toán 0: Số dư 1: WeChat 2: Alipay 3: Khác',
  `source` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Nguồn thanh toán wx app web wap',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái thanh toán -1: Hủy 0: Chưa hoàn thành 1: Đã hoàn thành -2: Bất thường',
  `completion_time` int(11) NOT NULL COMMENT 'Thời gian hoàn tất giao dịch',
  `note` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Ghi chú',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `transaction_order_sn_member_id_pay_state_source_status_index` (`order_sn`(191),`member_id`,`pay_state`,`source`(191),`status`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng lịch sử giao dịch
CREATE TABLE `transaction_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `events` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Chi tiết sự kiện',
  `result` text COLLATE utf8mb4_unicode_ci COMMENT 'Chi tiết kết quả',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Bảng đơn hàng
CREATE TABLE `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã đơn hàng',
  `order_sn` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã giao dịch',
  `member_id` int(11) NOT NULL COMMENT 'Mã khách hàng',
  `supplier_id` int(11) NOT NULL COMMENT 'Mã thương gia',
  `supplier_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Tên thương gia',
  `order_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái đơn hàng 0: Chưa thanh toán, 1: Đã thanh toán, 2: Đã giao hàng, 3: Đã nhận hàng, -1: Yêu cầu trả hàng, -2: Đang trả hàng, -3: Đã trả hàng, -4: Hủy giao dịch',
  `after_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái hậu mãi 0: Chưa gửi yêu cầu 1: Đã yêu cầu -1: Đã hủy hậu mãi 2: Đang xử lý 200: Đã xử lý xong',
  `product_count` int(11) NOT NULL DEFAULT '0' COMMENT 'Số lượng sản phẩm',
  `product_amount_total` decimal(12,4) NOT NULL COMMENT 'Tổng tiền sản phẩm',
  `order_amount_total` decimal(12,4) NOT NULL DEFAULT '0.0000' COMMENT 'Số tiền thực tế thanh toán',
  `logistics_fee` decimal(12,4) NOT NULL COMMENT 'Phí vận chuyển',
  `address_id` int(11) NOT NULL COMMENT 'Mã địa chỉ nhận hàng',
  `pay_channel` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Kênh thanh toán 0: Số dư 1: WeChat 2: Alipay',
  `out_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mã thanh toán đơn hàng',
  `escrow_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mã giao dịch bên thứ ba',
  `pay_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Thời gian thanh toán',
  `delivery_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Thời gian giao hàng',
  `order_settlement_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái quyết toán đơn hàng 0: Chưa quyết toán 1: Đã quyết toán',
  `order_settlement_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Thời gian quyết toán đơn hàng',
  `is_package` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'Có phải combo không',
  `is_integral` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'Có phải sản phẩm tích điểm không',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_sn_unique` (`order_sn`),
  KEY `order_order_sn_member_id_order_status_out_trade_no_index` (`order_sn`,`member_id`,`order_status`,`out_trade_no`(191))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng yêu cầu hậu mãi
CREATE TABLE `order_returns_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã đơn hàng',
  `order_detail_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã đơn hàng con',
  `return_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã yêu cầu hậu mãi',
  `member_id` int(11) NOT NULL COMMENT 'Mã người dùng',
  `state` tinyint(4) NOT NULL COMMENT 'Loại hình 0: Chỉ hoàn tiền 1: Trả hàng và hoàn tiền',
  `product_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái hàng 0: Đã nhận hàng 1: Chưa nhận hàng',
  `why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Lý do đổi trả',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Trạng thái xét duyệt -1: Từ chối 0: Chưa duyệt 1: Đã duyệt',
  `audit_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Thời gian duyệt',
  `audit_why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Lý do xét duyệt',
  `note` text COLLATE utf8mb4_unicode_ci COMMENT 'Ghi chú',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng ghi nhận đổi trả
CREATE TABLE `order_returns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `returns_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã đổi trả (dành cho khách hàng tra cứu)',
  `order_id` int(11) NOT NULL COMMENT 'Mã đơn hàng',
  `express_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mã vận đơn',
  `consignee_realname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Tên người nhận',
  `consignee_telphone` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Số điện thoại liên hệ',
  `consignee_telphone2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Số điện thoại dự phòng',
  `consignee_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Địa chỉ nhận hàng',
  `consignee_zip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mã bưu chính',
  `logistics_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Phương thức vận chuyển',
  `logistics_fee` decimal(12,2) NOT NULL COMMENT 'Cước phí vận chuyển',
  `order_logistics_status` int(11) DEFAULT NULL COMMENT 'Trạng thái vận chuyển',
  `logistics_settlement_status` int(11) DEFAULT NULL COMMENT 'Trạng thái quyết toán vận chuyển',
  `logistics_result_last` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mô tả trạng thái vận chuyển cuối cùng',
  `logistics_result` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Mô tả vận chuyển',
  `logistics_create_time` int(11) DEFAULT NULL COMMENT 'Thời gian gửi hàng',
  `logistics_update_time` int(11) DEFAULT NULL COMMENT 'Thời gian cập nhật vận chuyển',
  `logistics_settlement_time` int(11) DEFAULT NULL COMMENT 'Thời gian quyết toán vận chuyển',
  `returns_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0: Trả toàn bộ đơn 1: Trả một phần',
  `handling_way` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'PUPAWAY: Nhập kho trả hàng; REDELIVERY: Giao lại hàng; RECLAIM-REDELIVERY: Không thu hồi và giao lại hàng; REFUND: Hoàn tiền; COMPENSATION: Không trả hàng và bồi thường',
  `returns_amount` decimal(8,2) NOT NULL COMMENT 'Số tiền hoàn lại',
  `return_submit_time` int(11) NOT NULL COMMENT 'Thời gian gửi yêu cầu trả hàng',
  `handling_time` int(11) NOT NULL COMMENT 'Thời gian xử lý trả hàng',
  `remark` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Lý do trả hàng',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng đánh giá
CREATE TABLE `order_appraise` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL COMMENT 'Mã đơn hàng',
  `info` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Nội dung đánh giá',
  `level` enum('-1','0','1') COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Mức độ: -1: Kém 0: Trung bình 1: Tốt',
  `desc_star` tinyint(4) NOT NULL COMMENT 'Mức độ khớp mô tả 1-5',
  `logistics_star` tinyint(4) NOT NULL COMMENT 'Dịch vụ vận chuyển 1-5',
  `attitude_star` tinyint(4) NOT NULL COMMENT 'Thái độ phục vụ 1-5',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_appraise_order_id_index` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;