import numpy as np
#Part I
def simulate_motions(file_path):
    grid = np.zeros((500, 500))
    head = [0, 0]
    tail = [0, 0]
    grid[tail[0], tail[1]] = 1

    with open(file_path, 'r') as file:
        motions = file.readlines()

    for motion in motions:
        direction, amount = motion[0], int(motion[2:])
        for _ in range(amount):
            if direction == 'U':
                head[0] -= 1
            elif direction == 'D':
                head[0] += 1
            elif direction == 'L':
                head[1] -= 1
            elif direction == 'R':
                head[1] += 1

            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                if head[0] > tail[0]:
                    tail[0] += 1
                elif head[0] < tail[0]:
                    tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                elif head[1] < tail[1]:
                    tail[1] -= 1
                grid[tail[0], tail[1]] = 1

    return np.sum(grid)

print(simulate_motions('/Users/akselituominen/Desktop/AOC2022Day9'))

#Part II
def simulate_motionsII(file_path):
    grid = np.zeros((500, 500))
    #List of coordinates of the knots
    coords = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
              [0,0],[0,0]]
    #Mark start as visited
    grid[coords[9][0],coords[9][1]] = 1

    with open(file_path, 'r') as file:
        motions = file.readlines()

    for motion in motions:
        direction, amount = motion[0], int(motion[2:])
        for _ in range(amount):
            if direction == 'U':
                coords[0][0] -= 1
            elif direction == 'D':
                coords[0][0] += 1
            elif direction == 'L':
                coords[0][1] -= 1
            elif direction == 'R':
                coords[0][1] += 1

            for i in range(1,10):
                if abs(coords[i-1][0] - coords[i][0]) > 1 or abs(coords[i-1][1] - coords[i][1]) > 1:
                    if coords[i-1][0] > coords[i][0]:
                        coords[i][0] += 1
                    elif coords[i-1][0]< coords[i][0]:
                        coords[i][0] -= 1
                    if coords[i-1][1] > coords[i][1]:
                        coords[i][1] += 1
                    elif coords[i-1][1] < coords[i][1]:
                        coords[i][1] -= 1
                    grid[coords[9][0], coords[9][1]] = 1
  
    return np.sum(grid)
print(simulate_motionsII('/Users/akselituominen/Desktop/AOC2022Day9'))
