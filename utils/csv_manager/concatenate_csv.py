import csv
from os import listdir
from os.path import isfile, join
import random

in_folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video/fold_1/"
out_file_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video/fold_1/test.csv"

out_file = open(out_file_path, "w", newline='')
csv_writer = csv.writer(out_file, delimiter=",")
first_row = ["emotion", "image_name", "Usage"]
csv_writer.writerow(first_row)
files = [f for f in listdir(in_folder_path) if isfile(join(in_folder_path, f))]
rows = []
for i in range(0, len(files)):
    csv_path = in_folder_path + "/" + files[i]
    csv_file = open(csv_path)
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if row != first_row:
            rows.append(row)

random.shuffle(rows)

for i in range(0, len(rows)):
    csv_writer.writerow(rows[i])

print("Csv created")
