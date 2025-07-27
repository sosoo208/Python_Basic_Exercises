import datetime
import random

today = datetime.datetime.today()
print("현재 날짜와 시간 : ", today.strftime("%Y-%m-%d %H:%M:%S"))

kor_weekday = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_str = kor_weekday[today.weekday()]
print(f"포맷된 날짜: {today.year}년 {today.month:02d}월 {today.day:02d}일 {weekday_str}")

rand_int = random.randint(1, 10)
print("임의의 숫자 : ", rand_int)

rand_float = round(random.uniform(0,5), 2)
print("임의의 실수 : ", rand_float)

fruits = ['포도', '사과', '오렌지', '바나나', '딸기']
choose = random.choice(fruits)
print("임의의 리스트 요소 :", choose)

random.shuffle(fruits)
print("섞인 리스트 :", fruits)