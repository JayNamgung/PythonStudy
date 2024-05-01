'''
4장 되새김문제(4)
'''
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you","need","python"]))



'''
4장 되새김문제(5)
'''
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())



'''
4장 되새김문제(6)
'''
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close



'''
4장 되새김문제(7)
'''
f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace("java","python")
f.write(body)
f.close()



'''
4장 되새김문제(8)
'''
import sys

numbers = sys.argv[1:] #파일 이름을 제외한 며령 행의 모든입력

result = 0
for number in numbers:
    result += int(number)
print(result)