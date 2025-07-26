num = int(input("숫자를 입력하세요: "))
discrim = 0

for i in range(1, num+1):
    if num % i == 0:
        discrim += 1

if discrim == 2:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 정수입니다.")