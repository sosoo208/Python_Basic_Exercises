str_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

long_str = max(len(s) for s in str_list)
short_str = min(len(s) for s in str_list)
long_word = [s for s in str_list if len(s) == long_str]
short_word = [s for s in str_list if len(s) == short_str][0]

print("단어 목록 : ", str_list)
print(f"가장 긴 단어 : {long_word} ({long_str}글자)")
print(f"가장 짧은 단어 : {short_word} ({short_str}글자)")