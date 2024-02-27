'''
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))



'''
길이가 같은 두 문자열 str1과 str2가 주어집니다.

두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
'''
def solution(str1, str2):
    return "".join(str1 + str2 for str1, str2 in zip(str1, str2))

print(solution("aaaaa", "bbbbb"))