'''
정수 리스트 num_list가 주어집니다.
가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
두 값이 같을 경우 그 값을 return합니다.
'''
def solution(num_list):
    odd_sum = 0
    even_sum = 0

    for i, num in enumerate(num_list):
        if i % 2 == 0:  # 홀수 번째 원소
            odd_sum += num
        else:  # 짝수 번째 원소
            even_sum += num

    return max(odd_sum, even_sum)


num_list = [4, 2, 6, 1, 7, 6]
print(solution(num_list)) # 17

num_list = [-1, 2, 5, 6, 3]
print(solution(num_list)) # 8



'''
최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때,
앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요.
마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.
'''
def solution(names):
    grouped_names = []
    group_size = 5

    for i in range(0, len(names), group_size):
        group = names[i:i + group_size]
        grouped_names.append(group[0])  # 가장 앞에 있는 사람의 이름 추가

    return grouped_names


names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
print(solution(names)) # ["nami", "vex"]


'''
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(todo_list, finished):
    unfinished = []
    
    # 배열 순회
    for task, is_finished in zip(todo_list, finished):
        if not is_finished:
            unfinished.append(task)
    return unfinished



todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]
print(solution(todo_list, finished)) # ["practiceguitar", "studygraph"]


'''
정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(numbers, n):
    sum = 0
    for num in numbers:
        sum += num
        if sum > n:
            break
    return sum

# 예시 사용
numbers = [1, 2, 3, 4, 5]
n = 10
result = solution(numbers, n)
print(result)  # 15 (1 + 2 + 3 + 4 + 5 = 15)



numbers = [34, 5, 71, 29, 100, 34]
n = 123
print(solution(numbers, n)) # 139

numbers = [58, 44, 27, 10, 100]
n = 139
print(solution(numbers, n)) # 239