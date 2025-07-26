num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = [ x for x in num if x % 2 == 0]
squre_even_num = [y*y for y in even_num]

print("원본 리스트 : ", num)
print("짝수들 : ", even_num)
print("짝수의 제곱 : ", squre_even_num)