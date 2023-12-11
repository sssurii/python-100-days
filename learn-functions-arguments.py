def calculateAverage(a, b):
    avg = (a + b) / 2
    print("Average is :", avg)

calculateAverage(5, 6)

def calculateAverage(a = 5, b = 6):
    avg = (a + b) / 2
    print("Average is :", avg)

calculateAverage()


def calculateAverage(*numbers):  #tuple of numbers
    sum = 0
    for i in numbers:
        sum = sum + i
    avg = sum / len(numbers)

    print("Average is :", avg)

calculateAverage(5, 6, 7, 8)


def printName(**name): #dictionary of names
    print(name['firstName'], name['middleName'], name['lastName'])
    

printName(firstName = 'Surinder', middleName = '', lastName = 'Singh')


def calculateAverage(*numbers):  #tuple of numbers
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

print("Average is:", calculateAverage(5, 6, 7, 8))