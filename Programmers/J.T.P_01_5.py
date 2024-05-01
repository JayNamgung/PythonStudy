a = {1: 'a'}
a[2] = 'b'
print("(1) "+"="*40)
print(a)
print("="*44)

'''
OUTPUT : {1: 'a, 2: 'b'}
'''

a['name'] = 'pey'

print("(2) "+"="*40)
print(a)
print("="*44)

'''
OUTPUT : {1: 'a', 2: 'b', 'name': 'pey'}
'''

del a[1]
print("(3) "+"="*40)
print(a)
print("="*44)

'''
OUTPUT : {2: 'b', 'name': 'pey'}
'''