'''
정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서
그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    last_element = num_list[-1]   #마지막 원소 추출
    second_element = num_list[-2] #마지막 전 원소 추출

    if last_element > second_element:
        return num_list + [last_element - second_element]
    else:
        return num_list + [last_element * 2]
    

num_list = [2, 1, 6]
num_list_2 = [5, 2, 1, 7, 5]

print(solution(num_list))
print(solution(num_list_2))




'''
정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며,
control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.

위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.
'''
def basic_day6_2(n, control):
    for idx,str in enumerate(control):
        if str == "w":
            n += 1
        elif str == "s":
            n -= 1
        elif str == "d":
            n += 10
        elif str == "a":
            n -= 10
    return n

n = 0
control = "wsdawsdassw"

print(basic_day6_2(n, control)) #result : -1