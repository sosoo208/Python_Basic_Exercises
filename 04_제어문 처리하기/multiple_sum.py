i = 1
num_list = []

for i in range(101):
    if i%3==0:
        num_list.append(i)

print("1부터 100까지의 3의 배수 :", num_list)
print("3의 배수의 합:", sum(num_list))
print("3의 배수의 개수:", len(num_list)-1)