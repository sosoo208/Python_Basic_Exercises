numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

print("숫자 리스트 :", numbers1)
print("모든 수가 짝수인가?", all(numbers1 % 2 == 0 for numbers1 in numbers1))
print("하나라도 10보다 큰 수가 있는가?", any(numbers1 > 10 for numbers1 in numbers1))

print("\n숫자 리스트2 :", numbers2)
print("모든 수가 짝수인가?", all(numbers2 % 2 == 0 for numbers2 in numbers2))
print("하나라도 10보다 큰 수가 있는가?", any(numbers2 > 10 for numbers2 in numbers2))