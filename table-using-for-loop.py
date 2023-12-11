tbl = input("Please enter the number to print the table:")

for x in range(13):
    if (x == 0):
        continue

    if (x > 10):
        break
    print(tbl, "x", x, "=", int(tbl)*x)