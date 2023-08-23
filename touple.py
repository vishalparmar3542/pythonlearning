lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst2 = []
lst3 = []

for x in range(len(lst)):
    lst2.append(lst[x][-1])


lst2.sort()

for x in lst2:
    for y in range(len(lst)):
        if x == lst[y][-1]:
            lst3.append(lst[y])

print(lst3)