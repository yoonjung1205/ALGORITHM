from itertools import combinations

example = []
score = 0
for i in range(9):
    shape, color, b_color = input().split()
    example.append([shape,color,b_color])
example.insert(0,0)

# 정답구하기
case = list(combinations(range(1,10),3))
solution = []
for i in range(len(case)):
    e1,e2,e3 = case[i]
    # 모양 다 같던지 다 다르던지
    if example[e1][0] == example[e2][0] == example[e3][0] or \
            (example[e1][0] != example[e2][0] and example[e2][0] != example[e3][0] and example[e1][0] != example[e3][0]):
        # 색깔 다 같던지 다 다르던지
        if example[e1][1] == example[e2][1] == example[e3][1] or \
                (example[e1][1] != example[e2][1] and example[e2][1] != example[e3][1] and example[e1][1] != example[e3][1]):
            # 배경 다 같던지 다 다르던지
            if example[e1][2] == example[e2][2] == example[e3][2] or \
                    (example[e1][2] != example[e2][2] and example[e2][2] != example[e3][2] and example[e1][2] != example[e3][2]):
                solution.append([e1,e2,e3])

# print(solution)

n = int(input())
history = [''] * n
my_solution = []
flag = 0
for i in range(n):
    player_input = input()
    if player_input[0] == 'H':
        mode, a,b,c = player_input.split()
        choice = sorted([int(a),int(b),int(c)])
        # print(choice)
        if choice not in history:
            if choice in solution:
                score += 1
                my_solution.append(choice)
            else:
                score -= 1
        else:
            score -= 1
        history[i] = choice
    else:
        if len(my_solution) == len(solution) and flag == 0:
            score += 3
            flag = 1
        else:
            score -= 1
print(score)

