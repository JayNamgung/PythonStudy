'''
알파벳으로 이루어진 문자열 myString이 주어집니다.
모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
'''
def solution(myString):
    return myString.upper()

'''
알파벳으로 이루어진 문자열 myString이 주어집니다.
모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
'''
def solution(myString):
    return myString.lower()

'''
문자열 배열 strArr가 주어집니다.
모든 원소가 알파벳으로만 이루어져 있을 때,
배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로,
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.
'''
def solution(strArr):
    return [str.lower() if i%2 == 0 else str.upper() for i,str in enumerate(strArr)]


strArr = ["AAA","BBB","CCC","DDD"]
print(solution(strArr)) # ["aaa","BBB","ccc","DDD"]

strArr = ["aBc","AbC"]
print(solution(strArr)) # 	["abc","ABC"]


'''
문자열 myString이 주어집니다.
myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
'''
def solution(myString):
    answer = ""
    for char in myString:
        if char == 'a':
            answer += 'A'
        elif char.isupper() and char != 'A':
            answer += char.lower()
        else:
            answer += char
    return answer



myString = "abstract algebra"
print(solution(myString)) # "AbstrAct AlgebrA"

myString = "PrOgRaMmErS"
print(solution(myString)) # "progrAmmers"


'''
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때,
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, alp):
    if len(alp) != 1 or not alp.islower():
        raise ValueError("ERROR !")

    upper_alp = alp.upper()
    modified_string = ""

    for char in my_string:
        if char == alp:
            modified_string += upper_alp
        else:
            modified_string += char
    return modified_string

my_string = "programmers"
alp = "p"
print(solution(my_string, alp)) # "Programmers"

my_string = "lowercase"
alp = "x"
print(solution(my_string, alp)) # "lowercase"



'''
문자열 myString과 pat가 주어집니다.
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
'''
def solution(myString, pat):
    # pat의 길이
    pat_len = len(pat)

    # 가장 긴 부분 문자열의 길이를 저장할 변수
    max_len = 0

    # 가장 긴 부분 문자열을 저장할 변수
    max_substring = ''

    # myString의 모든 부분 문자열 탐색
    for i in range(len(myString)):
        for j in range(i + 1, len(myString) + 1):
            substring = myString[i:j]
            if substring.endswith(pat):
                if len(substring) > max_len:
                    max_len = len(substring)
                    max_substring = substring

    return max_substring

myString = "AbCdEFG"
pat = "dE"
print(solution(myString, pat)) # 	"AbCdE"

myString = "AAAAaaaa"	
pat = "a"
print(solution(myString, pat)) # "AAAAaaaa"



'''
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
'''
def solution(myString, pat):
    count = 0
    pat_len = len(pat)
    for i in range(len(myString) - pat_len + 1):
        if myString[i:i+pat_len] == pat:
            count += 1
    return count



'''
문자열 배열 strArr가 주어집니다.
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
'''
def solution(strArr):
    answer = []
    for s in strArr:
        if "ad" not in s:
            answer.append(s)
    return answer


'''
단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string):
    return my_string.split()

my_string = "i love you"
print(solution(my_string)) # ["i", "love", "you"]

my_string = "programmers"
print(solution(my_string)) # ["programmers"]



'''
단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''
import re

def solution(my_string):
    answer = re.split(r'\s+', my_string.strip())
    return answer

my_string = " i    love  you"
print(solution(my_string)) # ["i", "love", "you"]

my_string = "    programmers  "
print(solution(my_string)) # ["programmers"]


'''
머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다.
할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며,
편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(message):
    length = 0
    for char in message:
        if char.isalnum() or char in "!~":  # 알파벳, 숫자, '!', '~' 인 경우
            length += 2  # 가로 2cm 크기로 계산
        else:  # 공백 문자인 경우
            length += 1  # 가로 1cm 크기로 계산
    return length+1

message = "happy birthday!"
print(solution(message)) # 30

message = "I love you~"
print(solution(message)) # 22


'''
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(array):
    max_num = max(array)
    max_idx = array.index(max_num)
    return [max_num, max_idx]

array = [1, 8, 3]
print(solution(array)) # [8, 1]

array = [9, 10, 11, 8]	
print(solution(array)) # [11, 2]


'''
my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''
def solution(my_string):
    
    tokens = my_string.split()
    result = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i+1])
        
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        elif op == "*":
            result *= num
        else:  # op == "/"
            result //= num
    
    return result


'''
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer



'''
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
'''
def solution(n):
    n_str = str(n)
    sum_of_digits = 0
    for digit in n_str:
        sum_of_digits += int(digit)
    return sum_of_digits


'''
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(quiz):
    answer = []
    for q in quiz:

        values = q.split()
        x = int(values[0])
        op = values[1]
        y = int(values[2])
        z = int(values[4])

        if op == "+":
            result = x + y
        else:
            result = x - y
        
        if result == z:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer