num = int(input("몇 단을 출력할까요? :"))

print(f"{num}단 구구단: ")
for i in range(1,10):
    print(f"{num} X {i} = {num*i}")