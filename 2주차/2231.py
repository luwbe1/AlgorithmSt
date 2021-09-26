N = int(input()) #입력
for i in range(1, N+1): #for문
    nlist = list(map(int,str(i))) #i의 각 자리수를 리스트에 넣음
    nsum = i+sum(nlist) #i와 각 자리수가 들어간 리스트를 더함
    if(nsum == N): #N과 비교
        print(i)
        break
    if(i == N): #없으면 0
        print(0)
