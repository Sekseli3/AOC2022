#part1
with open ('/Users/akselituominen/Desktop/AOC2022Day2', 'r') as file:
    rounds = file.read().strip().split('\n')
pointMap = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}
total = sum(pointMap[round] for round in rounds if round in pointMap)
            
print(total)


#part2
with open ('/Users/akselituominen/Desktop/AOC2022Day2', 'r') as file:
    rounds = file.read().strip().split('\n')
pointMap = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}
total = sum(pointMap[round] for round in rounds if round in pointMap)

print(total)