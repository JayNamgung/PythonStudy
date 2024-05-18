'''
문자열 myString이 주어집니다.
myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
'''
def solution(myString):
    split_strings = myString.split("x")
    return [len(s) for s in split_strings]


'''
문자열 myString이 주어집니다.
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 빈 문자열은 반환할 배열에 넣지 않습니다.
'''
def solution(myString):
   # "x"를 기준으로 문자열 분리
   split_strings = myString.split("x")
   
   # 빈 문자열 제거
   split_strings = [s for s in split_strings if s != ""]
   
   # 사전순으로 정렬
   sorted_strings = sorted(split_strings)
   
   return sorted_strings



'''
문자열 binomial이 매개변수로 주어집니다.
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다.
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(binomial):
   # binomial을 공백을 기준으로 분리
   parts = binomial.split()
   
   # a, op, b 값 할당
   a = int(parts[0])
   op = parts[1]
   b = int(parts[2])
   
   # 연산 수행
   if op == "+":
       result = a + b
   elif op == "-":
       result = a - b
   elif op == "*":
       result = a * b
   
   return result


'''
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
'''
def solution(myString, pat):
   # myString의 "A"와 "B"를 치환한 새로운 문자열 생성
   new_string = ''.join(['B' if char == 'A' else 'A' for char in myString])
   
   # pat이 새로운 문자열에 포함되어 있는지 확인
   if pat in new_string:
       return 1
   else:
       return 0
   

'''
'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(rny_string):
   return rny_string.replace('m', 'rn')


'''
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
'''
def solution(myStr):
    separators = ['a', 'b', 'c']
    result = []
    start = 0
    
    for i in range(len(myStr)):
        if myStr[i] in separators:
            substring = myStr[start:i]
            if substring:
                result.append(substring)
            start = i + 1
    if start < len(myStr):
        substring = myStr[start:]
        if substring:
            result.append(substring)
    
    if not result:
        return ["EMPTY"]
    else:
        return result
    


'''
아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
양의 정수 배열 arr가 매개변수로 주어질 때,
arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(arr):
    X = []
    for num in arr:
        X.extend([num] * num)
    return X


'''
아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고,
flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(arr, flag):
   X = []
   for i in range(len(flag)):
       if flag[i]:
           X.extend([arr[i]] * (arr[i] * 2))
       else:
           X = X[:-arr[i]]
   return X



'''
0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.

i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.

만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.

단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.
'''
def solution(arr):
   stk = []
   i = 0
   while i < len(arr):
       if not stk:
           stk.append(arr[i])
           i += 1
       elif stk and stk[-1] == arr[i]:
           stk.pop()
           i += 1
       else:
           stk.append(arr[i])
           i += 1
   return stk if stk else [-1]


'''
랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다.
적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.

이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.

정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성해 주세요.

단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.
'''
def solution(arr, k):
    result = []
    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
            if len(result) == k:
                break

    if len(result) < k:
        result.extend([-1] * (k - len(result)))

    return result



'''
문자열 str1, str2가 매개변수로 주어집니다.
str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
'''
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2


'''
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
'''
import math

def solution(n):
    n = math.sqrt(n)
    if n.is_integer():
        return 1
    else:
        return 2
    

'''
어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
'''
def solution(n, t):
    bacteria_count = n  # 초기 세균 수
    for _ in range(t):
        bacteria_count *= 2  # 1시간마다 두 배 증식
    return bacteria_count


'''
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때,
my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(my_string):
    my_string = my_string.lower()
    char_list = list(my_string)
    char_list.sort()
    sorted_string = ''.join(char_list)
    return sorted_string


'''
머쓱이는 행운의 숫자 7을 가장 좋아합니다.
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
'''
def solution(array):
    count = 0
    for num in array:
        num_str = str(num)
        count += num_str.count('7')
    return count


'''
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_str, n):
    result = []
    for i in range(0, len(my_str), n):
        result.append(my_str[i:i+n])
    return result


'''
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
'''
def solution(array, n):
    count = 0
    for num in array:
        if num == n:
            count += 1
    return count


'''
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
'''
def solution(array, height):
    count = 0
    for h in array:
        if h > height:
            count += 1
    return count