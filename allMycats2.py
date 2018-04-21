catNames = []
v = 0
while v < 6:
    print('Enter the name of cat' + str(v+1))
    try:
        catName = input()
        catNames.append(catName)
        v += 1
    except Exeception as err:
        print('Error message', err)

for names in catNames:
    print(names, end=' ')
