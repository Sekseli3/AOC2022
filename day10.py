with open('/Users/akselituominen/Desktop/AOC2022Day10','r') as file:
    lines = file.read().strip().split('\n')
#cycle number
cycle = 0
#value of X
x = 1
ans = []
def printCycle(cycles):
    if cycles in [20, 60, 100, 140, 180, 220]:
        ans.append(x * cycles)
#Loop throuh the lines and check whether the command is addx or noop
for line in lines:
    if line[0] == 'a':
        cycle += 1
        printCycle(cycle)
        cycle += 1
        printCycle(cycle)
        x += int(line[5:])
    else:
        cycle += 1
        printCycle(cycle)
print(sum(ans))



#Part II
file_task_2 = open('/Users/akselituominen/Desktop/AOC2022Day10', 'r')

def execute_cycle_actions(cycle_count, x_register, lit_pixels):
    cycle_count += 1
    if x_register <= cycle_count <= x_register+2:
        lit_pixels.append(cycle_count - 1)
    if cycle_count == 40:
        for idx in range(40):
            print("#", end="") if idx in lit_pixels else print(".", end="")
        print()
        lit_pixels.clear()
        cycle_count = 0
    return cycle_count


def task_2(file):

    lit_pixels = []
    x_register = 1
    cycle_count = 0
    print("Task 2 result: ")
    for command in file.readlines():
        cycle_count = execute_cycle_actions(cycle_count, x_register, lit_pixels)
        if command.startswith("addx"):
            cycle_count = execute_cycle_actions(cycle_count, x_register, lit_pixels)
            x_register += int(command.split()[1])
task_2(file_task_2)