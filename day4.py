with open('/Users/akselituominen/Desktop/AOC2022Day4','r') as file:
    pairs = file.read().strip().split('\n')

#Part II, Part I very similiar
answer = 0
for pair in pairs:
    pair1, pair2 = pair.split(',')
    pair1_1, pair1_2 = map(int, pair1.split('-'))
    pair2_1, pair2_2 = map(int, pair2.split('-'))
    if (pair1_1 <= pair2_2) and (pair1_2 >= pair2_1):
        answer = answer + 1
print(answer)
