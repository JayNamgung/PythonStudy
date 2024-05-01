'''
응용문제
'''

# add_multiple.py
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: 
        result += n
print(result)


i = 1
while i < 10:
    print(i)
    i = i + 1


# gugu.py
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(gugu(1))


for n in range(1, 1000):
    print(n)
    n += 1


def get_total_page(m,n):
    if m%n == 0:
        return m
    else:
        return m
    
print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))