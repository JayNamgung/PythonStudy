'''
표준 라이브러리
math
random
zip
traceback
'''

import math
print(math.lcm(15, 25))


# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))


# itertools_zip.py
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = zip(students, snacks)
print(list(result))


# itertools_zip.py
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))



list_1 = list(itertools.permutations([1,2,3,4,5],2))
print(list_1)



# itemgetter1.py
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result_2 = sorted(students, key=itemgetter(1))
print(result_2)


students2 = [
    {"name" : "jane", "age" : 22, "grade" : "A"},
    {"name" : "dave", "age" : 32, "grade" : "B"},
    {"name" : "sally", "age" : 17, "grade" : "C"}
]

result_3 = sorted(students2, key=itemgetter("age"))
print(result_3)




# traceback_test.py
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()