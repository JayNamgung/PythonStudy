'''
5장 되새김문제(6)
'''
original_list = [1, 2, 3, 4]
result_list = list(map(lambda x: x*3, original_list))
print(result_list)


original_list_2 = [1, 2, 3, 4]
print(list(map(lambda x: x*3, original_list_2)))


original_list_3 = [1, 2, 3, 4]
print(list(map(lambda x: x*3, original_list_3)))


'''
5장 되새김문제(7)
'''
exercise_7 = [-8, 2, 7, 5, -3, 5, 0, 1]
min_value = min(exercise_7)
max_value = max(exercise_7)
sum_of_min_max = min_value + max_value
print(f"최솟값 : {min_value}, 최댓값 : {max_value}, 합 : {sum_of_min_max}")


min_value_2 = min(exercise_7)
max_value_2 = max(exercise_7)
sum_of_min_max_2 = min_value + max_value
print(f"최솟값_2 : {min_value_2}, 최댓값_2 : {max_value_2}, 합_2 : {max_value_2}")



'''
5장 되새김문제(8)
'''
print(round(17/3,4))



'''
5장 되새김문제(9)
'''
import os

# C:\doit 디렉터리로 이동
target_directory = r"C:\Users\nk_jw\Desktop\Git\PythonStudy"
os.chdir(target_directory)

# 현재 작업 디렉터리 확인
print(f"현재 작업 디렉터리: {os.getcwd()}")


'''
5장 되새김문제(10)
'''
import glob

# C:\doit 디렉터리 내의 .py 파일들을 찾아서 리스트로 반환
py_files = glob.glob(r"C:\Users\nk_jw\Desktop\Git\PythonStudy\*.py")

# 찾은 파일들을 출력
for file in py_files:
    print(file)



'''
5장 되새김문제(11)
'''
import time

# 현재 날짜와 시간을 가져옵니다.
current = time.localtime()

# 현재 날짜와 시간 출력 (년-월-일 시:분:초)
print(f"현재 날짜와 시간: {time.strftime('%Y/%m-%d %H:%M:%S', current)}")

# 현재 날짜 출력 (년, 월, 일)
print(f"현재 날짜: {time.strftime('%Y/%m-%d', current)}")

# 현재 시간 출력 (시, 분, 초)
print(f"현재 시간: {time.strftime('%H:%M:%S', current)}")



'''
5장 되새김문제(12)
'''
import random

def generate_lotto_numbers():
    # 중복되지 않은 6개의 난수 생성
    lotto_numbers = random.sample(range(1, 46), 6)
    return lotto_numbers

# 로또 번호 생성
lotto_result = generate_lotto_numbers()
print(f"로또 번호: {lotto_result}")