list1 = ['jurusan', 'praktikum', 'kampus', 'tahun']
list2 = ['informatika', 'fungsional', 'UMM', '2020']

list = []
tuple = (list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3])
dictionary = {}

for i in range(0, 4):
    plus = list1[i] + list2[i]
    list.append(plus)
    dictionary[list1[i]] = list2[i]

print (list)
print (tuple)
print (dictionary) 