score = 80
print(f"점수: {score}, 결과: 합격" if score>=80 else f"점수: {score}, 결과: 불합격")

age = 17
print(f"나이: {age}, 상태: 미성년자" if age > 20 else f"나이: {age}, 상태: 성인")

numbers = [5, 12, 8, 23, -5, -12, -23, 42]
print(f"숫자들의 최댓값: {max(numbers)}")
print(f"양수들: {[n for n in numbers if n > 0]}" if any(n > 0 for n in numbers) else "양수가 없습니다.")