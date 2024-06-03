fp = open("myfile.txt", 'r', encoding="UTF-8")

while True:
    msg = fp.readline()
    if msg == '':
        break
    print(msg.strip())

fp.close()
