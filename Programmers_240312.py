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


def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))



'''
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(price):
    return int(price * 0.95) if price >= 100000 and price < 300000 else (int(price * 0.90) if price >= 300000 and price < 500000 else (int(price * 0.80) if price >= 500000 else int(price)))

print(solution(150000))
print(solution(5800000))



'''
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다.
아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(money):
    return [money // 5500, money % 5500]

print(solution(5500))
print(solution(15000))



'''
머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
'''
def solution(age):
    return 2022-int(age)+1

print(solution(40))
print(solution(23))



'''
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    return num_list[::-1]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))




'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
''' 
#index를 기준으로 switch
def solution(arr, queries):
    for i,j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
print(solution(arr, queries))