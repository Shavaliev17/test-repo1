list = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
list_repeat = []
for i in list:
    if list_repeat.count(i):
        print(i)
    else:
        list_repeat.append(i)
