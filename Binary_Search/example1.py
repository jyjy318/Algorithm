n = int(input())
office = list(map(int, input().split()))
left = 0
right = office[0]*n
while left+1 < right :  # 이웃화지 않은 경우
    mid = right + left //2
    pro = 0
    for o in office:
        pro += mid //o
    if pro >= n: #pass 한 경우
        right = mid # right 값을 mid로 설정
    else:
        left = mid
print(right)
