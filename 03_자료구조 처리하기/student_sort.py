student_info = {
    '김철수' : (20,'컴퓨터공학과'),
    '박민수' : (21,'경영학과'),
    '이영희' : (22,'영어영문학과'),
    '최수진' : (23,'수학과')
}

print("나이 순으로 정렬된 학생 목록: \n")

for name, (age, major) in student_info.items():
    sorted_students = sorted(student_info.items(), key=lambda item: item[1][0])
    print(f"{name} ({age}세) - {major} \n")