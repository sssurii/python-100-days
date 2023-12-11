# a = 3
# b = 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


a = input('Enter a number: ')
b = input('Enter another number: ')
o = input('Select the operation from below: \n 1 = + \n 2 = - \n 3 = x \n 4 = / \n')

operations = {'1' : '+', '2' : '-', '3' : 'x' , '4' : '/'}
r = 'na'

if (o == '1'):
    r = int(a) + int(b)
elif (o == '2'):
    r = int(a) - int(b)
elif (o == '3'):
    r = int(a) * int(b)
elif (o == '4'):
    r = int(a) / int(b)
else:
    print("Please enter a valid operation")

if (r != 'na'):
    print('Result of ', a, operations[o], b, 'is:', r)