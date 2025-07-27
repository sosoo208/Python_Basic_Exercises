import os

print("파일에 저장할 내용: \n 안녕하세요\n 파이썬 파일 처리를 연습하고 있습니다\n 오늘은 좋은 날씨입니다\n")

path = r"C:\Users\USER\Desktop\루키즈\과제\python_basic_exercises\file.txt"  # 파일명 바꾸기

with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
