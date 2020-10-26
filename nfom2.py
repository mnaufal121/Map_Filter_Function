numbers = ((1, 7), (2, 0), (4, 5))
plus = []
minus = []
devide = []
cubic = []

for x in range(len(numbers)):
    plus.append(list(numbers[x]))
    minus.append(list(numbers[x]))
    devide.append(list(numbers[x]))
    cubic.append(list(numbers[x]))
    for y in range(len(numbers[x])):
        plus[x][y] += 2
        minus[x][y] -= 2
        devide[x][y] /= 2
        cubic[x][y] = pow(cubic[x][y], 3)

print(numbers)
print(plus)
print(minus)
print(devide)
print(cubic)
