'''
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(a, b, c):
    return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3) if a == b == c else ((a + b + c) * (a**2 + b**2 + c**2) if a == b or b == c or a == c else a + b + c)

print(solution(2,6,1))
print(solution(5,3,3))
print(solution(4,4,4))



'''
정수가 담긴 리스트 num_list가 주어질 때,
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
'''
from functools import reduce

def solution(num_list):
    return 1 if sum(num_list) ** 2 > reduce(lambda x, y : x * y, num_list) else 0

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))



'''
정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    return int(''.join(map(str, filter(lambda x: x % 2, num_list)))) + int(''.join(map(str, filter(lambda x: not x % 2, num_list))))

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))