'''
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다.
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, queries):
    for query in queries:
        s, e = query
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string, queries)) # "programmers"



'''
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

numbers = [1, 2, 3, 4, 5]
num1 = 1
num2 = 3
print(solution(numbers, num1, num2)) # [2, 3, 4]

numbers = [1, 3, 5]
num1 = 1
num2 = 2
print(solution(numbers, num1, num2)) # [3, 5]



'''
우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다.
나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
'''
def solution(age):
    alphabet_age = ""
    for digit in str(age):
        alphabet_age += chr(97 + int(digit))
    return alphabet_age

age = 23
print(solution(age))

age = 51
print(solution(age))

age = 100
print(solution(age))