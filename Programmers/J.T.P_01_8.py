'''
변수 switch
'''
a = 3
b = 5
a, b = b, a

print("(1) "+"="*40)
print(a)
print(b)
print("="*44)

c = 1
d = 2
c = d

print("(2) "+"="*40)
print(c)
print(d)
print("="*44)

'''
제어문
if문
'''

money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
'''
택시를 타고 가라
'''


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("돈이 있네")
else:
    print("돈이 없네")
'''
돈이 있네
'''


'''
제어문
while
'''
treeHit = 0
max = 10
while treeHit < max:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다."% treeHit)
    if treeHit == max:
        print("나무 넘어갑니다.")

'''
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
'''

'''
멀티라인(줄바꿈 /n)을 사용하기 위해서 심플하게 큰 따옴표 3개 또는 작은 따옴표 3개를 사용하면 간단히 사용할 수 있다.
'''
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

'''
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number:
'''

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

'''
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 9개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 8개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 7개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 6개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 5개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 4개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 3개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 2개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 1개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 0개 입니다.
커피가 다 떨어졌습니다. 판매를 중지합니다.
'''