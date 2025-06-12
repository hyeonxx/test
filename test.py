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
            date_input = input("날짜 (YYYY-MM-DD, 예: 2025-05-06): ")
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
        
        # 전체 내역 보기
def show_all_records(records):
    print("\n--- 전체 내역 보기 ---")
    if not records:
        print("❗ 등록된 내역이 없습니다.")
        return

    # 날짜를 기준으로 정렬
    sorted_records = sorted(records, key=lambda x: x[0])

    total_income = 0
    total_expense = 0

    print("-" * 50)
    print(f"{'날짜':<12}{'분류':<6}{'카테고리':<10}{'내용':<15}{'금액':>10}")
    print("-" * 50)

    for record in sorted_records:
        date, rec_type, category, content, amount = record
        amount_int = int(amount)

        if rec_type == '수입':
            total_income += amount_int
            print(f"{date:<12}{rec_type:<6}{category:<10}{content:<15}{amount_int:>10,}")
        else: # 지출
            total_expense += amount_int
            print(f"{date:<12}{rec_type:<6}{category:<10}{content:<15}{-amount_int:>10,}") # 지출은 음수로 표시하여 시각적으로 구분

    print("-" * 50)
    print(f"총 수입: {total_income:,.0f}원")
    print(f"총 지출: {total_expense:,.0f}원")
    print(f"💰 최종 잔액: {total_income - total_expense:,.0f}원")
    print("-" * 50)


    # 월별 합계 보기
def show_monthly_calendar(records):
    print("\n--- 월별 합계 보기 (달력 형식) ---")
    if not records:
        print("❗ 등록된 내역이 없습니다.")
        return

    while True:
        year_month_input = input("조회할 연월을 입력하세요 (YYYY-MM, 예: 2023-01): ")
        if year_month_input.lower() in ['이전', 'back']:
            return # 메인 메뉴로 돌아가기
        try:
            year, month = map(int, year_month_input.split('-'))
            if not (1 <= month <= 12):
                raise ValueError
            break
        except ValueError:
            print("❗ 올바른 연월 형식(YYYY-MM)으로 입력해주세요.")

    # 해당 월의 기록 필터링 및 일별 합계 계산
    daily_summary = {} # {일: {'수입': 금액, '지출': 금액}}
    total_monthly_income = 0
    total_monthly_expense = 0

    for record in records:
        date_str, rec_type, category, content, amount_str = record
        try:
            record_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            if record_date.year == year and record_date.month == month:
                day = record_date.day
                amount = int(amount_str)

                if day not in daily_summary:
                    daily_summary[day] = {'수입': 0, '지출': 0}

                if rec_type == '수입':
                    daily_summary[day]['수입'] += amount
                    total_monthly_income += amount
                else: # 지출
                    daily_summary[day]['지출'] += amount
                    total_monthly_expense += amount
        except ValueError:
            # 날짜 형식 오류가 있는 레코드는 건너뜀
            continue

    # 달력 생성 및 출력
    cal = calendar.Calendar()
    print(f"\n{year}년 {month}월 가계부")
    print("=" * 70)
    print("월    화    수    목    금    토    일")
    print("-" * 70)

    for week in cal.monthdayscalendar(year, month):
        for day in week:
            if day == 0: # 해당 월에 속하지 않는 날짜
                print(f"{'':<8}", end="")
            else:
                summary_text = ""
                if day in daily_summary:
                    income_today = daily_summary[day]['수입']
                    expense_today = daily_summary[day]['지출']
                    if income_today > 0:
                        summary_text += f"↑{income_today:,.0f}"
                    if expense_today > 0:
                        if summary_text: summary_text += " "
                        summary_text += f"↓{expense_today:,.0f}"

                # 날짜와 요약 정보를 함께 출력
                print(f"{str(day).rjust(2):<2} {summary_text:<5}", end="  ")
        print() # 한 주가 끝나면 줄 바꿈

    print("-" * 70)
    print(f"\n--- {year}년 {month}월 요약 ---")
    print(f"총 수입: {total_monthly_income:,.0f}원")
    print(f"총 지출: {total_monthly_expense:,.0f}원")
    print(f"💰 월별 잔액: {total_monthly_income - total_monthly_expense:,.0f}원")
    print("-" * 70)

if __name__ == '__main__':
    main()
