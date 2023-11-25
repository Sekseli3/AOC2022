from collections import defaultdict


with open('/Users/akselituominen/Desktop/AOC2022Day7','r')as file:
    lines = file.read().strip().split('\n')

#Create dictionary path with value of size of the directory and subdirectories
dirs = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        size = int(words[0])
        #add files size to the current dirs size and the size of all parents
        for i in range(1,len(path)+1):
            dirs['/'.join(path[:i])] += size

#Part II 
max_used = 70000000-30000000
total_used = dirs['/']
need_to_free = total_used - max_used

best = 1e9
ans = 0
for key,value in dirs.items():
    if value >= need_to_free:
        best = min(best,value)
    if value <= 100000:
        ans += value
print(ans)
print(best)