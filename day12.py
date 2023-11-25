import numpy as np
from collections import deque

with open('/Users/akselituominen/Desktop/AOC2022Day12','r') as file:
    lines = file.read().strip().split()
grid = [list(line) for line in lines]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == 'S':
            sr = r
            sc = c
            grid[r][c] = 'a'
        if item == 'E':
            er = r
            ec = c
            grid[r][c] = 'z'

q = deque()
q.append((0,sr,sc))

visited = {(sr,sc)}

while q:
    d,r,c = q.popleft()
    for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr,nc) in visited:
            continue
        if ord(grid[nr][nc])-ord(grid[r][c]) > 1:
            continue
        if nr == er and nc == ec:
            print(d+1)

        visited.add((nr,nc))
        q.append((d+1,nr,nc))

#Part II
#Lest do the same thing just starting from E and seaching for first a
q2 = deque()
q2.append((0,er,ec))
vis = {(er,ec)}
while q2:
    d,r,c = q2.popleft()
    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr,nc) in vis:
            continue
        if ord(grid[nr][nc])-ord(grid[r][c]) < -1:
            continue
        if grid[nr][nc] == 'a':
            print(d+1)
            exit(0)
        vis.add((nr,nc))
        q2.append((d+1,nr,nc))