import csv
import random

in_path = "/home/nico/Scrivania/Big data/Progetto/csv/total.csv"  # path al csv
out_folder_path = "/home/nico/Scrivania/Big data/Progetto/csv/"  # path alla cartella
out_files = ["folder_1", "folder_2", "folder_3", "folder_4", "folder_5", "folder_6", "folder_7", "folder_8", "folder_9", "folder_10"]
percentage = 10 #perchè 10 fold

images_0 = []
images_1 = []
images_2 = []
images_3 = []
images_4 = []
images_5 = []
images_6 = []
totals = [0, 0, 0, 0, 0, 0, 0]
in_file = open(in_path)
csv_reader = csv.reader(in_file, delimiter=",")

for row in csv_reader:
    class_id = row[0]
    if class_id != "emotion":
        if class_id == "0":
            images_0.append(row)
            totals[0] += 1
        elif class_id == "1":
            images_1.append(row)
            totals[1] += 1
        elif class_id == "2":
            images_2.append(row)
            totals[2] += 1
        elif class_id == "3":
            images_3.append(row)
            totals[3] += 1
        elif class_id == "4":
            images_4.append(row)
            totals[4] += 1
        elif class_id == "5":
            images_5.append(row)
            totals[5] += 1
        else:
            images_6.append(row)
            totals[6] += 1
images_0_folder_1 = []
images_1_folder_1 = []
images_2_folder_1 = []
images_3_folder_1 = []
images_4_folder_1 = []
images_5_folder_1 = []
images_6_folder_1 = []
images_0_folder_2 = []
images_1_folder_2 = []
images_2_folder_2 = []
images_3_folder_2 = []
images_4_folder_2 = []
images_5_folder_2 = []
images_6_folder_2 = []
images_0_folder_3 = []
images_1_folder_3 = []
images_2_folder_3 = []
images_3_folder_3 = []
images_4_folder_3 = []
images_5_folder_3 = []
images_6_folder_3 = []
images_0_folder_4 = []
images_1_folder_4 = []
images_2_folder_4 = []
images_3_folder_4 = []
images_4_folder_4 = []
images_5_folder_4 = []
images_6_folder_4 = []
images_0_folder_5 = []
images_1_folder_5 = []
images_2_folder_5 = []
images_3_folder_5 = []
images_4_folder_5 = []
images_5_folder_5 = []
images_6_folder_5 = []
images_0_folder_6 = []
images_1_folder_6 = []
images_2_folder_6 = []
images_3_folder_6 = []
images_4_folder_6 = []
images_5_folder_6 = []
images_6_folder_6 = []
images_0_folder_7 = []
images_1_folder_7 = []
images_2_folder_7 = []
images_3_folder_7 = []
images_4_folder_7 = []
images_5_folder_7 = []
images_6_folder_7 = []
images_0_folder_8 = []
images_1_folder_8 = []
images_2_folder_8 = []
images_3_folder_8 = []
images_4_folder_8 = []
images_5_folder_8 = []
images_6_folder_8 = []
images_0_folder_9 = []
images_1_folder_9 = []
images_2_folder_9 = []
images_3_folder_9 = []
images_4_folder_9 = []
images_5_folder_9 = []
images_6_folder_9 = []
images_0_folder_10 = []
images_1_folder_10 = []
images_2_folder_10 = []
images_3_folder_10 = []
images_4_folder_10 = []
images_5_folder_10 = []
images_6_folder_10 = []
out_file_names = [out_files[0] + ".csv", out_files[1] + ".csv", out_files[2] + ".csv", out_files[3] + ".csv", out_files[4] + ".csv", out_files[5] + ".csv", out_files[6] + ".csv", out_files[7] + ".csv", out_files[8] + ".csv", out_files[9] + ".csv"]
folder_1_rows = []
folder_2_rows = []
folder_3_rows = []
folder_4_rows = []
folder_5_rows = []
folder_6_rows = []
folder_7_rows = []
folder_8_rows = []
folder_9_rows = []
folder_10_rows = []
random.shuffle(images_0)
random.shuffle(images_1)
random.shuffle(images_2)
random.shuffle(images_3)
random.shuffle(images_4)
random.shuffle(images_5)
random.shuffle(images_6)
for i in range(0, len(images_0)):
    images_per_folder = int((percentage/100)*len(images_0))
    if i < images_per_folder:
        images_0_folder_1.append(images_0[i])
    elif i < 2*images_per_folder:
        images_0_folder_2.append(images_0[i])
    elif i < 3 * images_per_folder:
        images_0_folder_3.append(images_0[i])
    elif i < 4 * images_per_folder:
        images_0_folder_4.append(images_0[i])
    elif i < 5 * images_per_folder:
        images_0_folder_5.append(images_0[i])
    elif i < 6 * images_per_folder:
        images_0_folder_6.append(images_0[i])
    elif i < 7 * images_per_folder:
        images_0_folder_7.append(images_0[i])
    elif i < 8 * images_per_folder:
        images_0_folder_8.append(images_0[i])
    elif i < 9 * images_per_folder:
        images_0_folder_9.append(images_0[i])
    elif i < 10 * images_per_folder:
        images_0_folder_10.append(images_0[i])
    else:
        remaining = len(images_0) - i
        if remaining == 1:
            images_0_folder_1.append(images_0[i])
        elif remaining == 2:
            images_0_folder_2.append(images_0[i])
        elif remaining == 3:
            images_0_folder_3.append(images_0[i])
        elif remaining == 4:
            images_0_folder_4.append(images_0[i])
        elif remaining == 5:
            images_0_folder_5.append(images_0[i])
        elif remaining == 6:
            images_0_folder_6.append(images_0[i])
        elif remaining == 7:
            images_0_folder_7.append(images_0[i])
        elif remaining == 8:
            images_0_folder_8.append(images_0[i])
        elif remaining == 9:
            images_0_folder_9.append(images_0[i])

