import sys
input = sys.stdin.readline
 
n = int(input()) #입력

for i in range(1,n+1): #for문 돌리기
    words = list(input().split()) #리스트로 받기
    print('Case #%d: %s' %(i, ' '.join(words[::-1])))
