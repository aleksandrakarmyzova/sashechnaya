import copy

n1 = '548'
list1 = list(n1)
list2 = copy.copy(list1)
list2.reverse()
if list1 == list2:
    print('это палиндром')
else:
    print('это не палиндром')
