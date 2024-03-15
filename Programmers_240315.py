'''
문자열 my_string이 매개변수로 주어집니다.
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    return my_string[::-1]


my_string = "jaron"
print(solution(my_string))
my_string = "bread"
print(solution(my_string))



'''
"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다.
정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
'''
n = int(input())
for i in range(1, n+1):
    print("*"*i)



'''
정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(num_list):
    return [sum(1 for num in num_list if num % 2 == 0), sum(1 for num in num_list if num %2 != 0)]

num_list = [1, 2, 3, 4, 5]
num_list_2 = [1, 3, 5, 7]

print(solution(num_list)) #[2,3]
print(solution(num_list_2)) #[0,4]



'''
문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(my_string, n):
    return ''.join([char*n for char in my_string])

my_string = "hello"
n = 3
print(solution(my_string, n)) #"hhheeellllllooo"



'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
'''
def basic_day7(arr, queries):
    for s,e,k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

print(basic_day7(arr, queries)) #[3, 2, 4, 6, 4]



'''
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서
숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
'''
def solution(l, r):
    num_list = []
    for num in range(l,r+1):
        if set(str(num)) <= {'0', '5'}:
            num_list.append(num)
    return num_list if num_list else [-1]

l = 5
r = 555

l2 = 10
r2 = 20

print(solution(l,r))
print(solution(l2,r2))