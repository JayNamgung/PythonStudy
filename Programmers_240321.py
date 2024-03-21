'''
정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.

변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.

만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성해 주세요.
'''
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for _ in range(len(answer)):
            if answer and answer[-1] >= arr[i]:
                answer.pop()
            else:
                break 
        answer.append(arr[i])
    return answer




'''
문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string, letter):
    return my_string.replace(letter, "")


my_string = "abcdef"
letter = "f"
print(solution(my_string, letter))

my_string = "BCBdbe"
letter = "B"
print(solution(my_string, letter))



'''
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
'''
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        return 0


angle = 70
print(solution(angle))

angle = 91
print(solution(angle))

angle = 180
print(solution(angle))




'''
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.
정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
'''
def solution(n, k):
    양꼬치_가격 = 12000
    음료수_가격 = 2000
    
    서비스_음료수 = n // 10
    지불_음료수 = max(k - 서비스_음료수, 0)
    
    총_금액 = (양꼬치_가격 * n) + (음료수_가격 * 지불_음료수)
    
    return 총_금액


n = 10
k = 3
print(solution(n,k))

n = 64
k = 6
print(solution(n,k))



'''
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
'''
def solution(n):
    return sum(num for num in range(2, n+1, 2))

n = 10
print(solution(n))

n = 4
print(solution(n))