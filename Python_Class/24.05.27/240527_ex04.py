# write(문자열) - 문자열을 파일에 쓴다
# writelines(문자열 리스트) - 리스트에 있는 문자열을 한 줄에 쓴다

# fp = open("newfile.txt", 'w', encoding="UTF-8")
# fp.write("안녕")
# fp.write("하세요!!!!\n")
# fp.writelines(["오늘은", "파일 입출력을", "알아보는 중입니다"])
#
# fp.close()

# 모드 'a'는 append의 약자
fp = open("newfile.txt", 'a', encoding="UTF-8")
fp.write("낄낄")
print(fp)
fp.close()