import re
import datetime

file = open("willis.txt")

data = file.read()

file.close()

print(data)

pattern = re.compile(r'''
                    (?P<start>[\d]+)
                    [\s]+
                    (?P<end>[\d]+)
                    [\s]+
                    (?P<value>[\d\.]+)
                    \n''', re.X)

datalist = re.findall(pattern, data)

print(len(datalist))
print(datalist[12][0])

out = open("data.csv", "w")

for line in datalist:
    writestring = ""
    date = datetime.datetime.strptime(line[0], "%Y%m%d")
    writestring += str(date)
    writestring += ";"
    if (float)(line[2]) > 1000:
        writestring += ""
    else:
        writestring += line[2]
    writestring += "\n"

    out.write(writestring)

out.close()
