text = input("문장을 입력하세요 :")

del_str = text.replace("  ", " ")
num_str = del_str.split(" ")

print("공백 제거 :", del_str)
print("단어 개수 :", len(num_str))