a = 3
b = 5
c = 9
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a, b, c)
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
print(a, b, c)