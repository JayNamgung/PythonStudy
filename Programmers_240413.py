'''
정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다.
정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.
'''
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

arr = [0, 0, 0, 1]
idx = 1
print(solution(arr, idx)) # 3

arr = [1, 0, 0, 1, 0, 0]
idx = 3
print(solution(arr, idx)) # -1

arr = [1, 1, 1, 1, 0]
idx = 3
print(solution(arr, idx)) # 3



'''
약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
  if n <= 1:
    return 0

  # True : 소수
  # False : 소수가 아님
  is_prime = [True] * (n + 1) # 2부터 시작
  is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

  # 소수 찾기 및 배수 처리
  for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
      for j in range(i * 2, n + 1, i):
        is_prime[j] = False

  # 합성수 Count (전체 - 소수)
  answer = 0
  for i in range(2, n + 1):
    if is_prime[i]:
      answer += 1

  return n - answer - 1

n = 10
print(solution(n)) # 5

n = 15
print(solution(n)) # 8


'''
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
'''
def solution(numbers):
    # 내림차순으로 정렬
    numbers.sort(reverse=True)
    # 가장 큰 두 수를 곱한 값을 return
    return numbers[0] * numbers[1]

numbers = [1, 2, 3, 4, 5]
print(solution(numbers)) # 20

numbers = [0, 31, 24, 10, 1, 9]
print(solution(numbers)) # 744



'''
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    i = 1
    # 팩토리얼은 초기값 1부터 시작
    factorial = 1
    # factorial 값이 처음으로 n보다 커지는 순간을 찾을 때까지 반복
    while factorial <= n:
        i += 1
        factorial *= i
    # while문을 빠져나올 경우, i값이 n보다 작거나 같은 가장 큰 정수
    return i - 1

n = 3628800
print(solution(n)) # 10

n = 7
print(solution(n)) # 3