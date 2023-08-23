a = 10
for i in range(1, 6):
    for j in range(1, a):
        print(end=" ")
    a = a - 2
    for j in range(1, i+1):
        print(i,"", end="")
    print()