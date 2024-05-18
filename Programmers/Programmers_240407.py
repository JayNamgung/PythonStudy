'''
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(numbers, direction):
    n = len(numbers)

    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    else:
        return numbers[1:] + numbers[:1]
    

numbers = [1,2,3]
direction = "right"
print(solution(numbers, direction)) # [3,1,2]

numbers = [4, 455, 6, 4, -1, 45, 6]
direction = "left"
print(solution(numbers, direction)) # [455, 6, 4, -1, 45, 6, 4]



'''
머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다.
상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때,
상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(box, n):
    box.sort()
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer


box = [1,1,1]
n = 1
print(solution(box,n)) # 1

box = [10,8,6]
n = 3
print(solution(box, n)) # 12