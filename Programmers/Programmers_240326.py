'''
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다.
my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, index_list):
     return "".join(my_string[i] for i in index_list if 0 <= i < len(my_string))


my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
print(solution(my_string, index_list))  # "programmers"

my_string = "zpiaz"
index_list = [1, 2, 0, 0, 3]
print(solution(my_string, index_list)) # pizza



'''
음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.
'''
def solution(number):
    return sum(int(num) for num in number) % 9

number = "123"
print(solution(number)) # 6

number = "78720646226947352489"
print(solution(number)) # 2



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
   #return ''.join([my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:] for s, e in queries])


my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
print(solution(my_string, queries)) # "programmers"