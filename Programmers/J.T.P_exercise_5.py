'''
5장 되새김문제(1)
'''
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
    
    def minus(self, val):
        self.value -= val


class UpgradeCalculator(Calculator):
    pass

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)



'''
5장 되새김문제(2)
'''
class Calculator2:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator2):
    pass

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)

print(cal2.value)


'''
5장 되새김문제(3)
'''
print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')


'''
5장 되새김문제(4)
'''
a = list(filter(lambda x:x > 0, [1, -3, 2, 0, -5, 6]))
print(a)


'''
5장 되새김문제(5)
'''
b = int(hex(234), 16)
print(b)