list1 = ['jurusan', 'praktikum', 'kampus', 'tahun']
list2 = ['informatika', 'fungsional', 'UMM', '2020']


# penerapan penggabungan 2 list pada list
# opsi panjang
list = []
relist = []
for i in range(4):
    plus = list1[i] + list2[i]
    list.append(plus)

for i in range(4):
    if(list2[i] == list2[2]):
        list2[i] = list2[i].lower()
    plus = list1[i] + list2[i]
    relist.append(plus)

print(list)
print(relist)

# opsi pendek
# print(list(i + j for i, j in zip(list1, list2)))
# print(list(i + j.lower() for i, j in zip(list1, list2)))

# catatan : untuk menggunakan program ini sebaiknya salah satu dikomen atau dihapus

# penerapan penggabungan 2 list pada tuple

# opsi panjang
tuple = (list1[0].capitalize() + list2[0].capitalize(), list1[1].capitalize() + list2[1].capitalize(),
         list1[2].capitalize() + list2[2].capitalize(), list1[3].capitalize() + list2[3])
retuple = (list1[0].upper() + list2[0].upper(), list1[1].upper() + list2[1].upper(),
           list1[2].upper() + list2[2], list1[3].upper() + list2[3])

print(tuple)
print(retuple)

# opsi pendek
# print(tuple(i.title() + j.title() for i, j in zip(list1, list2)))
# print(tuple(i.upper() + j.upper() for i, j in zip(list1, list2)))

# catatan : untuk menggunakan program ini sebaiknya salah satu dikomen atau dihapus

# penerapan penggabungan 2 list pada dictionary

# opsi panjang
dictionary = {}

for i in range(4):
    dictionary[list1[i]] = list2[i]

print(dictionary)
# opsi lebih pendek
# print(dict(zip(list1, list2)))

# catatan : untuk menggunakan program ini sebaiknya salah satu dikomen atau dihapus
