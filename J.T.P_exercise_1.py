'''
2장 되새김문제(1)
'''

list = { '국어': 80, '영어':75, '수학':55}

print(round((list['국어'] + list['영어'] + list['수학']) / 3))


'''
2장 되새김문제(2)
'''
a = 13
if a%2 == 0:
    print("짝수")
else:
    print("홀수")


'''
2장 되새김문제(3)
'''
pin = "881020-1068234"
yyyymmdd = pin[0:6]
num = pin[7:16]

print(yyyymmdd)
print(num)


'''
2장 되새김문제(4)
'''
pin = "881020-1068234"
print(pin[7])


'''
2장 되새김문제(5)
'''
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


'''
2장 되새김문제(6)
'''
c = [1, 3, 5, 4, 2]
c.sort()
c.reverse()
print(c)