students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print("학생 정보:", students)

name_sorted = sorted(students, key=lambda x: x[0])
print("이름순 정렬:", name_sorted)

score_sorted = sorted(students, key=lambda x: x[1])
print("점수순 정렬:", score_sorted)

score_desc_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print("점수 내림차순:", score_desc_sorted)