for i in range(0, len(images_1)):
    images_per_folder = int((percentage/100)*len(images_1))
    if i < images_per_folder:
        images_1_folder_1.append(images_1[i])
    elif i < 2 * images_per_folder:
        images_1_folder_2.append(images_1[i])
    elif i < 3 * images_per_folder:
        images_1_folder_3.append(images_1[i])
    elif i < 4 * images_per_folder:
        images_1_folder_4.append(images_1[i])
    elif i < 5 * images_per_folder:
        images_1_folder_5.append(images_1[i])
    elif i < 6 * images_per_folder:
        images_1_folder_6.append(images_1[i])
    elif i < 7 * images_per_folder:
        images_1_folder_7.append(images_1[i])
    elif i < 8 * images_per_folder:
        images_1_folder_8.append(images_1[i])
    elif i < 9 * images_per_folder:
        images_1_folder_9.append(images_1[i])
    elif i < 10 * images_per_folder:
        images_1_folder_10.append(images_1[i])
    else:
        remaining = len(images_1) - i
        if remaining == 1:
            images_1_folder_1.append(images_1[i])
        elif remaining == 2:
            images_1_folder_2.append(images_1[i])
        elif remaining == 3:
            images_1_folder_3.append(images_1[i])
        elif remaining == 4:
            images_1_folder_4.append(images_1[i])
        elif remaining == 5:
            images_1_folder_5.append(images_1[i])
        elif remaining == 6:
            images_1_folder_6.append(images_1[i])
        elif remaining == 7:
            images_1_folder_7.append(images_1[i])
        elif remaining == 8:
            images_1_folder_8.append(images_1[i])
        elif remaining == 9:
            images_1_folder_9.append(images_1[i])

for i in range(0, len(images_2)):
    images_per_folder = int((percentage/100)*len(images_2))
    if i < images_per_folder:
        images_2_folder_1.append(images_2[i])
    elif i < 2 * images_per_folder:
        images_2_folder_2.append(images_2[i])
    elif i < 3 * images_per_folder:
        images_2_folder_3.append(images_2[i])
    elif i < 4 * images_per_folder:
        images_2_folder_4.append(images_2[i])
    elif i < 5 * images_per_folder:
        images_2_folder_5.append(images_2[i])
    elif i < 6 * images_per_folder:
        images_2_folder_6.append(images_2[i])
    elif i < 7 * images_per_folder:
        images_2_folder_7.append(images_2[i])
    elif i < 8 * images_per_folder:
        images_2_folder_8.append(images_2[i])
    elif i < 9 * images_per_folder:
        images_2_folder_9.append(images_2[i])
    elif i < 10 * images_per_folder:
        images_2_folder_10.append(images_2[i])
    else:
        remaining = len(images_2) - i
        if remaining == 1:
            images_2_folder_1.append(images_2[i])
        elif remaining == 2:
            images_2_folder_2.append(images_2[i])
        elif remaining == 3:
            images_2_folder_3.append(images_2[i])
        elif remaining == 4:
            images_2_folder_4.append(images_2[i])
        elif remaining == 5:
            images_2_folder_5.append(images_2[i])
        elif remaining == 6:
            images_2_folder_6.append(images_2[i])
        elif remaining == 7:
            images_2_folder_7.append(images_2[i])
        elif remaining == 8:
            images_2_folder_8.append(images_2[i])
        elif remaining == 9:
            images_2_folder_9.append(images_2[i])

