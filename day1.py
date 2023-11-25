sequence = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
# Python

# Open and read the file
with open('/Users/akselituominen/Desktop/AOC2022Day1', 'r') as file:
    parts = file.read().strip().split('\n\n')
# Initialize the maximum sums
max_sums = [0, 0, 0]

for part in parts:
    # Calculate the sum of the current part
    current_sum = sum(int(number) for number in part.split('\n'))

    # Update the maximum sums if necessary
    for i, max_sum in enumerate(max_sums):
        if current_sum > max_sum:
            max_sums.insert(i, current_sum)
            max_sums.pop()
            break
print(max_sums[1]+max_sums[2]+max_sums[0])
