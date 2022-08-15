#Sum of even number:
a = int(input('Enter initial value:'))
add = 0
while a < 100:
    if a % 2 == 0:
        add = add + a
        a = a + 2
print(add)

#Sum of odd number:
a = int(input('Enter initial value:'))
add = 0
while a < 100:
    if not(a % 2 == 0):
        add = add + a
        a = a + 2
print(add)
