# for number in range(0, 101):
#      if number is not 0 and not number % 5:
#          print(number)

def dividing_by_five(list):
    i = 0
    while i is not len(list):
        if not list[i] % 5:
            i += 1
        else:
            list.remove(list[i])
            i -= 1
    return list


list1 = [0, 3, 5, 6, 8, 10, 13, 15]
new_list = dividing_by_five(list1)
print(new_list)