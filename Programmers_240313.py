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



'''
정수 배열 numLog가 주어집니다.
처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.

그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다.
즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.
'''
def basic_day6_3_1(numLog):
    answer = []

    for idx, val in enumerate(numLog):
        compare_val = 0

        if idx != 0:
            compare_val = val - numLog[idx-1]
        if compare_val == 1:
            answer.append("w")
        elif compare_val == -1:
            answer.append("s")
        elif compare_val == 10:
            answer.append("d")
        elif compare_val == -10:
            answer.append("a")
    return "".join(answer)


def basic_day6_3_2(numLog):
    answer = ''
    data_dict = {1:"w", -1:"s", 10:"d", -10:"a"}

    for idx in range(1, len(numLog)):
        compare_val = numLog[idx] - numLog[idx - 1]
        answer += data_dict[compare_val]
    return answer


def basic_day6_3_3(numLog):
    answer = ''
    data_dict = {1:"w", -1:"s", 10:"d", -10:"a"}

    for idx, val in enumerate(numLog[1:], start=1):
        compare_val = val - numLog[idx - 1]

        if compare_val in data_dict:
            answer += data_dict[compare_val]
    return answer


numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(basic_day6_3_1(numLog)) #result : "wsdawsdassw"
print(basic_day6_3_2(numLog)) #result : "wsdawsdassw"
print(basic_day6_3_3(numLog)) #result : "wsdawsdassw"