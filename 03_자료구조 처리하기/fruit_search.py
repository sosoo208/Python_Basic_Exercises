fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print("과일목록 :", fruits)

find = input("찾을 과일을 입력하세요 : ")
#count는 정수 반환
find_fruits = fruits.count(find)
if find_fruits > 0:
    print(f"'{find}'가 목록에 있습니다!")
else:
    print("과일이 목록에 없습니다")
