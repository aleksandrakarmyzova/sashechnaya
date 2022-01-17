# a = 0
# b = 1
# print(a)
# print(b)
# c = 0
# i = 0
# while i < 11:
#     c = a + b
#     a = b
#     b = c
#     i += 1
#     print(c)


a = 0
b = 1
print(a)
print(b)
c = 0
for i in range(1, 11):
    c = a + b
    a = b
    b = c
    print(c)
