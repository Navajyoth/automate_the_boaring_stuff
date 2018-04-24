grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# to transpose a list in python3
# list(map(list, zip(*grid))))
# a = map(''.join, zip(*grid))
# for i in a:
#     print(i)
#     print('\n')

for i in range(len(grid[0])):
    print('\n')
    for j in range(len(grid)):
        print(grid[j][i], end='')
