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


# 메인 메뉴
name = input("이름을 입력하세요:")
def main():
    records = load_records()
    while True:
        print("\n" + "="*40)
        print(f"📒 {name}의 알뜰살뜰 가계부!".center(40))
        print("="*40)
        print("1. 수입/지출 등록")
        print("2. 전체 내역 보기")
        print("3. 월별 합계 보기 ")
        print("4. 종료 및 저장")
        choice = input("선택 > ")

        if choice == '1':
            add_record(records)
        elif choice == '2':
            show_all_records(records)
        elif choice == '3':
            show_monthly_calendar(records)
        elif choice == '4':
            save_records(records)
            print("✅ 저장 후 종료합니다.")
            break
        else:
            print("❗ 올바른 번호를 입력해주세요.")

def add_record(records):
    print("\n[수입/지출 등록]")

def show_all_records(records):
    print("\n[전체 내역  보기 기능]")

def show_monthly_calendar(records):
    print("\n[월별 달력 합계 보기 기능]")