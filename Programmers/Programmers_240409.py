'''
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를
순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if char.isupper():
            answer[ord(char) - ord('A')] += 1
        else:
            answer[ord(char) - ord('a') + 26] += 1
    return answer

my_string = "Programmers"
print(solution(my_string)) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]



'''
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
'''
def solution(n, k):
    return [i for i in range(1, n+1) if i % k == 0]

n = 10
k = 3
print(solution(n,k)) # [3, 6, 9]

n = 15
k = 5
print(solution(n, k)) # [5, 10, 15]



'''
문자열 my_string과 정수 배열 indices가 주어질 때,
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, indices):
    my_string_list = list(my_string)
    indices_sorted = sorted(indices, reverse=True)
    for i in indices_sorted:
        del my_string_list[i]
    return ''.join(my_string_list)

my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]
print(solution(my_string, indices)) # "programmers"



'''
정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(start, end_num):
    return list(range(start, end_num - 1, -1))

start_num = 10
end_num = 3

print(solution(start_num, end_num)) # [10, 9, 8, 7, 6, 5, 4, 3]