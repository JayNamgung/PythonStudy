'''
문자열 배열 strlist가 매개변수로 주어집니다.
strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
'''
def solution(strlist):
    return [len(s) for s in strlist]


strlist = ["We", "are", "the", "world!"]
print(solution(strlist)) # [2, 3, 3, 6]

strlist = ["I", "Love", "Programmers."]
print(solution(strlist)) # [1, 4, 12]