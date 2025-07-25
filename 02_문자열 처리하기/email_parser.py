email = input("이메일 주소를 입력하세요 : ")
email_spl = email.split('@')

print("사용자명 :", email_spl[0])
print("도메인 :", email_spl[1])