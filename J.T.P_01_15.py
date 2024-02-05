print(abs(3))

print(abs(-3))

print(abs(-1.2))

print(all([1,2,3]))

print(all([1,2,3,0]))

print(all([]))

print(chr(97))

print(divmod(7,3))

print(7//3)

print(7%3)

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


print(eval('1+2'))

print(eval("'hi'+'a'"))

print(eval("'1'+'2'"))

b = input("Enter : ")
print(b)


print(list("python"))

c = input("Enter(2) : ")
print(list(c))


# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)



print(list(map(lambda a: a*2, [1, 2, 3, 4])))

print(list(range(5)))

print(list(range(1,5)))

print(list(range(1, 10, 2)))