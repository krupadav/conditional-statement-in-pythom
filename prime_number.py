# Prime number
while True:
    a = int(input('Enter a number:'))
    if (a == 2) and (a == 3) and (a == 5) and (a == 7) and (a == 11):
        print('Number is prime')
    elif not(a % 2 == 0) and not(a % 3 == 0) and not(a % 5 == 0) and not(a % 7 == 0) and not(a % 11 == 0):
        print('Number is prime')
    else:
        print('Number is not prime')
