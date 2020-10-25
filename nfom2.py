numbers = ([1, 7], [2, 0], [4, 5])

# for x in range(len(numbers)):
#     for y in range(2):
#         numbers[x][y] = numbers[x][y] * numbers[x][y]

for x in range(len(numbers)):
    for y in range(2):
        numbers[x][y] *= 2

for x in range(len(numbers)):
    for y in range(2):
        numbers[x][y] += 2

print (numbers)