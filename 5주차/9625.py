K = int(input()) # 주어지는 K의 횟수

A = 0 # A의 개수
B = 1 # B의 개수 

for _ in range(1, K): # A는 B로 바뀌고, B는 A+B로 바뀐다.
    temp = A + B
    A = B 
    B = temp
    
print(A, B)
