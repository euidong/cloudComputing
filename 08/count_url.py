
file = open("5GB.txt", 'r')

urls = {}

for line in file.readlines():
    if line in urls:
        urls[line] += 1
    else:
        urls[line] = 1
file.close()

for item in urls.items():
    print(item[0] + "       " + str(item[1]))
