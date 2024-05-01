'''
모듈
패키지
예외 처리
'''

try:
    4/0
except ZeroDivisionError as e:
    print(e)



try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
except IndexError as e:
    print("인덱싱할 수 없습니다.")
    print(e)



try:
    a = [1,2]
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)



try:
    age = int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')




class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# say_nick("천사")
# say_nick("바보")




try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print("허용되지 않는 별명입니다.")
    print(e)




'''
OUTPUT

division by zero
인덱싱할 수 없습니다.
list index out of range
list index out of range
나이를 입력하세요: 21
환영합니다.
천사
허용되지 않는 별명입니다.
'''