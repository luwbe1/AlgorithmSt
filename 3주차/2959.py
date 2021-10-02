A, B, C, D = map(int, input().split()) # 거북이가 생각한 양의 정수 A,B,C,D 입력
turtle = [A, B, C, D] # 거북이
turtle.sort(reverse=True) # 정렬
print(turtle[1] * turtle[-1]) # 직사각형 넓이 구하기, 두 번째로 큰 수 x 제일 작은 수
