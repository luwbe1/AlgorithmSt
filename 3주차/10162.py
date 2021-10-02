T = int(input()) # 요리시간 T 입력 받기
A=0 # 모두 다 0
B=0
C=0
if T % 10 != 0: # T초를 맞출 수 없을 땐 -1
    print(-1)
else: # A,B,C 계산
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)
