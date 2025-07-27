numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x * x, numbers))
up_num = list(filter(lambda y: y > 5, numbers))

print("원본 숫자:", numbers)
print("모든 수의 제곱:", squares)
print("5보다 큰 수들:",up_num)
print("5보다 큰 수들의 제곱:", list(map(lambda z: z*z, up_num)))