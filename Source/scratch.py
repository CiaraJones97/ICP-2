my_list = ["PHP", "Exercises", "Backend"]
count =[]
l_final = []
x = len(my_list)

for i in range(0,x):
    count.append(len(my_list[i]))

for i in range(0,x):
    l_final.append((count[i]),my_list[i])

l_final.sort()
print(l_final)


