N, M = map(int, input().split()) #첫째줄 카드 N,M
num = list(map(int, input().split())) #둘째줄 카드에 쓰여있는 수
answer = 0 #답
for i in range(N): #모든 경우의 수를 확인하는 for문 시작
    for j in range(i+1, N):
        for k in range(j+1, N):
            if(num[i] + num[j] + num[k] > M): #합이 m을 넘으면 넘어감
                continue
            else:
                answer = max(answer, num[i] + num[j] + num[k])
print(answer)
