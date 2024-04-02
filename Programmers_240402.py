'''
문자열 my_string과 두 정수 m, c가 주어집니다.
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, m, c):
    chunks = [my_string[i:i + m] for i in range(0, len(my_string), m)]
    column_chars = [chunk[c - 1] for chunk in chunks if len(chunk) >= c]
    return ''.join(column_chars)


my_string = "ihrhbakrfpndopljhygc"
m = 4
c = 2
print(solution(my_string, m, c)) # happy



my_string = "programmers"
m = 1
c = 1
print(solution(my_string, m, c)) # "programmers"



'''
두 정수 q, r과 문자열 code가 주어질 때,
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(q, r, code):
    answer = ""
    for i, char in enumerate(code):
        if i % q == r:
            answer += char
    return answer


q = 3
r = 1
code = "qjnwezgrpirldywt"
print(solution(q,r,code)) # "jerry"

q = 1
r = 0
code = "programmers"
print(solution(q,r,code)) # "programmers"