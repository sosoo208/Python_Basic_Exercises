shopping_cart = {
    '사과': (2, 1000),
    '바나나': (3, 800),
    '오렌지': (1, 1500)
}

sum_price = 0

print("쇼핑카트:")
for fruit, (num, price) in shopping_cart.items():
    final_price = num * price
    print(f"{fruit}: {num}개 (개당 {price}원) = {final_price}원")
    sum_price += final_price

print("총 가격:", sum_price, "원")