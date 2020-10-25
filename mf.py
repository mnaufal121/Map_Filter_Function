enums = [8, 7, 4, 2, 8, 9]

# penerapan konsep map & filter function 
cubic = list(map(lambda x: x*x*x, enums))
morthan = list(filter(lambda x: x > 7, enums))

print(cubic)
print(morthan)

# penerapan yang tidak memakai map & filter function 
cubic1 = []
morthan1 = []

for enum in enums:
    x = enum*enum*enum
    cubic1.append(x)
    if enum > 70:
        morthan1.append(enum)

print(cubic1)
print(morthan1)