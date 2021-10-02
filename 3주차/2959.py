A, B, C, D = map(int, input().split()) # A,B,C,D 입력
turtle = [A, B, C, D] # 거북이
turtle.sort(reverse=True) # 정렬
print(turtle[1] * turtle[-1]) # 직사각형 넓이 구하기
