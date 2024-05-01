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