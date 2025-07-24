import math

radius = int(input("원의 반지름을 입력하세요: "))

width = radius * radius * math.pi
cir = 2 * math.pi * radius

print(f"반지름이 {radius}인 원의 넓이 : {width:.2f}")
print(f"반지름이 {radius}인 원의 둘레 : {cir:.2f}")