dic = {
    "surinder": "surinder is a name",
    "Age": "in years"
}

print(dic)

print(dic['Age'])

item = {
    "name": "surinder",
    "age": "31yrs",
    "eligible": False,
}

# print(item)
# print(item['name'])
# print(item.get('name'))
# print(item.keys())
# print(item.values())
# print(item.items())

# for key in item.keys():
#     print(f"{key}: {item[key]}")

for key, value in item.items():
    print(f"{key}: {value}")


dic1 = item
print(dic1)

dic1.update(dic)
print(dic1)

#dic1.clear()
print(dic1.pop('surinder'))
print(dic1)
print(dic1.popitem())
print(dic1)

del dic1['eligible']
print(dic1)


