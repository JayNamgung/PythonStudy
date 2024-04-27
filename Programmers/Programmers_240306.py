'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
최빈값이 여러 개면 -1을 return 합니다.
'''
from collections import Counter

def solution(array):
    freq_dict = Counter(array) #결과 : {"1":1,"2:1,"3":3,"4":1}
    
    max_freq = max(freq_dict.values()) #결과 : 3,2,1

    mode_values = [key for key, value in freq_dict.items() if value == max_freq] #결과 : [3],[1, 2],[1]

    if len(mode_values) > 1:
        return -1
    else:
        return mode_values[0]

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))