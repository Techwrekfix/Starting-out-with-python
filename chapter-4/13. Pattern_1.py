#This program used nested loops to display this pattern

for rows in range(8,1,-1):
    for colums in range(rows- 1):
        print('*',end='')
    print()


