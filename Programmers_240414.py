'''
정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다.
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.

n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]
    else:
        return []


n = 3
slicer = [1, 5, 2]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]	
print(solution(n, slicer, num_list)) # [2, 3, 4, 5, 6]

n = 4
slicer = [1, 5, 2]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution(n, slicer, num_list)) # [2,4,6]


'''
정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요.
음수가 없다면 -1을 return합니다.
'''
def solution(num_list):
    try:
        # index(next~~) : 음수인 값을 찾는 표현식
        return num_list.index(next(num for num in num_list if num < 0))
    except StopIteration:
        # 더 이상 try문 진행이 되지 않을 경우 stop되는 역할
        return -1

num_list = [12, 4, 15, 46, 38, -2, 15]
print(solution(num_list)) # 5

num_list = [13, 22, 53, 24, 15, 6]
print(solution(num_list)) # -1


'''
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다.
닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.
'''
def solution(arr, intervals):
    first_interval = arr[intervals[0][0]:intervals[0][1] + 1]
    second_interval = arr[intervals[1][0]:intervals[1][1] + 1]
    return first_interval + second_interval

arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]
print(solution(arr, intervals)) # [2, 3, 4, 1, 2, 3, 4, 5]

'''
정수 배열 arr가 주어집니다.
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
단, arr에 2가 없는 경우 [-1]을 return 합니다.
'''
def solution(arr):
    has_2 = False
    # left : 배열의 마지막 인덱스 초기값 설정
    # right : 배열의 첫 번째 인덱스보다 작은 값으로 초기값 설정
    left, right = len(arr), -1

    for i, num in enumerate(arr):
        if num == 2:
            has_2 = True
            left = min(left, i) # left : 2가 있는 가장 작은 인덱스
            right = max(right, i) # right : 2가 있는 가장 큰 인덱스

    if has_2:
        return arr[left:right + 1]
    else:
        return [-1]

arr = [1, 2, 1, 4, 5, 2, 9]
print(solution(arr)) # [2, 1, 4, 5, 2]

arr = [1, 2, 1]
print(solution(arr)) # [2]

arr = [1, 1, 1]
print(solution(arr)) # [-1]

arr = [1, 2, 1, 2, 1, 10, 2, 1]
print(solution(arr)) # [2, 1, 2, 1, 10, 2]


'''
정수 배열 arr와 query가 주어집니다.

query를 순회하면서 다음 작업을 반복합니다.

짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.
'''
def solution(arr, query):
    for i, idx in enumerate(query):
        if i % 2 == 0:
            arr = arr[:idx] + arr[idx:idx+1]
        else:
            arr = arr[idx:]
    return arr

arr = [0, 1, 2, 3, 4, 5]
query = [4, 1, 2]
print(solution(arr, query)) # [1, 2, 3]


'''
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    vowels = set('aeiou')
    # 각 문자를 소문자로 변환 후, vowels 집합에 포함되는지 체크
    answer = ''.join(char for char in my_string if char.lower() not in vowels)
    return answer

my_string = "bus"
print(solution(my_string)) # "bs"

my_string = "nice to meet you"
print(solution(my_string)) # "nc t mt y"


'''
문자열 my_string이 매개변수로 주어질 때,
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
'''
def solution(my_string):
    numbers = [int(char) for char in my_string if char.isdigit()]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

my_string = "hi12392"
print(solution(my_string)) # [1, 2, 2, 3, 9]

my_string = "p2o4i8gj2"
print(solution(my_string)) # [2, 2, 4, 8]

my_string = "abcde0"
print(solution(my_string)) # [0]


'''
문자열 my_string이 매개변수로 주어집니다.
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    numbers = [int(char) for char in my_string if char.isdigit()]
    total_sum = sum(numbers)
    return total_sum

my_string = "aAb1B2cC34oOp"
print(solution(my_string)) # 10

my_string = "1a2b3c4d123"
print(solution(my_string)) # 16


'''
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다.
따라서 12의 소인수는 2와 3입니다.
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = set()
    num = 2
    while n > 1:
        while n % num == 0:
            answer.add(num)
            n //= num
        num += 1
    return sorted(answer)

n = 12
print(solution(n)) # [2, 3]

n = 17
print(solution(n)) # [17]

n = 420
print(solution(n)) # [2, 3, 5, 7]



'''
정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list, n):
    return num_list[n-1:]


num_list = [2, 1, 6]
n = 3
print(solution(num_list, n)) # [6]

num_list = [5, 2, 1, 7, 5]
n = 2
print(solution(num_list, n)) # [2, 1, 7, 5]


'''
정수 리스트 num_list와 정수 n이 주어질 때,
num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠
n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list, n):
    return num_list[n:] + num_list[:n]

num_list = [2, 1, 6]
n = 1
print(solution(num_list, n)) # [1, 6, 2]

num_list = [5, 2, 1, 7, 5]
n = 3
print(solution(num_list, n)) # [7, 5, 5, 2, 1]



'''
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를,
먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"l"이나 "r"이 없다면 빈 리스트를 return합니다.
'''
def solution(str_list):
    pivot_char = None
    pivot_idx = None
    result_group = []
    for idx, char in enumerate(str_list):
        # 문자 i, r 찾기
        if char in ["l", "r"]:
            pivot_char = char
            pivot_idx = idx
            break
    # pivot_idx에 l,r이 있을 경우
    if pivot_idx is not None:
        if pivot_char == "l":
            result_group = str_list[:pivot_idx]
        else:
            result_group = str_list[pivot_idx + 1:]
    return result_group


str_list = ["u", "u", "l", "r"]
print(solution(str_list)) # ["u", "u"]

str_list = ["l"]
print(solution(str_list)) # []


'''
정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list, n):
    if n <= 0 or n > len(num_list):
        return []
    else:
        return num_list[:n]


num_list = [2, 1, 6]
n = 1
print(solution(num_list, n)) # [2]

num_list = [5, 2, 1, 7, 5]
n = 3
print(solution(num_list, n)) # [5, 2, 1]


'''
정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list, n):
    if n <= 0:
        return []
    else:
        result = []
    for i in range(len(num_list)):
      if i % n == 0:
        result.append(num_list[i])
    return result

num_list = [4, 2, 6, 1, 7, 6]
n = 2
print(solution(num_list, n)) # [4, 6, 7]

num_list = [4, 2, 6, 1, 7, 6]
n = 4
print(solution(num_list, n)) # [4, 7]


'''
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(s):
    answer = 0
    s_list = list(s.split())
    for i in range(len(s_list)):
        if s_list[i] == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(s_list[i])
    return answer


s = "1 2 Z 3"
print(solution(s)) # 4

s = "10 20 30 40"
print(solution(s)) # 100

s = "10 Z 20 Z 1"
print(solution(s)) # 1

s = "10 Z 20 Z"
print(solution(s)) # 0

s = "-1 -2 -3 Z"
print(solution(s)) # -3