n = int(input()) #카드 개수 입력 받기
cards = [i for i in range(1, n + 1)] 

while len(cards) > 1: #카드 개수가 1보다 클 때까지
    print(cards.pop(0), end=" ") #버리기
    cards.append(cards.pop(0)) #뒤로 옮기기
print(cards[0])