for i in range(0, len(images_3)):
    images_per_folder = int((percentage/100)*len(images_3))
    if i < images_per_folder:
        images_3_folder_1.append(images_3[i])
    elif i < 2 * images_per_folder:
        images_3_folder_2.append(images_3[i])
    elif i < 3 * images_per_folder:
        images_3_folder_3.append(images_3[i])
    elif i < 4 * images_per_folder:
        images_3_folder_4.append(images_3[i])
    elif i < 5 * images_per_folder:
        images_3_folder_5.append(images_3[i])
    elif i < 6 * images_per_folder:
        images_3_folder_6.append(images_3[i])
    elif i < 7 * images_per_folder:
        images_3_folder_7.append(images_3[i])
    elif i < 8 * images_per_folder:
        images_3_folder_8.append(images_3[i])
    elif i < 9 * images_per_folder:
        images_3_folder_9.append(images_3[i])
    elif i < 10 * images_per_folder:
        images_3_folder_10.append(images_3[i])
    else:
        remaining = len(images_3) - i
        if remaining == 1:
            images_3_folder_1.append(images_3[i])
        elif remaining == 2:
            images_3_folder_2.append(images_3[i])
        elif remaining == 3:
            images_3_folder_3.append(images_3[i])
        elif remaining == 4:
            images_3_folder_4.append(images_3[i])
        elif remaining == 5:
            images_3_folder_5.append(images_3[i])
        elif remaining == 6:
            images_3_folder_6.append(images_3[i])
        elif remaining == 7:
            images_3_folder_7.append(images_3[i])
        elif remaining == 8:
            images_3_folder_8.append(images_3[i])
        elif remaining == 9:
            images_3_folder_9.append(images_3[i])

for i in range(0, len(images_4)):
    images_per_folder = int((percentage/100)*len(images_4))
    if i < images_per_folder:
        images_4_folder_1.append(images_4[i])
    elif i < 2 * images_per_folder:
        images_4_folder_2.append(images_4[i])
    elif i < 3 * images_per_folder:
        images_4_folder_3.append(images_4[i])
    elif i < 4 * images_per_folder:
        images_4_folder_4.append(images_4[i])
    elif i < 5 * images_per_folder:
        images_4_folder_5.append(images_4[i])
    elif i < 6 * images_per_folder:
        images_4_folder_6.append(images_4[i])
    elif i < 7 * images_per_folder:
        images_4_folder_7.append(images_4[i])
    elif i < 8 * images_per_folder:
        images_4_folder_8.append(images_4[i])
    elif i < 9 * images_per_folder:
        images_4_folder_9.append(images_4[i])
    elif i < 10 * images_per_folder:
        images_4_folder_10.append(images_4[i])
    else:
        remaining = len(images_4) - i
        if remaining == 1:
            images_4_folder_1.append(images_4[i])
        elif remaining == 2:
            images_4_folder_2.append(images_4[i])
        elif remaining == 3:
            images_4_folder_3.append(images_4[i])
        elif remaining == 4:
            images_4_folder_4.append(images_4[i])
        elif remaining == 5:
            images_4_folder_5.append(images_4[i])
        elif remaining == 6:
            images_4_folder_6.append(images_4[i])
        elif remaining == 7:
            images_4_folder_7.append(images_4[i])
        elif remaining == 8:
            images_4_folder_8.append(images_4[i])
        elif remaining == 9:
            images_4_folder_9.append(images_4[i])

