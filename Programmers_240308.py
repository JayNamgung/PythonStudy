'''
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(n):
    if n % 2 == 0:
        return sum(i ** 2 for i in range(2, n+1, 2))
    else:
        return sum(i for i in range(1, n+1, 2))

print(solution(7))



'''
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

두 수가 n과 m이라면
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다.
그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(ineq, eq, n, m):
    return int(eval(f"{str(n) + ineq + eq.replace('!', '') +str(m)}"))

print(solution("<", "=", 20, 50))
print(solution(">", "!", 41, 78))



'''
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(a, b, flag):
    return int(a+b) if flag else a-b

print(solution(-4, 7, "true"))
print(solution(-4, 7, "false"))


'''
머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
'''
def solution(n):
    return (n//7) + (1 if n%7 != 0 else 0)

print("================================")
print(solution(7))
print(solution(1))
print(solution(15))




'''
머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다.
피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
'''
import math

def solution(n):
    return n//6 if n%6 == 0 else n*6//math.gcd(n,6)//6

print("================================")
print(solution(6))  #1
print(solution(10)) #5
print(solution(4))  #2



'''
머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
'''
import math

def solution(slice, n):
    return n//slice if n%slice == 0 else n//slice+1

print("================================")
print(solution(7, 10))  #2
print(solution(4, 12))  #3



'''
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
'''
import numpy as np
def solution(numbers):
    return np.median(numbers)

print("================================")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))                #5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))   #94.0