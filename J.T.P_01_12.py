number = input("숫자를 입력하세요: ")

print("(1) "+"="*40)
print(number)
print("="*44)

print("(2) "+"="*40)
print(type(number))
print("="*44)

a = 123
print("(3) "+"="*40)
print(a)
a = [1, 2, 3]
print(a)
print("="*44)

print("(4) "+"="*40)
print("[1] life is too short")
print("[2] life" "is" "too" "short")
print("[3] life" "is" "too" " short")
print("[4]", "life", "is", "too", "short")
print("="*44)

print("(5) "+"="*40)
for i in range(10):
    print(i, end=' ')
print("="*44)

print("(6) "+"="*40)
for i in range(10):
    print(i, end='')
print("="*44)

print("(7) "+"="*40)
for i in range(10):
    print(i)
print("="*44)




result = 0

def add(num):
    global result
    result += num
    return result

print("(8) "+"="*40)
print(add(3))
print("="*44)


result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print("(9) "+"="*40)
print(add1(3))
print(add1(4))
print(add2(7))
print(add2(9))
print("="*44)

class Cookie:
    pass

print("(10) "+"="*40)
a = Cookie()
b = Cookie()
print("="*44)


'''
숫자를 입력하세요: 91002
(1) ========================================
91002
============================================
(2) ========================================
<class 'str'>
============================================
(3) ========================================
123
[1, 2, 3]
============================================
(4) ========================================
[1] life is too short
[2] lifeistooshort
[3] lifeistoo short
[4] life is too short
============================================
(5) ========================================
0 1 2 3 4 5 6 7 8 9 ============================================
(6) ========================================
0123456789============================================
(7) ========================================
0
1
2
3
4
5
6
7
8
9
============================================
(8) ========================================
3
============================================
(9) ========================================
3
7
7
16
============================================
(10) ========================================
============================================
'''