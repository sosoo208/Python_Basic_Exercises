num_list = []

while True:
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료) : "))
    num_list.append(num)
    if num == 0:
        print("입력된 숫자들의 합: ", sum(num_list))
        break
    else:
        continue