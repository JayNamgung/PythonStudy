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