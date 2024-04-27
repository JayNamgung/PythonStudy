'''
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        answer.append(sorted_emergency.index(emergency[i]) + 1)
    return answer

# 예시
emergency = [3, 76, 24]
print(solution(emergency)) # [3,1,2]

emergency = [1, 2, 3, 4, 5, 6, 7]
print(solution(emergency)) # [7, 6, 5, 4, 3, 2, 1]

emergency = [30, 10, 23, 6, 100]
print(solution(emergency)) # [2, 4, 3, 5, 1]



'''
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if i != j:
                count += 2
            else:
                count += 1
    return count

n = 20
print(solution(n)) # 6

n = 100
print(solution(n)) # 9




'''
개미 군단이 사냥을 나가려고 합니다.
개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다.
예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다.
사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
'''
def solution(hp):
    generals = hp // 5
    remaining_hp = hp % 5
    
    soldiers = remaining_hp // 3
    remaining_hp %= 3
    
    ants = remaining_hp
    
    return generals + soldiers + ants


hp = 23
print(solution(hp)) # 5

hp = 24
print(solution(hp)) # 6

hp = 999
print(solution(hp)) # 201



'''
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다.
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다.
문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
모스부호는 다음과 같습니다.

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
'''
def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    
    return ''.join(morse[a] for a in letter.split(" "))


letter = ".... . .-.. .-.. ---"
print(solution(letter)) # "hello"

letter = ".--. -.-- - .... --- -."
print(solution(letter)) # "python"