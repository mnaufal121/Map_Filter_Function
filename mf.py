enums = [8, 7, 4, 2, 8, 9]

# penerapan konsep map & filter function 
cubic = list(map(lambda x: x*x*x, enums))
morthan = list(filter(lambda x: x > 7, enums))

print(cubic)
print(morthan)

# penerapan yang tidak memakai map & filter function 

cubic2 = []
morthan2 = []

def cubic1(x):
    res = x*x*x
    cubic2.append(res)

def morthan1(x):
    if x > 7:
        morthan2.append(x)


for enum in enums:
    cubic1(enum)
    morthan1(enum)

print(cubic2)
print(morthan2)