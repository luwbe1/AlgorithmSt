hash = int(input()) # 문자열의 길이
string = list(input()) # 영문으로만 된 소문자 문자열(리스트로 했음)
answer = 0

for i in range(hash):
    answer += (ord(string[i])-96) * (31 ** i) #ord 함수
print(answer % 1234567891)
