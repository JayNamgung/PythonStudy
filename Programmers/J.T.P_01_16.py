'''
내장 함수
max ~ 
'''

print(max([1,2,3]))
print(max("python"))
print(max((1,2,3)))
print(max({1,2,3}))

print(min([1,2,3]))
print(min("python"))

print(oct(34))
print(oct(12345))

print(ord('a'))
print(ord('가'))

print(pow(2,4))
print(pow(3,3))

print(list(range(5)))
print(list(range(5, 10)))
print(list)

print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

print(round(4.6))
print(round(4.2))

print(round(5.678, 2))

print(sorted([3,1,2]))

print(str(3))
print(str('hi'))


'''
튜플 : 수정 불가능
'''
print(tuple("abc"))
print(tuple([1,2,3]))

print(list(zip([1,2,3], [4,5,6])))