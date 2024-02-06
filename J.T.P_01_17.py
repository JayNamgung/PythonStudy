import datetime
import time
import math
import random
import itertools

'''
표준 라이브러리 - date
'''
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

print(day1)
print(day2)

diff = day2 - day1
diff.days

print(diff.days)

'''
표준 라이브러리 - datetime
'''

day = datetime.date(2021, 12, 14)
print(day.weekday())
print(day.isoweekday())

print(time.time())
print(time.asctime())

print(math.gcd(60, 100, 80))

print(math.lcm(15, 25))

print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 55))

'''
로또번호 추출하기
'''
it = itertools.combinations(range(1, 46), 6)

'''
for num in it:
    print(num)
'''

'''
경우의 수 추출
'''
print(len(list(itertools.combinations(range(1, 46), 6))))