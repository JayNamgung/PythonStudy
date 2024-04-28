'''
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
'''
def solution(numbers):
    dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, digit in dict.items():
        numbers = numbers.replace(word, digit)
    return int(numbers)

numbers = "onetwothreefourfivesixseveneightnine"
print(solution(numbers)) # 123456789

numbers = "onefourzerosixseven"
print(solution(numbers)) # 14067


'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    return "".join(my_list)

my_string = "hello"
num1 = 1
num2 = 2
print(solution(my_string, num1, num2)) # "hlelo"

my_string = "I love you"
num1 = 3
num2 = 6
print(solution(my_string, num1, num2)) # "I l veoyou"



'''
문자열 s가 매개변수로 주어집니다.
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
'''
def solution(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    unique_chars = [char for char, count in char_count.items() if count == 1]
    unique_chars.sort()
    
    return "".join(unique_chars)


s = "abcabcadc"
print(solution(s)) # "d"

s = "abdc"
print(solution(s)) # "abcd"

s = "hello"
print(solution(s)) # "echo"


'''
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
    return answer

n = 24
print(solution(n)) # [1, 2, 3, 4, 6, 8, 12, 24]

n = 29
print(solution(n)) # [1,29]