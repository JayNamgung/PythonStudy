'''
5장 되새김문제(13)
'''
import datetime

# 시작 날짜와 종료 날짜 정의
start_date = datetime.datetime(1995, 11, 20)
end_date = datetime.datetime(1998, 10, 6)

# 시간 간격 계산
time_interval = end_date - start_date

# 결과 출력
print(f"시작 날짜: {start_date.date()}")
print(f"종료 날짜: {end_date.date()}")
print(f"시간 간격: {time_interval.days} 일")


'''
5장 되새김문제(14)
'''
import operator

data = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.83),
        ('이성호', 17.7),
        ('김옥순', 16.71),
        ('황민지', 17.65),
        ('김영철', 16.7),
        ('주병철', 15.67),
        ('박상현', 14.16),
        ('김영순', 14.81),
        ('오지아', 15.13),
        ('윤지은', 16.93),
        ('문재호', 16.39)]

data = sorted(data, key=operator.itemgetter(1))

for d in data:
    print(f"14번 문제 : {d}")

    
'''
5장 되새김문제(15)
'''
from itertools import combinations

students = ["나지혜", "성성민", "윤지현", "김정숙"]
num_cleaners = 2

cleaner_combinations = list(combinations(students, num_cleaners))

print(f"{num_cleaners}명의 청소 당번을 뽑을 수 있는 경우의 수:")
for combo in cleaner_combinations:
    print(", ".join(combo))


import itertools

students_2 = ['나지혜', '성성민', '윤지현', '김정숙']
result = itertools.combinations(students_2, 2)
print(list(result))
for combo in result:
    print(combo)

'''
5장 되새김문제(16)
'''
a = "abcd"
result_2 = itertools.permutations(a, 4)
len_a = 0

for r in result_2:
    print(''.join(r))
    len_a+=1

print(f"경우의 수 : {len_a}")


'''
5장 되새김문제(17)
'''
import random
import itertools

people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
duty = ['청소', '빨래', '설거지']

random_people = random.sample(people, len(people))
result_3 = itertools.zip_longest(random_people, duty, fillvalue="휴식")

for n in result_3:
    print(n)



people_2 = ['김승현', '김진호', '강춘자', '이예준', '김현주']
duty_2 = ['청소', '빨래', '설거지']

random_people_2 = random.sample(people, len(people))
result_4 = itertools.zip_longest(random_people_2, duty_2, fillvalue="휴식")

for n in result_4:
    print(f"결과 : {n}")



'''
5장 되새김문제(18)
'''
import math

width = 200
height = 80

tile_size = math.gcd(width, height)
print(f"타일 한 선의 길이 : {tile_size}")

width_count = width/tile_size
height_count = height/tile_size

print(f"필요한 타일의 개수 : {int(width_count*height_count)}")