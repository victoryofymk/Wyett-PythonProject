#使用存储过程批量增加数据
DELIMITER $$
DROP FUNCTION
IF EXISTS `getRand`$$

CREATE FUNCTION `getRand` (counts INTEGER) RETURNS VARCHAR (20) CHARSET utf8
BEGIN

DECLARE sTemp VARCHAR (20) ;
DECLARE sTempCounts INTEGER ;

SET sTemp = CONCAT(
	ROUND(
		ROUND(RAND(), counts) * (POW(10, counts))
	),
	''
) ;
IF (CHAR_LENGTH(sTemp) < counts) THEN

SET sTempCounts = counts - CHAR_LENGTH(sTemp) ;
SET sTemp = CONCAT(
	sTemp,
	RIGHT (
		CONCAT(POW(10, sTempCounts), ''),
		sTempCounts
	)
) ;
END
IF ; RETURN sTemp ; END$$

DELIMITER $$

-- 插入数据
drop procedure if exists inset_abnor$$
CREATE PROCEDURE inset_abnor (
	IN max_num INT(10)
)
BEGIN

DECLARE i INT DEFAULT 0; -- 循环开始


declare in_dateTime  dateTime ; -- 循环递增的起始时间
declare complaint_email varchar(20);
declare complaint_sheet varchar(20) ;
declare complaint_item_abnor_id varchar(20);
-- DECLARE $complaint_reason = ENUM("01","02","03","04","05");
-- DECLARE $ec_name = new Array("腾讯","阿里","华为","百度","卓望","google","微软");
-- DECLARE $mobile = new Array("134","135","136","139");


SET autocommit = 0; #set autocommit=0 把autocommit设置成0  含义：不要自动提交


SET in_dateTime = '2016-01-01 00:00:00';


REPEAT

SET i = i + 1;

#通过前面写的函数随机产生字符串和部门编号，然后加入带emp表
SET @in_dateTime=DATE_FORMAT(in_dateTime, '%Y%m%d');
select @in_dateTime;


SET @complaint_email = CONCAT(
	'TS',
	@in_dateTime,
	getRand(4)
);
select @complaint_email;


SET @complaint_sheet = CONCAT(@complaint_email, getRand(1));
select @complaint_sheet;

SET @complaint_item_abnor_id = CONCAT(@complaint_sheet, getRand(5));
select @complaint_item_abnor_id;

INSERT INTO `cm_complaint_item_abnor`
VALUES
	(
		@complaint_item_abnor_id,-- 投诉条目编号
		@complaint_sheet, -- 投诉单编号
		'1', -- 投诉方式
		in_dateTime,-- 投诉时间
		NULL, --
		'01',-- 投诉原因
		'1', -- 是否有效
		'yanmingkun', -- 上一个处理人
		'yanmingkun', -- 当前处理人
		'', -- 责任方
		'美的', -- 集团客户名称
		'3243', -- 集团编码
		'01', -- 产品类
		'789027444', -- 产品功能订购ID
		'987613434',-- SID
		'93834477', -- 序号
		'2016-09-09 18:30:25',-- 个人客户投诉时间
		getRand(11),-- 手机号
		'2016-09-09 18:30:25',-- 订单具体时间
		'流量未到账',-- 内容
		'未到账',-- 客户查询结果
		'290',--  省份
		'45656',-- 证明
		'04',-- 实际到账
		'1',-- 流量补充情况
		'1',-- 是否扣费
		'1111',-- 订单编号
		'111',-- BBOSS流水
		'1111',-- 个人产品订购结果查询
		NULL,
		'11111',-- 问题原因
		'11',-- 处理结果
		'',-- 投诉处理结果附件
		'',-- 预处理结果附件
		NULL,-- 协查结果附件
		'18',-- 处理环节
		'2016-12-29 20:51:00',-- 处理时间
		'O',-- 状态
		'2016-12-29 20:51:00',-- 发起时间
		NULL,
		NULL,
		NULL,
		'',--
		'0',-- 是否处理超时
		NULL,
		NULL,
		@complaint_email,-- 邮件/工单编号
		'abnor_chart_test'
	);

-- INSERT INTO cm_complaint_item_abnor
-- VALUES
-- 	(
-- 		(START + i),
-- 		rand_string (6),
-- 		'SALESMAN',
-- 		0001,
-- 		curdate(),
-- 		2000,
-- 		400,
-- 		rand_num ()
-- 	);
SET in_dateTime = DATE_ADD(
	in_dateTime,
	INTERVAL '01:00:00' HOUR_SECOND
);
select in_dateTime;
UNTIL i = max_num
-- 时间增加，按一小时递增 UNTIL i = max_num
END REPEAT ;



#commit 整体提交所有spl语句，提高效率
COMMIT;


END $$ 



call inset_abnor(8);

