numbers1 = [10, 20, 30, 40, 10]
numbers2 = [10, 20, 30, 40, 10, 80]


def comparing_elements(list):
    if list[0] == list[-1]:
        print('true')
    else:
        print('false')

def comparing_elements_with_return(list):
    if list[0] == list[-1]:
        return True
    else:
        return False

def stepen(number, stepen):
    return number ** stepen


# result1 = comparing_elements(numbers2)
# result2 = comparing_elements_with_return(numbers2)
important_number = stepen(3, 7)
result3 = important_number - 3
print(result3)

# print("Result1 is", result1)
# print("Result2 is", result2)

