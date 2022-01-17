str1 = 'pynative'
for character in str1:
    index = str1.index(character)
    if not index % 2:
        print(character)