for i in range(0, len(images_5)):
    images_per_folder = int((percentage/100)*len(images_5))
    if i < images_per_folder:
        images_5_folder_1.append(images_5[i])
    elif i < 2 * images_per_folder:
        images_5_folder_2.append(images_5[i])
    elif i < 3 * images_per_folder:
        images_5_folder_3.append(images_5[i])
    elif i < 4 * images_per_folder:
        images_5_folder_4.append(images_5[i])
    elif i < 5 * images_per_folder:
        images_5_folder_5.append(images_5[i])
    elif i < 6 * images_per_folder:
        images_5_folder_6.append(images_5[i])
    elif i < 7 * images_per_folder:
        images_5_folder_7.append(images_5[i])
    elif i < 8 * images_per_folder:
        images_5_folder_8.append(images_5[i])
    elif i < 9 * images_per_folder:
        images_5_folder_9.append(images_5[i])
    elif i < 10 * images_per_folder:
        images_5_folder_10.append(images_5[i])
    else:
        remaining = len(images_5) - i
        if remaining == 1:
            images_5_folder_1.append(images_5[i])
        elif remaining == 2:
            images_5_folder_2.append(images_5[i])
        elif remaining == 3:
            images_5_folder_3.append(images_5[i])
        elif remaining == 4:
            images_5_folder_4.append(images_5[i])
        elif remaining == 5:
            images_5_folder_5.append(images_5[i])
        elif remaining == 6:
            images_5_folder_6.append(images_5[i])
        elif remaining == 7:
            images_5_folder_7.append(images_5[i])
        elif remaining == 8:
            images_5_folder_8.append(images_5[i])
        elif remaining == 9:
            images_5_folder_9.append(images_5[i])

for i in range(0, len(images_6)):
    images_per_folder = int((percentage/100)*len(images_6))
    if i < images_per_folder:
        images_6_folder_1.append(images_6[i])
    elif i < 2 * images_per_folder:
        images_6_folder_2.append(images_6[i])
    elif i < 3 * images_per_folder:
        images_6_folder_3.append(images_6[i])
    elif i < 4 * images_per_folder:
        images_6_folder_4.append(images_6[i])
    elif i < 5 * images_per_folder:
        images_6_folder_5.append(images_6[i])
    elif i < 6 * images_per_folder:
        images_6_folder_6.append(images_6[i])
    elif i < 7 * images_per_folder:
        images_6_folder_7.append(images_6[i])
    elif i < 8 * images_per_folder:
        images_6_folder_8.append(images_6[i])
    elif i < 9 * images_per_folder:
        images_6_folder_9.append(images_6[i])
    elif i < 10 * images_per_folder:
        images_6_folder_10.append(images_6[i])
    else:
        remaining = len(images_6) - i
        if remaining == 1:
            images_6_folder_1.append(images_6[i])
        elif remaining == 2:
            images_6_folder_2.append(images_6[i])
        elif remaining == 3:
            images_6_folder_3.append(images_6[i])
        elif remaining == 4:
            images_6_folder_4.append(images_6[i])
        elif remaining == 5:
            images_6_folder_5.append(images_6[i])
        elif remaining == 6:
            images_6_folder_6.append(images_6[i])
        elif remaining == 7:
            images_6_folder_7.append(images_6[i])
        elif remaining == 8:
            images_6_folder_8.append(images_6[i])
        elif remaining == 9:
            images_6_folder_9.append(images_6[i])

for i in range(0, len(images_0_folder_1)):
    folder_1_rows.append(images_0_folder_1[i])
for i in range(0, len(images_1_folder_1)):
    folder_1_rows.append(images_1_folder_1[i])
for i in range(0, len(images_2_folder_1)):
    folder_1_rows.append(images_2_folder_1[i])
for i in range(0, len(images_3_folder_1)):
    folder_1_rows.append(images_3_folder_1[i])
for i in range(0, len(images_4_folder_1)):
    folder_1_rows.append(images_4_folder_1[i])
for i in range(0, len(images_5_folder_1)):
    folder_1_rows.append(images_5_folder_1[i])
for i in range(0, len(images_6_folder_1)):
    folder_1_rows.append(images_6_folder_1[i])

for i in range(0, len(images_0_folder_2)):
    folder_2_rows.append(images_0_folder_2[i])
for i in range(0, len(images_1_folder_2)):
    folder_2_rows.append(images_1_folder_2[i])
