fp = open("myfile.txt", 'r', encoding="UTF-8")
msg_list = [m.strip() for m in fp.readlines()]

# for 인덱스변수, 값 in enumerate(순서가 있는 데이터)
# enumerate는 인덱스와 값을 묶은 정보를 만들어줌

for idx, msg in enumerate(msg_list):
    print(f"{idx + 1} : {msg}")

fp.close()
