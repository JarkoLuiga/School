str1 = int(open("file1", "r").read())
str2 = int(open("file2", "r").read())
if str1 + str2 < 20:
    print(str1 + str2)
else:
    open("tulemus.txt","w").write("Hallo!" * 20)

str1 = int(open("A.txt", "r").read())
str2 = int(open("B.txt", "r").read())
s = str1 + str2
if s > 20:
    print(str1 + str2)
else:
    open("tulemus.txt","w").write("Hallo!" * s)
