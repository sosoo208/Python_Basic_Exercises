price = int(input("상품 가격을 입력하세요: "))
rate = int(input("할인율을 입력하세요(%): "))

sale_price = price * (rate/100)
final_price = price - sale_price

print("원래 가격:", price)
print(f"할인율:{rate}%")
print(f"할인 금액: {sale_price}원")
print(f"최종 금액: {final_price}원")