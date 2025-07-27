import numpy

numbers = [10, 20, 30, 40, 50]

print("숫자들: ", numbers)
print("평균: ", numpy.mean(numbers))
print("최댓값: ", max(numbers))
print("최솟값: ", min(numbers))
print(f"표준편차: {numpy.std(numbers):.2f}")