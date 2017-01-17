#-*- coding:utf-8 -*-
import time
import random
sql_template = '''INSERT INTO `cm_complaint_item_abnor` (`ABNOR_ID`, `SHEET_ID`, `COMPLAINT_SOURCE`, `RECEIVE_TIME`, `ISSUE_TYPE`, `COMPLAINT_REASON`, `VALID_FLAG`, `ASSIGN_TO_BEFORE`, `ASSIGN_TO`, `RESPONSIBLY_PARTY`, `EC_NAME`, `EC_CODE`, `PRODUCT_TYPE`, `PRODUCT_ORDER_ID`, `SID`, `SERIAL_NUM`, `CONSUMER_COMPLAINT_TIME`, `MOBILE`, `ORDER_CREATED_DATE`, `CONTENT`, `CONSUMER_SEARCH_RESULT`, `PROV_ID`, `PROVE`, `REAL_TRANSFER_INFO`, `RE_TRANSFER`, `CHARGE_FLAG`, `ORDER_ID`, `BBOSS_FLOW`, `PERSONAL_ORDER_SEARCH`, `ATTACH_GROUP_ID`, `ISSUE_REASON`, `PROCESSED_RESULT`, `PROCESSED_ATTACH_ID`, `PRE_PROCESSED_ATTACH_ID`, `INVEST_ATTACH_ID`, `PROCESSING_STEP`, `PROCESSED_TIME`, `STATUS`, `START_TIME`, `END_TIME`, `PROCESS_TIME`, `LOCAL_PROCESS_TIME`, `NONLOCAL_PROCESS_TIME`, `OVERTIME_FLAG`, `OVERTIME`, `REOPEN_INFO`, `REFER_ID`, `DESCRIPTION`) values
('TS%s','TS2016122400041','2','%s','01','02','1','yh','admin','01','中国移动','1233333','02','7654444','9876351342','93834772','2016-12-08 15:33:10','13538292555','2016-12-08 15:33:10','流量未到账','未到账','280','123','01','1','1','6568759879','87989087098','台发布VC吧','7023','教育局与','宇航员进入','7060','7059',NULL,'13','2016-12-26 20:50:00','O','2016-12-29 16:08:17','2016-12-26 20:50:00',NULL,NULL,'1','0',NULL,NULL,'TS201612240004',NULL);'''
def random_timestamp():
    YYYYMMDD=time.strftime('%Y-%m-%d',time.localtime())
    hour=str(random.randint(0,24)).zfill(2)
    min=str(random.randint(0,60)).zfill(2)
    sec=str(random.randint(0,60)).zfill(2)
    return '%s %s:%s:%s'  % (YYYYMMDD,hour,min,sec)

fi = open('yh.sql','w+')

for li in range(1,10):
    timestamp = random_timestamp()
    fi.write(sql_template % (str(li).zfill(18),timestamp) +'\n')
    

fi.close()

