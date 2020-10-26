numbers = []
numbers1 = []

# inputan bersifat dinamis, dengan list dalam list
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
    for j in range(len(numbers[i])):
        kuadrat = pow(numbers[i][j], 2)
        temp1.append(kuadrat)
    numbers1.append(temp1)

print(numbers)
print(numbers1)

# inputan manual, dengan list didalam tuple
# numbers = ([1, 7], [2, 0], [4, 5])

# for x in range(len(numbers)):
#     for y in range(2):
#         numbers[x][y] = numbers[x][y] * numbers[x][y]

# for x in range(len(numbers)):
#     for y in range(2):
#         numbers[x][y] *= 2

# for x in range(len(numbers)):
#     for y in range(2):
#         numbers[x][y] += 2

# print (numbers)

# catatan : untuk menggunakan program ini sebaiknya salah satu dikomen atau dihapus
