'''
문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, n):
    return my_string[0:n]

my_string = "ProgrammerS123"
n = 11
print(solution(my_string, n)) # "ProgrammerS"

my_string = "He110W0r1d"
n = 5
print(solution(my_string, n)) # "He110"



'''
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다.
예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0

my_string = "banana"
is_prefix = "ban"
print(solution(my_string, is_prefix)) # 1

my_string = "banana"
is_prefix = "nan"
print(solution(my_string, is_prefix)) # 0



'''
문자열 my_string과 정수 s, e가 매개변수로 주어질 때,
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]


my_string = "Progra21Sremm3"
s = 6
e = 12
print(solution(my_string, s, e)) # "ProgrammerS123"

my_string = "Stanley1yelnatS"
s = 4
e = 10
print(solution(my_string, s, e)) # "Stanley1yelnatS"