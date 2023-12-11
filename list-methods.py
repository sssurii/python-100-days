lst = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lst)

print(lst[3])
print(lst[:])
print(lst[2:]) #start from index 3
print(lst[2:5])
print(lst[2:10:2])

if 14 in lst:
    print("14 is in the list")
else:
    print("14 is not in the list")

#dynamic lists / list comprehension

lst = [i for i in range(10) if i%2==0 ]
print(lst)

lst = [i*i for i in range(10) if i%2==0 ]
print(lst)

lst.append(12)
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

print(lst.index(16))

nlst = lst  #make reference to original list
nlst[0] = 10
print(lst)

nlst = lst.copy()
nlst[1] = 8
print(lst)
print(nlst)

lst.insert(1, 64)
print(lst)

dlst = [i for i in range(20, 40) if i%2 == 0]
lst.extend(dlst)
print(lst)

dlst = dlst + lst
print(dlst)