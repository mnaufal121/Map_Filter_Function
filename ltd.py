list1 = ['jurusan', 'praktikum', 'kampus', 'tahun']
list2 = ['informatika', 'fungsional', 'UMM', '2020']

list = []
relist = []
dictionary = {}

# penerapan penggabungan 2 list pada 1 tuple
tuple = (list1[0].capitalize() + list2[0].capitalize(), list1[1].capitalize() + list2[1].capitalize(),
            list1[2].capitalize() + list2[2].capitalize(), list1[3].capitalize() + list2[3])
retuple = (list1[0].upper() + list2[0].upper(), list1[1].upper() + list2[1].upper(),
            list1[2].upper() + list2[2], list1[3].upper() + list2[3])

# penerapan penggabungan 2 list pada list dan dictionary
for i in range(4):
    plus = list1[i] + list2[i]
    list.append(plus)


# for i in range(4):
#     if(list2[i] == list2[2]):
#         list2[i] = list2[i].lower()
#     plus = list1[i] + list2[i]
#     relist.append(plus)

for i in range(4):
    dictionary[list1[i]] = list2[i]

print (list)
print (relist)
print (tuple)
print (retuple)
print (dictionary)