for i in range(0, len(images_2_folder_2)):
    folder_2_rows.append(images_2_folder_2[i])
for i in range(0, len(images_3_folder_2)):
    folder_2_rows.append(images_3_folder_2[i])
for i in range(0, len(images_4_folder_2)):
    folder_2_rows.append(images_4_folder_2[i])
for i in range(0, len(images_5_folder_2)):
    folder_2_rows.append(images_5_folder_2[i])
for i in range(0, len(images_6_folder_2)):
    folder_2_rows.append(images_6_folder_2[i])

for i in range(0, len(images_0_folder_3)):
    folder_3_rows.append(images_0_folder_3[i])
for i in range(0, len(images_1_folder_3)):
    folder_3_rows.append(images_1_folder_3[i])
for i in range(0, len(images_2_folder_3)):
    folder_3_rows.append(images_2_folder_3[i])
for i in range(0, len(images_3_folder_3)):
    folder_3_rows.append(images_3_folder_3[i])
for i in range(0, len(images_4_folder_3)):
    folder_3_rows.append(images_4_folder_3[i])
for i in range(0, len(images_5_folder_3)):
    folder_3_rows.append(images_5_folder_3[i])
for i in range(0, len(images_6_folder_3)):
    folder_3_rows.append(images_6_folder_3[i])

for i in range(0, len(images_0_folder_4)):
    folder_4_rows.append(images_0_folder_4[i])
for i in range(0, len(images_1_folder_4)):
    folder_4_rows.append(images_1_folder_4[i])
for i in range(0, len(images_2_folder_4)):
    folder_4_rows.append(images_2_folder_4[i])
for i in range(0, len(images_3_folder_4)):
    folder_4_rows.append(images_3_folder_4[i])
for i in range(0, len(images_4_folder_4)):
    folder_4_rows.append(images_4_folder_4[i])
for i in range(0, len(images_5_folder_4)):
    folder_4_rows.append(images_5_folder_4[i])
for i in range(0, len(images_6_folder_4)):
    folder_4_rows.append(images_6_folder_4[i])

for i in range(0, len(images_0_folder_5)):
    folder_5_rows.append(images_0_folder_5[i])
for i in range(0, len(images_1_folder_5)):
    folder_5_rows.append(images_1_folder_5[i])
for i in range(0, len(images_2_folder_5)):
    folder_5_rows.append(images_2_folder_5[i])
for i in range(0, len(images_3_folder_5)):
    folder_5_rows.append(images_3_folder_5[i])
for i in range(0, len(images_4_folder_5)):
    folder_5_rows.append(images_4_folder_5[i])
for i in range(0, len(images_5_folder_5)):
    folder_5_rows.append(images_5_folder_5[i])
for i in range(0, len(images_6_folder_5)):
    folder_5_rows.append(images_6_folder_5[i])

for i in range(0, len(images_0_folder_6)):
    folder_6_rows.append(images_0_folder_6[i])
for i in range(0, len(images_1_folder_6)):
    folder_6_rows.append(images_1_folder_6[i])
for i in range(0, len(images_2_folder_6)):
    folder_6_rows.append(images_2_folder_6[i])
for i in range(0, len(images_3_folder_6)):
    folder_6_rows.append(images_3_folder_6[i])
for i in range(0, len(images_4_folder_6)):
    folder_6_rows.append(images_4_folder_6[i])
for i in range(0, len(images_5_folder_6)):
    folder_6_rows.append(images_5_folder_6[i])
for i in range(0, len(images_6_folder_6)):
    folder_6_rows.append(images_6_folder_6[i])

for i in range(0, len(images_0_folder_7)):
    folder_7_rows.append(images_0_folder_7[i])
for i in range(0, len(images_1_folder_7)):
    folder_7_rows.append(images_1_folder_7[i])
for i in range(0, len(images_2_folder_7)):
    folder_7_rows.append(images_2_folder_7[i])
for i in range(0, len(images_3_folder_7)):
    folder_7_rows.append(images_3_folder_7[i])
for i in range(0, len(images_4_folder_7)):
    folder_7_rows.append(images_4_folder_7[i])
for i in range(0, len(images_5_folder_7)):
    folder_7_rows.append(images_5_folder_7[i])
for i in range(0, len(images_6_folder_7)):
    folder_7_rows.append(images_6_folder_7[i])

