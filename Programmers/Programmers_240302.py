'''
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
import math

def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1 #분자
    denominator = denom1 * denom2 #분모
    
    #최대공약수
    divisor = math.gcd(numerator, denominator)

    #최종결과 세팅
    numerator = numerator / divisor
    denominator = denominator / divisor

    return numerator, denominator



'''
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(numbers):
    return [i*2 for i in numbers]