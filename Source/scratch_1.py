filename = open("input","r")
lines = filename.read()

text = list(lines.splitlines())

for i in range (0,len(text)):
    print(text[i], " ", len(text[i]))

outputfile = open("output", "w")
for i in range (0, len(text)):
    outputfile.write(text[i])
    outputfile.write(" , ")
    outputfile.write(str(len(text[i])))
    outputfile.write("\n")

