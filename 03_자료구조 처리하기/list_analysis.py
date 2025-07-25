num_list = [15, 3, 27, 8, 19, 12, 31]

max_num = max(num_list)
min_num = min(num_list)
num_list.remove(max_num)  
second_max_num = max(num_list)

print("숫자 목록 :", num_list)
print("최댓값 :", max_num)
print("최솟값 :", min_num)
print("두 번째로 큰 값 :", second_max_num)