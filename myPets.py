mypets = ['bounty', 'rocky', 'jimmy']
print('Enter the name of the pet: ')
name = input()
if name not in mypets:
    print('I do not have a pet named', name)
else:
    print(name, 'is my pet.')
