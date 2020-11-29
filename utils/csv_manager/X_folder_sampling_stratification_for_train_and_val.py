import csv
import random

in_folder_path = "/home/nico/Scrivania/Big data/Progetto/csv/"  # path alla cartella
out_folder_path = "/home/nico/Scrivania/Big data/Progetto/csv/"  # path alla cartella
out_files = ["val", "train"]
train_percentage = 90
val_percentage = 10

first_row = ["emotion", "pixels", "Usage"]
out_file_names = [out_files[0] + ".csv", out_files[1] + ".csv"]
if (train_percentage + val_percentage) == 100:
    for z in range(0, 10):
        images_0 = []
        images_1 = []
        images_2 = []
        images_3 = []
        images_4 = []
        images_5 = []
        images_6 = []
        totals = [0, 0, 0, 0, 0, 0, 0]
        in_path = in_folder_path + "fold_" + str(z + 1) + "/train_val.csv"
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

        percentages = [val_percentage, train_percentage]
        random.shuffle(images_0)
        random.shuffle(images_1)
        random.shuffle(images_2)
        random.shuffle(images_3)
        random.shuffle(images_4)
        random.shuffle(images_5)
        random.shuffle(images_6)

        for i in range(0, len(out_file_names)):
            if i == 0:
                val_rows = []
            else:
                train_rows = []
            for j in range(0, len(totals)):
                if i == 0:
                    index_start = 0
                    total = int(round(((percentages[i] / 100) * totals[j]), 0))
                    index_end = index_start + total
                else:
                    index_start = int(round(((percentages[0] / 100) * totals[j]), 0))
                    index_end = totals[j]
                if j == 0:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_0[k][2] = "PublicTest"
                            val_rows.append(images_0[k])
                        else:
                            images_0[k][2] = "Training"
                            train_rows.append(images_0[k])
                elif j == 1:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_1[k][2] = "PublicTest"
                            val_rows.append(images_1[k])
                        else:
                            images_1[k][2] = "Training"
                            train_rows.append(images_1[k])
                elif j == 2:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_2[k][2] = "PublicTest"
                            val_rows.append(images_2[k])
                        else:
                            images_2[k][2] = "Training"
                            train_rows.append(images_2[k])
                elif j == 3:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_3[k][2] = "PublicTest"
                            val_rows.append(images_3[k])
                        else:
                            images_3[k][2] = "Training"
                            train_rows.append(images_3[k])
                elif j == 4:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_4[k][2] = "PublicTest"
                            val_rows.append(images_4[k])
                        else:
                            images_4[k][2] = "Training"
                            train_rows.append(images_4[k])
                elif j == 5:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_5[k][2] = "PublicTest"
                            val_rows.append(images_5[k])
                        else:
                            images_5[k][2] = "Training"
                            train_rows.append(images_5[k])
                else:
                    for k in range(index_start, index_end):
                        if i == 0:
                            images_6[k][2] = "PublicTest"
                            val_rows.append(images_6[k])
                        else:
                            images_6[k][2] = "Training"
                            train_rows.append(images_6[k])

        random.shuffle(val_rows)
        random.shuffle(train_rows)
        for i in range(0, len(out_file_names)):
            out_path = out_folder_path + "fold_" + str(z + 1) + "/" + out_file_names[i]
            out_file = open(out_path, "w", newline='')
            csv_writer = csv.writer(out_file, delimiter=",")
            csv_writer.writerow(first_row)
            if i == 0:
                for j in range(0, len(val_rows)):
                    csv_writer.writerow(val_rows[j])
            else:
                for j in range(0, len(train_rows)):
                    csv_writer.writerow(train_rows[j])

    print("Csv created")
else:
    print("Not correct train and val percentages!!")
