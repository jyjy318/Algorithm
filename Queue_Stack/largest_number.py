n, k = map(int, input().split())
numbers = input()
stack = [ ]
n -= k
for c in numbers:
    while len(stack) > 0 and k > 0 and stack[-1] < c:
        stack.pop()
        k -= 1
    stack.append(c)
print(''.join(stack[:n]))
