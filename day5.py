with open('/Users/akselituominen/Desktop/AOC2022Day5','r') as file:
    string = file.read().strip().split('move')

moves = string[1:]
stringi = '''[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]'''
# Columns as python lists
split_stringi = stringi.split('\n')
cols = []
try:
    for i in range(1, 100, 4):
        cols.append([r[i] for r in split_stringi])
except IndexError:
    pass

stacks = [
    list("".join(cols[0]).strip()[::-1]),
    list("".join(cols[1]).strip()[::-1]),
    list("".join(cols[2]).strip()[::-1]),
    list("".join(cols[3]).strip()[::-1]),
    list("".join(cols[4]).strip()[::-1]),
    list("".join(cols[5]).strip()[::-1]),
    list("".join(cols[6]).strip()[::-1]),
    list("".join(cols[7]).strip()[::-1]),
    list("".join(cols[8]).strip()[::-1])
]
#Part I
numbers = [[int(word) for word in move.split() if word.isdigit()] for move in moves]
for number in numbers:
    amount = number[0]
    start = number[1] - 1  # Subtract 1 because list indices start at 0
    end = number[2] - 1  # Subtract 1 because list indices start at 0

    # Use the start and end indices to access the correct stacks
    for _ in range(amount):
        movable = stacks[start].pop()
        stacks[end].append(movable)

print(stacks)

# Part II
for number in numbers:
    amount = number[0]
    start = number[1] - 1  # Subtract 1 because list indices start at 0
    end = number[2] - 1  # Subtract 1 because list indices start at 0
    movables = []
    # Use the start and end indices to access the correct stacks
    for _ in range(amount):
        movable = stacks[start].pop()
        movables.append(movable)
    for _ in range(amount):
        stacks[end].append(movables.pop())

print(stacks)