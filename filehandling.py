'''
data = [1,2,3,4,5,4,3,5,6,4,4,3,3,3,4,5,67,7,98,67,6,8]

f = open("text.txt", "a")

for xvalue in data:
    record = str(xvalue)
    f.write(record)
    f.write("\n")

f.close()
'''

f = open("text.txt", "r")

for record in f:
    record = record.replace("\n", "")
    print(record)

f.close()