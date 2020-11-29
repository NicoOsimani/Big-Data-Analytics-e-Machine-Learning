import csv

in_folder_path = "/home/nico/Scrivania/Big data/Progetto/csv/"  # path alla cartella
out_folder_path = "/home/nico/Scrivania/Big data/Progetto/csv/"  # path alla cartella
in_files = ["folder_1", "folder_2", "folder_3", "folder_4", "folder_5", "folder_6", "folder_7", "folder_8", "folder_9", "folder_10"]

first_row = ["emotion", "pixels", "Usage"]
in_file_names = [in_files[0] + ".csv", in_files[1] + ".csv", in_files[2] + ".csv", in_files[3] + ".csv", in_files[4] + ".csv", in_files[5] + ".csv", in_files[6] + ".csv", in_files[7] + ".csv", in_files[8] + ".csv", in_files[9] + ".csv"]

for i in range(0, len(in_file_names)):
    if i == 0:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 1:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 2:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 3:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 4:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 5:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 6:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 7:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    elif i == 8:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)
        for row in csv_reader_10:
            csv_writer_2.writerow(row)
    else:
        in_path_1 = in_folder_path + "folder_1.csv"
        in_path_2 = in_folder_path + "folder_2.csv"
        in_path_3 = in_folder_path + "folder_3.csv"
        in_path_4 = in_folder_path + "folder_4.csv"
        in_path_5 = in_folder_path + "folder_5.csv"
        in_path_6 = in_folder_path + "folder_6.csv"
        in_path_7 = in_folder_path + "folder_7.csv"
        in_path_8 = in_folder_path + "folder_8.csv"
        in_path_9 = in_folder_path + "folder_9.csv"
        in_path_10 = in_folder_path + "folder_10.csv"
        in_file_1 = open(in_path_1)
        in_file_2 = open(in_path_2)
        in_file_3 = open(in_path_3)
        in_file_4 = open(in_path_4)
        in_file_5 = open(in_path_5)
        in_file_6 = open(in_path_6)
        in_file_7 = open(in_path_7)
        in_file_8 = open(in_path_8)
        in_file_9 = open(in_path_9)
        in_file_10 = open(in_path_10)
        csv_reader_1 = csv.reader(in_file_1, delimiter=",")
        csv_reader_2 = csv.reader(in_file_2, delimiter=",")
        csv_reader_3 = csv.reader(in_file_3, delimiter=",")
        csv_reader_4 = csv.reader(in_file_4, delimiter=",")
        csv_reader_5 = csv.reader(in_file_5, delimiter=",")
        csv_reader_6 = csv.reader(in_file_6, delimiter=",")
        csv_reader_7 = csv.reader(in_file_7, delimiter=",")
        csv_reader_8 = csv.reader(in_file_8, delimiter=",")
        csv_reader_9 = csv.reader(in_file_9, delimiter=",")
        csv_reader_10 = csv.reader(in_file_10, delimiter=",")
        out_path_1 = out_folder_path + "fold_" + str(i + 1) + "/test.csv"
        out_file_1 = open(out_path_1, "w", newline='')
        csv_writer_1 = csv.writer(out_file_1, delimiter=",")
        out_path_2 = out_folder_path + "fold_" + str(i + 1) + "/train_val.csv"
        out_file_2 = open(out_path_2, "w", newline='')
        csv_writer_2 = csv.writer(out_file_2, delimiter=",")
        csv_writer_1.writerow(first_row)
        for row in csv_reader_1:
            csv_writer_2.writerow(row)
        for row in csv_reader_2:
            csv_writer_2.writerow(row)
        for row in csv_reader_3:
            csv_writer_2.writerow(row)
        for row in csv_reader_4:
            csv_writer_2.writerow(row)
        for row in csv_reader_5:
            csv_writer_2.writerow(row)
        for row in csv_reader_6:
            csv_writer_2.writerow(row)
        for row in csv_reader_7:
            csv_writer_2.writerow(row)
        for row in csv_reader_8:
            csv_writer_2.writerow(row)
        for row in csv_reader_9:
            csv_writer_2.writerow(row)
        for row in csv_reader_10:
            row[2] = "PrivateTest"
            csv_writer_1.writerow(row)

print("Csv created")
