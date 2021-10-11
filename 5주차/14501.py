N = int(input())

tlist = []
plist = []
dp = [0] * (n+1)

for i in range(n):
    t, p = map(int,input().split())
    tlist.append(t)
    plist.append(p)
    
for i in range(N-1, -1, -1): # n-1에서 시작해서 0까지 -1씩 빼준다.
    if tlist[i] + i > N: # 상담이 끝나는 날이 n을 넘기면 일을 할 수 없다.
        dp[i] = dp[i+1]
    else: # 일을 맡지 않을 경우
        # 지금 일 보상 + 다음날에 쌓여있는 보상
        dp[i] = max(dp[i+1], plist[i] + dp[i + tlist[i]]) # 맨 마지막 일부터 올 수 있는 가장 큰 값
        
print(dp[0])
