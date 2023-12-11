fl = open('/home/fnl/dev/Python-100-days/file-io/mytext.txt', 'r')
text = fl.read()
print(text)
fl.close()


fl = open('/home/fnl/dev/Python-100-days/file-io/mytext2.txt', 'w')
fl.write("Hello Surinder!")
fl.close()