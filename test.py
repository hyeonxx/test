import csv
import os
import datetime
import calendar

FILENAME = 'account.csv'
CATEGORIES = {
    '수입': ['월급', '용돈', '상여','금융소득','부수입', '기타'],
    '지출': ['식비', '교통/차량', '쇼핑', '문화생활','교육','마트/편의점','경조사/회비', '기타']
}

# CSV 파일 불러오기
def load_records():
    records = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # 헤더 스킵
            records = [row for row in reader]
    return records

# CSV 파일 저장하기
def save_records(records):
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['날짜', '분류', '카테고리', '내용', '금액'])
        writer.writerows(records)


