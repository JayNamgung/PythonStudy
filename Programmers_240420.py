'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
'''
def solution(arr, queries):
  n = len(arr)

  diff = [0] * (n + 1)
  for query in queries:
    s, e = query
    diff[s] += 1
    diff[e + 1] -= 1

  for i in range(1, n):
    diff[i] += diff[i - 1]
  for i in range(n):
    arr[i] += diff[i]

  return arr


arr = [0, 1, 2, 3, 4]
queries = [[0, 1],[1, 2],[2, 3]]

print(solution(arr, queries)) # [1, 3, 4, 4, 4]



'''
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(array, n):

  # 정렬 기준 함수 (거리, 값 순)
  def sort_key(num):
    distance = abs(num - n)
    return (distance, num)

  return sorted(array, key=sort_key)[0]

array = [3, 10, 28]
n = 20
print(solution(array, n)) # 28

array = [10, 11, 12]	
n = 13
print(solution(array, n)) # 12


'''
머쓱이는 친구들과 369게임을 하고 있습니다.
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
'''
def solution(order):
    answer = 0
    order = list(str(order))
    for i in order:
        if i in "369":
            answer += 1
    return answer

order = 3
print(solution(order)) # 1

order = 29423
print(solution(order)) # 2



'''
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(cipher, code):
  
    cipher_length = len(cipher)
    decrypted_message = ""

    for i in range(0, cipher_length, code):
        # 마지막 글자 추출
        if i + code <= cipher_length:
            last_character = cipher[min(i + code - 1, cipher_length - 1)]
            decrypted_message += last_character

    return decrypted_message

cipher = "dfjardstddetckdaccccdegk"	
code = 4
print(solution(cipher, code)) # "attack"

cipher = "pfqallllabwaoclk"
code = 2
print(solution(cipher, code)) # "fallback"



'''
문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    converted_string = ""

    for char in my_string:
        if char.isupper():
            converted_char = char.lower()
        else:
            converted_char = char.upper()
        converted_string += converted_char
    return converted_string


my_string = "cccCCC"
print(solution(my_string)) # "CCCccc"

my_string = "abCdEfghIJ"
print(solution(my_string)) # "ABcDeFGHij"