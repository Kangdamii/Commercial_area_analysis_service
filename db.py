import pymysql
import scipy.io
import csv
db = pymysql.connect(host='database-1.c4y1s8zaxihb.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='admin', passwd='mypassword', db='retail_info', charset='utf8')

cursor = db.cursor()
sql1 = '''
            CREATE TABLE busan_store (
                idx INT NOT NULL,
                id  VARCHAR(20) NOT NULL PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                branch VARCHAR(20),
                sec1_code VARCHAR(2) NOT NULL,
                sec1_name VARCHAR(10) NOT NULL,
                sec2_code VARCHAR(4) NOT NULL,
                sec2_name VARCHAR(10) NOT NULL,
                sec3_code VARCHAR(7) NOT NULL,
                sec3_name VARCHAR(20) NOT NULL,
                std_industry_code VARCHAR(7) NOT NULL,
                std_industry_name VARCHAR(20) NOT NULL,
                sido_code VARCHAR(2) NOT NULL,
                sido_name VARCHAR(5) NOT NULL,
                sigoongoo_code VARCHAR(6) NOT NULL,
                sigoongoo_name VARCHAR(10) NOT NULL,
                admin_dong_code VARCHAR(15) NOT NULL,
                admin_dong_name VARCHAR(10) NOT NULL,
                law_dong_code VARCHAR(15) NOT NULL,
                law_dong_name VARCHAR(10) NOT NULL,
                jibun_code FLOAT,
                daeji_code INT,
                daeji_name CHAR(3),
                jibun_main_bunji INT,
                jibun_part_bunji INT,
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
                jibun_juso VARCHAR(50) NOT NULL,
                doro_code FLOAT NOT NULL,
                doro_name VARCHAR(50) NOT NULL,
                building_main_bunji INT,
                building_part_bunji INT,
                building_mng_num FLOAT NOT NULL,
                building_name VARCHAR(30),
                doro_juso VARCHAR(50) NOT NULL,
                old_zip CHAR(6) NOT NULL,
                new_zip CHAR(5) NOT NULL,
                dong_info CHAR(1),
                floor_info INT,
                ho_info INT,
                longitude FLOAT NOT NULL,
                latitude FLOAT NOT NULL,
                div_code CHAR(2)
            );
        '''
f = open('insert.csv','r')

csvReader = csv.reader(f)
for row in csvReader:
    idx = (row[0])
    id_ = (row[1])
    name = (row[2])
    branch = (row[3])
    sec1_code (row[4])
    sec1_name (row[5])
    sec2_code (row[6])
    sec2_name (row[7])
    sec3_code (row[8])
    sec3_name (row[9])
    std_industry_code (row[10])
    std_industry_name (row[11])
    sido_code (row[12])
    sido_name (row[13])
    sigoongoo_code (row[14])
    sigoongoo_name (row[15])
    admin_dong_code (row[16])
    admin_dong_name (row[17])
    law_dong_code (row[18])
    law_dong_name (row[19])
    jibun_code (row[20])
    daeji_code (row[21])
    daeji_name (row[22])
    jibun_main_bunji (row[23])
    jibun_part_bunji (row[24])
    jibun_juso (row[25])
    doro_code (row[26])
    doro_name (row[27])
    building_main_bunji (row[28])
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)
    jibun_juso VARCHAR(50) NOT NULL,
    doro_code FLOAT NOT NULL,
    doro_name VARCHAR(50) NOT NULL,
    building_main_bunji INT,
    building_part_bunji INT,
    building_mng_num FLOAT NOT NULL,
    building_name VARCHAR(30),
    doro_juso VARCHAR(50) NOT NULL,
    old_zip CHAR(6) NOT NULL,
    new_zip CHAR(5) NOT NULL,
    dong_info CHAR(1),
    floor_info INT,
    ho_info INT,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    div_code CHAR(2)

sql2 = '''
'''

cursor.execute(sql)
# DB에 Complete 하기
db.commit()
# DB 연결 닫기
db.close()
