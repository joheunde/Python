fp = open("myfile.txt", 'r', encoding="UTF-8")
msg = fp.readline().strip()  # .strip() => 문자열의 함수, 마지막에 있는 엔터값을 없애줌
print(msg, end='')
msg = fp.readline().strip()
print(msg, end='')
msg = fp.readline().strip()
print(msg, end='')
msg = fp.readline().strip()
print(msg, end='')

fp.close()  # 파일 닫기
