from collections import Counter
import re

sample_text = "파이썬 프로그래밍은 배우기 쉬운 언어입니다. 파이썬 프로그래밍은 강력한 언어입니다. 파이썬입니다"
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r'\b[가-힣]+\b', text)
word_counts = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}번")
