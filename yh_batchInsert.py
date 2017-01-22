# -*- coding:utf-8 -*-
import datetime
import random

# 写入sql文件 yh.sql
sql_template = '''INSERT INTO `cm_complaint_item_abnor` (`ABNOR_ID`,       `SHEET_ID`,    `COMPLAINT_SOURCE`, `RECEIVE_TIME`, `ISSUE_TYPE`, `COMPLAINT_REASON`, `VALID_FLAG`, `ASSIGN_TO_BEFORE`, `ASSIGN_TO`, `RESPONSIBLY_PARTY`, `EC_NAME`, `EC_CODE`, `PRODUCT_TYPE`, `PRODUCT_ORDER_ID`, `SID`,         `SERIAL_NUM`, `CONSUMER_COMPLAINT_TIME`, `MOBILE`,      `ORDER_CREATED_DATE`,    `CONTENT`,    `CONSUMER_SEARCH_RESULT`, `PROV_ID`, `PROVE`, `REAL_TRANSFER_INFO`, `RE_TRANSFER`, `CHARGE_FLAG`, `ORDER_ID`, `BBOSS_FLOW`, `PERSONAL_ORDER_SEARCH`, `ATTACH_GROUP_ID`, `ISSUE_REASON`, `PROCESSED_RESULT`, `PROCESSED_ATTACH_ID`, `PRE_PROCESSED_ATTACH_ID`, `INVEST_ATTACH_ID`, `PROCESSING_STEP`, `PROCESSED_TIME`, `STATUS`, `START_TIME`, `END_TIME`, `PROCESS_TIME`, `LOCAL_PROCESS_TIME`, `NONLOCAL_PROCESS_TIME`, `OVERTIME_FLAG`, `OVERTIME`, `REOPEN_INFO`, `REFER_ID`, `DESCRIPTION`) values
                                                          ('TS%(abnorId)s','%(sheetId)s','2',               '%(receiveTime)s',          '01',        '02',      '1',    'yh',             'admin',     '01',             '%(ecName)s','1233333', '02',           '7654444',       '9876351342', '93834772',  '2016-12-08 15:33:10','%(mobile)s','2016-12-08 15:33:10','流量未到账','未到账',                '280',    '123',   '01','1','1','6568759879','87989087098','台发布VC吧','7023','教育局与','宇航员进入','7060','7059',NULL,'13','2016-12-26 20:50:00','O','2016-12-29 16:08:17','2016-12-26 20:50:00',NULL,NULL,'1','0',NULL,NULL,'TS201612240004','batch_test_data');'''
# current_time=time.localtime();
current_time = datetime.datetime.now()
ec_name_array = ["卓望", "阿里", "百度", "腾讯", "华为", "微软", "google", "索尼", "咪咕", "小米", "锤子科技", "", "京东", "亚马逊", "招商银行",
                 "工商银行", "中国移动", "中国电信", "中国联通", "网易", "暴雪娱乐", "中国银行", "三星", "任天堂"];
mobile_array = ["139", "136", "134", "135"];

fi = open('yh.sql', 'w+')

for li in range(1, 50000):
    # timestamp = random_timestamp()
    receiveTime = datetime.datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S');
    referId = "TS" + datetime.datetime.strftime(current_time, '%Y%m%d') + str(random.randint(1, 9999)).zfill(4);
    sheetId = referId + str(random.randint(1, 3)).zfill(1);
    abnorId = sheetId + str(random.randint(1, 99999)).zfill(5);
    ec_name = ec_name_array[random.randint(0, len(ec_name_array)) - 1];
    mobile = mobile_array[random.randint(0, len(mobile_array)) - 1] + str(random.randint(1, 99999999)).zfill(8);
    fi.write(sql_template % {"abnorId": abnorId, "sheetId": sheetId, "receiveTime": receiveTime, "ecName": ec_name,
                             "mobile": mobile} + '\n')

    current_time = current_time + datetime.timedelta(hours=1);

fi.close()
