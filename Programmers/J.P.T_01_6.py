'''
2024.01.24
'''

a = [1,2,3,'TEST']

print("(1) "+"="*40)
print(a.index("TEST"))
print("="*44)
'''
OUTPUT : 3
'''

print()
print("(2) "+"="*40)
print(a.index(3))
print("="*44)
'''
OUTPUT : 2
'''

b = [1,2,3,1,2,3]
b.remove(3)
print()
print("(3) "+"="*40)
print(b)
print("="*44)
'''
OUTPUT : [1, 2, 1, 2, 3]
맨 앞의 '3'만 제거됨
두 번쨰 '3'도 제거하기 위해선 rmove 한 번 더 호출해야함
'''

c = [1,2,3,3,3,3,3,3,3,3]
print()
print("(4) "+"="*40)
print(c.count(3))
print("="*44)
'''
OUTPUT : 8
'''

d = []
d.extend(a)
d.extend(b)
d.extend(c)
print()
print("(5) "+"="*40)
print(d)
print("="*44)
'''
OUTPUT : [1, 2, 3, 'TEST', 1, 2, 1, 2, 3, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
'''

s1 = set([1,2,3])
l1 = list(s1)
s2 = set(l1)
print()
print("(6) "+"="*40)
print(s1)
print(l1)
print(s2)
print("="*44)
'''
{1, 2, 3}
[1, 2, 3]
{1, 2, 3}
'''

print()
print("(7) "+"="*40)
print(s1 | s2)
print(s1.union(s2))
print(s1&s2)
print(s1 - s2)
print("="*44)
'''
{1, 2, 3}
{1, 2, 3}
{1, 2, 3}
set() -- 차집합 결과가 null이면 set() 출력됨
'''

if s1-s2==set():
    print("TEST")
'''
차집합 결과가 null임을 확인하기 위해선 s1-s2==set() 조건식을 넣어야함
'''