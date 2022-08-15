# Program to write table:
# Using for:
num = int(input('Enter a number:'))
for i in range(0, 11):
    print(i*num)

# *If we do not take int in the print then it considers input as string
# And thus gives us a pattern instead of table as it repeats the string in for loop.

# Using while:
a = 1
b = int(input('Enter the number:'))
while a < 11:
    c = a * b
    a = a + 1
    print(c)
