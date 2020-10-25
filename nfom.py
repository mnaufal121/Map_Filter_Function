numbers = []
numbers1 = []

input1 = input('Masukkan jumlah list yang ingin dimasukkan: ')
limit1 = int(input1)

input2 = input('Masukkan jumlah batas list dalam list : ')
limit2 = int(input2)

for x in range(0, limit1):
    temp = []
    for y in range(0, limit2):
        input3 = input('Masukkan angka : '.format(x))
        temp.append(int(input3))
    numbers.append(temp)

for i in range(len(numbers)):
    temp1 = []
    for j in range(2):
        x = numbers[i][j]
        kuadrat = x * x
        temp1.append(kuadrat)
    numbers1.append(temp1)

print (numbers)
print (numbers1)