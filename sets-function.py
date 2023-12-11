s = set()
print(s)

set1 = {'2', 2, 4, '4'}
print(set1)

set1 = {'2', '2', '4', '4'}
print(set1)

#set functions

set1 = {'2', '4',}
set2 = {'2', '5', '7',}

print(set1.union(set2))
print(set1.issuperset(set2))

set1.update(set2)
print(set1)
print(set1.issuperset(set2))
print(set2.issubset(set1))

set1 = {'2', '4',}
set2 = {'2', '5', '7',}
print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)

set1 = {'2', '4',}
set2 = {'2', '5', '7',}

print(set1.difference(set2))
print(set1.symmetric_difference(set2))

set1.add('9')
print(set1)

print(set1.pop())

if '7' in set2:
    print("7 present in set")
else:
    print("7 is not present in set")