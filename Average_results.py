import re
import numpy as np
from prettytable import PrettyTable

t = PrettyTable(['Name', 'Age'])
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])
print(t)

dataFile = "/home/nico/Scrivania/Log.txt"
exp = "[+-]?\d+\.\d+"     #r'^[+,\-]?[0-9]{1,3}$')
numbers = 18
class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
foldData = []
allData = []
z = 0
k = 1
with open(dataFile) as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        for s in re.findall(exp, line):
            foldData.append(float(s))
            z += 1
            if z == k * numbers:
                z == 0
                allData.append(foldData)
                foldData = []
                k += 1

average = []
for i in range(0, len(allData[0])):
    average.append(0)

for i in range(0, len(allData)):
    for j in range(0, len(allData[0])):
        average[j] += allData[i][j]

for i in range(0, len(average)):
    average[i] = round(average[i]/len(allData), 2)


print("\t\t\t\tprecison\trecall\tf1-score")
for i in range (0, len(class_names)):
    print("\n")
    print("\t{}\t\t{}\t\t\t{}\t\t{}".format(class_names[i], average[3*i], average[3*i], average[3*i+2]))
print(allData)
print(average)