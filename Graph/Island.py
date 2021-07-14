n, m = map(int, input().split())

def dfs(M, r, c):
	M[r][c] = 0
	dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
	for (dr, dc) in dxy:
		nr, nc = r + dr, c + dc
		# boundary check
		if nr < 0 or nr >= len(M): continue
		if nc < 0 or nc >= len(M[0]): continue
		# check can go there
		if M[nr][nc] == 0: continue
		# recursive call
		dfs(M, nr, nc)

M = [ [0]*m for _ in range(n) ]		# Make a multi-list sized nxm

for i in range(n):
	s = input()
	for j in range(m):
		if s[j] == "1": M[i][j] = 1

islands = 0
for i in range(n):
	for j in range(m):
		if M[i][j] == 0: continue
		islands += 1
		dfs(M, i, j)

print(islands)
