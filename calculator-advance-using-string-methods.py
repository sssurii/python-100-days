# a = 3
# b = 2
inpt = input('Enter an operation i.e. 3 + 5: ')
st = inpt.split(" ")
a = int(st[0])
o = st[1]
b = int(st[2])

r = 'na'

if (o == '+'):
    r = a + b
elif (o == '-'):
    r = a - b
elif (o == '*'):
    r = a * b
elif (o == '/'):
    r = a / b
else:
    print("Please enter a valid operation")

# match (o)
#     case '+':
#         r = a + b
#     case '-':
#         r = a - b
#     case '*' :
#         r = a * b
#     case '/' :
#         r = a / b
#     case _:
#         print("Please enter a valid operation")


if (r != 'na'):
    print('Result of', inpt, 'is:', r)