'''
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = []

    for num in range(n+1):
        if num % 2 == 1:
            answer.append(num)
    return answer

print(solution(10))


'''
정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num, n):
    return 1 if num%n == 0 else 0

print(solution(98, 2))
print(solution(34, 3))



'''
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(number, n, m):
    return 1 if number%n == 0 and number%m == 0 else 0

print(solution(60, 2, 3))
print(solution(55, 10, 5))