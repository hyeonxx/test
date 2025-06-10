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

    # 수입/지출 등록
def add_record(records):
    print("\n--- 수입/지출 등록 --- (이전으로 돌아가려면 '이전' 또는 'back' 입력)")

    # 입력값을 저장할 임시 변수들
    date_str = None
    record_type = None
    category = None
    content = None
    amount = None

    # 각 단계를 관리하는 상태 변수 (0: 시작, 1: 날짜, 2: 분류, 3: 카테고리, 4: 내용, 5: 금액, 6: 완료)
    step = 1

    while True:
        if step == 1: # 날짜 입력
            date_input = input("날짜 (YYYY-MM-DD, 예: 2023-01-15): ")
            if date_input.lower() in ['이전', 'back']:
                print("❗ 첫 단계에서는 이전으로 돌아갈 수 없습니다. 등록을 취소하려면 Ctrl+C를 누르세요.")
                continue
            try:
                datetime.datetime.strptime(date_input, '%Y-%m-%d')
                date_str = date_input
                step = 2 # 다음 단계로
            except ValueError:
                print("❗ 올바른 날짜 형식(YYYY-MM-DD)으로 입력해주세요.")

        elif step == 2: # 분류 선택
            record_type_input = input("분류 (1. 수입 / 2. 지출): ")
            if record_type_input.lower() in ['이전', 'back']:
                step = 1 # 이전 단계로
                print("🔙 날짜 입력으로 돌아갑니다.")
                continue
            if record_type_input == '1':
                record_type = '수입'
                step = 3
            elif record_type_input == '2':
                record_type = '지출'
                step = 3
            else:
                print("❗ 1 또는 2를 입력해주세요.")

        elif step == 3: # 카테고리 선택
            current_categories = CATEGORIES[record_type]
            print(f"\n--- {record_type} 카테고리 ---")
            for i, cat in enumerate(current_categories):
                print(f"{i+1}. {cat}")
            category_input = input("카테고리 선택 (번호 입력): ")
            if category_input.lower() in ['이전', 'back']:
                step = 2 # 이전 단계로
                print("🔙 분류 선택으로 돌아갑니다.")
                continue
            try:
                category_choice = int(category_input)
                if 1 <= category_choice <= len(current_categories):
                    category = current_categories[category_choice - 1]
                    step = 4
                else:
                    print("❗ 올바른 카테고리 번호를 입력해주세요.")
            except ValueError:
                print("❗ 숫자를 입력해주세요.")

        elif step == 4: # 내용 입력
            content_input = input("내용: ")
            if content_input.lower() in ['이전', 'back']:
                step = 3 # 이전 단계로
                print("🔙 카테고리 선택으로 돌아갑니다.")
                continue
            content = content_input
            step = 5

        elif step == 5: # 금액 입력
            amount_input = input("금액 (숫자만 입력): ")
            if amount_input.lower() in ['이전', 'back']:
                step = 4 # 이전 단계로
                print("🔙 내용 입력으로 돌아갑니다.")
                continue
            try:
                amount_val = int(amount_input)
                if amount_val <= 0:
                    print("❗ 금액은 0보다 큰 숫자로 입력해주세요.")
                else:
                    amount = str(amount_val) # CSV 저장을 위해 문자열로 저장
                    step = 6 # 완료 단계로
            except ValueError:
                print("❗ 금액은 숫자로만 입력해주세요.")

        elif step == 6: # 모든 정보가 유효하게 입력된 후
            records.append([date_str, record_type, category, content, amount])
            print("\n✅ 기록이 성공적으로 등록되었습니다.")
            return # 함수 종료 (등록 완료)