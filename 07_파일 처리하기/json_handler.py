import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

with open("data.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("데이터가 data.json에 저장되었습니다.\n")

with open("data.json", 'r', encoding="utf-8") as f:
    load_data = json.load(f)

print("JSON에서 읽어온 데이터:")
print("이름 :", load_data["이름"])
print("나이 :", load_data["나이"])
print("직업 :", load_data["직업"])
print("취미 :", load_data["취미"])
print("주소 :", load_data["주소"])