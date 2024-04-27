def add(a,b):
    return a+b

a = 3
b = 4
c = add(3, 4)

print("(1) "+"="*40)
print(c)
print("="*44)

print("(2) "+"="*40)
print(add(3,4))
print("="*44)


def add2(a,b):
    result = a+b
    return result

print("(3) "+"="*40)
print(add2(4,4))
print("="*44)

def say():
    return 'HI'

print("(4) "+"="*40)
print(say())
print("="*44)

def add3(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b, a+b))

print("(5) "+"="*40)
add3(5,5)
print("="*44)

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3)
print("(6) "+"="*40)
print(add_many(1,2,3))
print("="*44)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print("(7) "+"="*40)
print(add_mul('add', 1,2,3,4,5,6,7,8,9,10))
print(add_mul('mul', 1,2,3,4,5,6,7,8,9,10))
print("="*44)

def print_kwargs(**kwargs):
    print(kwargs)

print("(8) "+"="*40)
print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3)
print("="*44)

def add_and_mul(a,b):
    return a+b, a*b

result2, result3 = add_and_mul(9,10)

print("(9) "+"="*40)
print(add_and_mul(3,4))
print(result2, result3)
print("="*44)

def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick} 입니다.")

print("(10) "+"="*40)
say_nick("야호")
say_nick("바보")
print("="*44)


def say_myself(name, age, man=True):
    print(f"나의 이름은 {name} 입니다.")
    print(f"나이는 {age} 입니다.")
    
    if man:
        print(f"남자입니다.\n")
    else:
        print(f"여자입니다.\n")

print("(11) "+"="*40)
say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 30, False)
print("="*44)

a = 1
def vartest(a):
    a = a+1

print("(12) "+"="*40)
vartest(1)
print(a)
print("="*44)


def vartest2():
    global a
    a = a+1

vartest2()
print("(13) "+"="*40)
print(a)
print("="*44)

'''
def를 한줄로 표기 = lambda
'''
add = lambda a, b: a+b
result = add(3,4)
print(result)


'''
OUTPUT


(1) ========================================
7
============================================
(2) ========================================
7
============================================
(3) ========================================
8
============================================
(4) ========================================
HI
============================================
(5) ========================================
5, 5의 합은 10입니다.
============================================
(6) ========================================
6
============================================
(7) ========================================
55
3628800
============================================
(8) ========================================
{'a': 1}
{'name': 'foo', 'age': 3}
============================================
(9) ========================================
(7, 12)
19 90
============================================
(10) ========================================
나의 별명은 야호 입니다.
============================================
(11) ========================================
나의 이름은 박응용 입니다.
나이는 27 입니다.
남자입니다.

나의 이름은 박응용 입니다.
나이는 27 입니다.
남자입니다.

나의 이름은 박응선 입니다.
나이는 30 입니다.
여자입니다.

============================================
(12) ========================================
1
============================================
(13) ========================================
2
============================================
7

'''