#언패킹 공부 더 필요 / ai 도움 받음

coord = (10, 20)
x_num, y_num = coord
print(f"좌표: x={x_num} y={y_num}")

a, b, c = [1, 2, 3]
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

values = [10, 20, 30]
total = sum(values)
print("가변 인수의 합:", total)

info = {'name': '김철수', 'age': 25, 'city': '서울'}
print("키워드 인수들:", ', '.join(f"{k}={v}" for k, v in info.items()))