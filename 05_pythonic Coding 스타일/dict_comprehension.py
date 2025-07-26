num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squ_num = { num: num*num for num in num if num <= 5}
odd_squ_num = {num : num*num for num in num if num % 2 == 0}

print("1부터 5까지의 제곱 딕셔너리 :", squ_num)
print("짝수만의 제곱 딕셔너리 :", odd_squ_num)