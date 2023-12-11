# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

str = input("Please add your message:")
encode = input("Do you want to encode or decode:")
encode = True if encode == "encode" else False
print(str)
newStr = []
if encode:
    words = str.split(" ")
    for word in words:
        if len(word) >= 3:
            prefix = 'srt'
            suffix = 'dne'
            word = prefix + word[1:] + word[0:1] + suffix
        else:
            word = word[::-1]
        newStr.append(word)
else:
    words = str.split(" ")
    for word in words:
        if len(word) >= 3:
            prefix = 'srt'
            suffix = 'dne'
            word = word[3:-3]
            word = word[-1:] + word[:-1]
        else:
            word = word[::-1]
        newStr.append(word)

print(" ".join(newStr))