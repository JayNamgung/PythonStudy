'''
2장 되새김문제(7)
'''
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


'''
2장 되새김문제(8)
'''
b = (1,2,3)
b = b + (4,)
print(b)

c = {1,2,3}
c.add(4)
c.update([5,6,7,8,9,10])
print(c)

'''
2장 되새김문제(9)
'''
d = dict()
d['name'] = 'python'
print(d)
d[('a', )] = 'python'
print(d)
#d[[1]] = 'python' #대괄호+대괄호는 사용 불가
d[250] = 'python'
print(d)

'''
2장 되새김문제(10)
'''
e = {'A':90, 'B':80, 'C':70}
result = e.pop('B')
print(e)
print(result)


'''
2장 되새김문제(11)
'''
f = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
fSet = set(f) #리스트를 집합화 & 중복제거
f = list(fSet) #집합을 리스트화
print(fSet)
print(f)

'''
2장 되새김문제(12)
'''
g = h = [1,2,3]
g[1] = 4
print(g)
print(h)