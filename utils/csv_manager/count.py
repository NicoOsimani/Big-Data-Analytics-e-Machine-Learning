import csv

folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video/fold_1/" #path alla cartella
file_names = ["test"]

for i in range(0, len(file_names)):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    total = 0
    csv_path = folder_path + file_names[i] + ".csv"
    csv_file = open(csv_path)
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        class_id = row[0]
        if class_id != "emotion":
            total += 1
            if class_id == "0":
                count_0 += 1
            elif class_id == "1":
                count_1 += 1
            elif class_id == "2":
                count_2 += 1
            elif class_id == "3":
                count_3 += 1
            elif class_id == "4":
                count_4 += 1
            elif class_id == "5":
                count_5 += 1
            else:
                count_6 += 1

    percent_0 = (count_0*100)/total
    percent_1 = (count_1*100)/total
    percent_2 = (count_2*100)/total
    percent_3 = (count_3*100)/total
    percent_4 = (count_4*100)/total
    percent_5 = (count_5*100)/total
    percent_6 = (count_6*100)/total
    print(file_names[i])
    print("")
    print("0 = {}  {:.0f}".format(count_0, percent_0) + " %")
    print("1 = {}  {:.0f}".format(count_1, percent_1) + " %")
    print("2 = {}  {:.0f}".format(count_2, percent_2) + " %")
    print("3 = {}  {:.0f}".format(count_3, percent_3) + " %")
    print("4 = {}  {:.0f}".format(count_4, percent_4) + " %")
    print("5 = {}  {:.0f}".format(count_5, percent_5) + " %")
    print("6 = {}  {:.0f}".format(count_6, percent_6) + " %")
    print("total = {}".format(total))
    print("")
    print("")
