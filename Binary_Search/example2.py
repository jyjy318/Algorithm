from bisect import bisect_left
L,K,C = map(int, input().split())
cuts = list(map(int, input().split()))
cuts += [0,L]
cuts.sort()

def isPass(cuts, longest, c):
    cur = cuts[-1]
    while c>0:
        f = cur - longest
        if f<=0:
            return True, cuts[1]
        idx = bisect_left(cuts, f)
        if cur == cuts[idx]:
            return False, 0
        cur = cuts[idx]
        c -= 1
    if cur > longest:
        return False, 0
    return True, cur

#binary search
left, right = 0, L
while left+1 < right:
    mid = (left + right)//2
    r, fc = isPass(cuts, mid, C)
    if r:
        right = mid
        firstCut = fc
    else:
        left = mid
print(right, firstCut)
