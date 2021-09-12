import sys
input = sys.stdin.readline
 
n = int(input()) # 막대 입력
sticks = [int(input()) for i in range(n)] # for문
max = sticks[-1] #최대 높이
count = 1
 
for i in range(n): #for문 시작
    now = sticks.pop() #현재
    if max < now: #최대 높이가 현재보다 작으면
        count += 1 #하나 더 카운트
        max = now #최대높이는 현재로 맞춤
print(count)
