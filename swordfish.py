while True:
    print("who are you?")
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe what is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
