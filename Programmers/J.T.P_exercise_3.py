'''
3장 되새김문제(1)
'''
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
else:
    print("none")



'''
3장 되새김문제(2)
'''
result = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result += i
    i += 1
print(result)



'''
3장 되새김문제(3)
'''
i = 0
while True:
    i += 1
    if i>5:
        break
    print(i*"*")



'''
3장 되새김문제(4)
'''
for i in range(1,101):
    print(i)



'''
3장 되새김문제(5)
'''
A = {70, 60, 55, 75, 95, 90, 80, 80, 85, 100}
total = 0
for score in A:
    total += score
average = total / len(A)
print(total)
print(average)


'''
3장 되새김문제(6)
'''
numbers = [1, 2, 3, 4, 5]
result1 = []
for n in numbers:
    if n % 2 == 1:
        result1.append(n * 2)
print(result1)

result2 = [n*2 for n in numbers if n%2 == 1]
print(result2)



'''
4장 되새김문제(1)
'''
def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_odd(4))
print(is_odd(3))



'''
4장 되새김문제(2)
'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))



'''
4장 되새김문제(3)
'''
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print(f"두 수의 합은 {total}입니다.")