import re

def greeting(name):
    if re.fullmatch(r'[a-zA-Z]+', name):
        return f"Hello, {name}!"
    else:
        return f"안녕하세요, {name}!"

print(f"{greeting('김철수')}")
print(f"{greeting('John')}")
print(f"{greeting('이영희')} 좋은 하루 되세요!")