import numpy

grades = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최수진': 95
}

grade_ave = numpy.mean(list(grades.values()))

print("학생 성적:")
for name, score in grades.items():
    print(f"{name}: {score}점")

print(f"평균 점수: {grade_ave:.1f}점")