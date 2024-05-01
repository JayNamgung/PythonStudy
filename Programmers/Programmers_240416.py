'''
문자열 my_string이 매개변수로 주어집니다.
my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    set_string = set()
    answer = ""
    for char in my_string:
        if char not in set_string:
            set_string.add(char)
            answer += char
    return answer

my_string = "people"
print(solution(my_string)) # "peol"

my_string = "We are the world"
print(solution(my_string)) # "We arthwold"


'''
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
'''
def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2
    

sides = [1, 2, 3]
print(solution(sides)) # 2

sides = [3, 6, 2]
print(solution(sides)) # 2

sides = [199, 72, 222]
print(solution(sides)) # 1