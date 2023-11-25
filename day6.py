#Part I and II very similiar, this is for part II
with open('/Users/akselituominen/Desktop/AOC2022Day6','r') as file:
    data = file.read()
print(data)
data2 = "nppdvjthqldpwncqszvftbrmjlhg"
marker = []
amount = 0
for char in data:
    amount += 1
    marker.append(char)
    if len(set(marker)) == 14:
        break
    elif len(marker) == 14:
        marker.remove(marker[0])
print(amount)
