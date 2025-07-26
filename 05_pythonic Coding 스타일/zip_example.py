students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]
student_scores = dict(zip(students, scores))

print("학생과 점수 매칭:")
print('\n'.join(f"{name}: {score}점" for name, score in student_scores.items()))
print("점수별 학생 딕셔너리:", student_scores)