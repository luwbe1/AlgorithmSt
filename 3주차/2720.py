import sys

T=int(sys.stdin.readline()) # T 입력

# 쿼터, 다임, 니켈, 페니
for _ in range(T): 
    money = int(sys.stdin.readline()) # 돈 
    a = money // 25 # 25
    money %=25
    b = money // 10 # 10
    money %=10
    c = money // 5 # 5
    money %=5
    d = money
    print(a,b,c,d)
