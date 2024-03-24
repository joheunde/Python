# Escape Character(\) => 다음에 나오는 문자가 문법적 해석에서 '탈출'

# 예시) "안녕!" 이라는 문구를 출력할 때
#       문자열의 시작과 끝을 큰따옴표를 사용하면 문제가 발생
#       str1 = ""안녕!""
#       문법적으로 해석되지 않길 원하는 2, 3번째 큰따옴표 앞에 \를 추가
str1 = "\"안녕!\""
print(str1)

str2 = "뉴라인(\\n)은 개행문자를 추가해줍니다."
print(str2)

str3 = '"안녕!~~"'
print(str3)

str4 = "'~~~' 라고 생각한다"
print(str4)

str5 = ('')
print(str5)
print(type(str5))

msg = "동아대 AI학과"
# len은 python의 built-in 함수, 문자열 뿐만 아니라 리스트 등에도 사용
print(len(msg))
# upper(), lower()는 string을 위한 함수, str 클래스에 정의되어있음
print(msg.lower())

print(msg.find("AI"))

# 문자열에서 각 문자를 가져오고 싶을 때에는 '인덱스'를 사용
# 인덱스는 0부터 시작
msg = "동아대 AI학과"
print(msg[6])
