str1 = 'koshka-kartoshka'


def remove_characters(string, number):
    i = 0
    while i is not number:
        string = string.replace(string[0], '', 1)
        i += 1
    print(string)


def delete_characters(string, number):
    for i in range(number):
        string = string.replace(string[0], '', 1)
    print(string)


delete_characters(str1, 7)

#remove_characters(str1, 4)

