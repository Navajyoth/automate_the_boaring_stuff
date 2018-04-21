spam = ['apples', 'bananas', 'tofu', 'cats']
a = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
b = [1, 2, 3, 'Hello!']


def spam_Check(spam):
    try:
        spam.insert(len(spam) - 1, 'and')
        e = ''
        for i in spam:
            e += i
            e += ' '
        print(e)
    except Exception as Err:
        print('Please insert the proper list: ', Err)


spam_Check(['apples', 'bananas', 'tofu', 'cats'])
spam_Check(a)
spam_Check(b)
