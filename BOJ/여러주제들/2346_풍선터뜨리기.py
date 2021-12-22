# deque.rotate(num) : num>0 이면 오른쪽으로 num 만큼 밀어내기, num<0이면 왼쪽으로 num 만큼 밀어내기

from collections import deque
N = int(input())
balloon = list(map(int,input().split()))
new_balloon = deque()

# index랑 풍선안에 들어있는 값을 리스트로 받아서 deque에 넣어줌
for i in range(len(balloon)):
    new_balloon.append([i+1,balloon[i]])

# print(new_balloon)

while new_balloon:
    num, paper = new_balloon.popleft()
    # print(num,paper)
    print(num, end=" ")
    if paper > 0:
        new_balloon.rotate(-paper+1)
    else:
        new_balloon.rotate(-paper)
    # print(new_balloon)