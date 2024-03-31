'''
가위는 2 바위는 0 보는 5로 표현합니다.
가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
'''
def solution(rsp):
    answer = ""
    for r in rsp:
        if r == "2":
            answer += "0"
        elif r == "0":
            answer += "5"
        elif r == "5":
            answer += "2"
    return answer


rsp = "2"
print(solution(rsp)) # "0"

rsp = "205"
print(solution(rsp)) # "052"


'''
머쓱이는 구슬을 친구들에게 나누어주려고 합니다.
구슬은 모두 다르게 생겼습니다.
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때,
balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
'''
def solution(balls, share):
    import math
    return math.comb(balls, share)


balls = 3
share = 2
print(solution(balls, share))

balls = 5
share = 3
print(solution(balls, share))




'''
문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다.
이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.
'''

def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        substring = intStr[s:s + l]
        num = int(substring)
        if num > k:
            answer.append(num)
    return answer

intStrs = ["0123456789","9876543210","9999999999999"]
k = 50000
s = 5
l = 5

print(solution(intStrs, k, s, l)) # [56789, 99999]



'''
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_strings, parts):
  answer = ""
  for i in range(len(my_strings)):
    s, e = parts[i]
    answer += my_strings[i][s:e+1]
  return answer

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]

print(solution(my_strings, parts))



'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, n):
  if n >= len(my_string):
    return my_string
  else:
    return my_string[-n:]

my_string = "ProgrammerS123"	
n = 11
print(solution(my_string, n))

my_string = "He110W0r1d"
n = 5
print(solution(my_string, n))



'''
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, is_suffix):
  if len(is_suffix) > len(my_string):
    return 0
  elif len(is_suffix) == len(my_string):
    return my_string == is_suffix
  else:
    return my_string[-len(is_suffix):] == is_suffix

my_string = "banana"
is_suffix = "ana"
print(solution(my_string, is_suffix))

is_suffix = "nan"
print(solution(my_string, is_suffix))