for i in range(0, len(images_0_folder_8)):
    folder_8_rows.append(images_0_folder_8[i])
for i in range(0, len(images_1_folder_8)):
    folder_8_rows.append(images_1_folder_8[i])
for i in range(0, len(images_2_folder_8)):
    folder_8_rows.append(images_2_folder_8[i])
for i in range(0, len(images_3_folder_8)):
    folder_8_rows.append(images_3_folder_8[i])
for i in range(0, len(images_4_folder_8)):
    folder_8_rows.append(images_4_folder_8[i])
for i in range(0, len(images_5_folder_8)):
    folder_8_rows.append(images_5_folder_8[i])
for i in range(0, len(images_6_folder_8)):
    folder_8_rows.append(images_6_folder_8[i])

for i in range(0, len(images_0_folder_9)):
    folder_9_rows.append(images_0_folder_9[i])
for i in range(0, len(images_1_folder_9)):
    folder_9_rows.append(images_1_folder_9[i])
for i in range(0, len(images_2_folder_9)):
    folder_9_rows.append(images_2_folder_9[i])
for i in range(0, len(images_3_folder_9)):
    folder_9_rows.append(images_3_folder_9[i])
for i in range(0, len(images_4_folder_9)):
    folder_9_rows.append(images_4_folder_9[i])
for i in range(0, len(images_5_folder_9)):
    folder_9_rows.append(images_5_folder_9[i])
for i in range(0, len(images_6_folder_9)):
    folder_9_rows.append(images_6_folder_9[i])

for i in range(0, len(images_0_folder_10)):
    folder_10_rows.append(images_0_folder_10[i])
for i in range(0, len(images_1_folder_10)):
    folder_10_rows.append(images_1_folder_10[i])
for i in range(0, len(images_2_folder_10)):
    folder_10_rows.append(images_2_folder_10[i])
for i in range(0, len(images_3_folder_10)):
    folder_10_rows.append(images_3_folder_10[i])
for i in range(0, len(images_4_folder_10)):
    folder_10_rows.append(images_4_folder_10[i])
for i in range(0, len(images_5_folder_10)):
    folder_10_rows.append(images_5_folder_10[i])
for i in range(0, len(images_6_folder_10)):
    folder_10_rows.append(images_6_folder_10[i])

#first_row = ["emotion", "pixels", "Usage"]
random.shuffle(folder_1_rows)
random.shuffle(folder_2_rows)
random.shuffle(folder_3_rows)
random.shuffle(folder_4_rows)
random.shuffle(folder_5_rows)
random.shuffle(folder_6_rows)
random.shuffle(folder_7_rows)
random.shuffle(folder_8_rows)
random.shuffle(folder_9_rows)
random.shuffle(folder_10_rows)

for i in range(0, len(out_file_names)):
    out_path = out_folder_path + out_file_names[i]
    out_file = open(out_path, "w", newline='')
    csv_writer = csv.writer(out_file, delimiter=",")
    #csv_writer.writerow(first_row)
    if i == 0:
        for j in range(0, len(folder_1_rows)):
            csv_writer.writerow(folder_1_rows[j])
    elif i == 1:
        for j in range(0, len(folder_2_rows)):
            csv_writer.writerow(folder_2_rows[j])
    elif i == 2:
        for j in range(0, len(folder_3_rows)):
            csv_writer.writerow(folder_3_rows[j])
    elif i == 3:
        for j in range(0, len(folder_4_rows)):
            csv_writer.writerow(folder_4_rows[j])
    elif i == 4:
        for j in range(0, len(folder_5_rows)):
            csv_writer.writerow(folder_5_rows[j])
    elif i == 5:
        for j in range(0, len(folder_6_rows)):
            csv_writer.writerow(folder_6_rows[j])
    elif i == 6:
        for j in range(0, len(folder_7_rows)):
            csv_writer.writerow(folder_7_rows[j])
    elif i == 7:
        for j in range(0, len(folder_8_rows)):
            csv_writer.writerow(folder_8_rows[j])
    elif i == 8:
        for j in range(0, len(folder_9_rows)):
            csv_writer.writerow(folder_9_rows[j])
    else:
        for j in range(0, len(folder_10_rows)):
            csv_writer.writerow(folder_10_rows[j])

print("Csv created")
