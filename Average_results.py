import re
import matplotlib.pyplot as plt
import numpy as np
import itertools
from prettytable import PrettyTable

dataFile = "resmasking_dropout1_fer2013_fold_all_results_train1_test1.txt"
class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

log_name_list = list(dataFile)
log_name_list[len(log_name_list) - 4] = "_"
log_name_list[len(log_name_list) - 3] = "a"
log_name_list[len(log_name_list) - 2] = "v"
log_name_list[len(log_name_list) - 1] = "e"
log_name_list = log_name_list + list("raged")
log_name = ""
for x in log_name_list:
    log_name += x

def Log(data, name):
    file = open(name, "a")
    file.write(str(data))
    file.close()

def plot_confusion_matrix(
    cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues
):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
    for i in range(0,len(cm)):
        for j in range(0, len(cm[0])):
            cm[i][j] = round(cm[i][j], 2)
    print(cm)
    Log("Confusion matrix\n", "./saved/results/{}.txt".format(log_name))
    Log(cm, "./saved/results/{}.txt".format(log_name))
    fig = plt.figure(figsize=(6, 6), dpi=80)
    plt.imshow(cm, interpolation="nearest", cmap=cmap)
    plt.title(title, fontsize=12)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = ".2f" if normalize else "d"
    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(
            j,
            i,
            format(cm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black",
        )

    plt.ylabel("True label", fontsize=12)
    plt.xlabel("Predicted label", fontsize=12)
    plt.tight_layout()
    fig.savefig("./saved/cm/cm_{}.png".format(log_name))
    plt.show()
    plt.close(fig)

def main():
    num_classes = len(class_names)
    numbers = num_classes*num_classes
    dataPath = "./saved/results/" + dataFile
    exp = "\d+\.\d+"
    foldData = []
    allData = []
    z = 0
    k = 1
    with open(dataPath) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for s in re.findall(exp, line):
                foldData.append(float(s))
                z += 1
                if z == k * (numbers + num_classes*4):
                    z == 0
                    allData.append(foldData)
                    foldData = []
                    k += 1

    average = []
    for i in range(0, numbers + num_classes*4):
        average.append(0)

    for i in range(0, len(allData)):
        for j in range(0, len(allData[0])):
            average[j] += allData[i][j]

    for i in range(0, len(average)):
        average[i] = round(average[i]/(k - 1), 2)

    cm = np.array([[]])
    row = []
    k = 1
    for i in range(0, numbers):
        row.append(average[i])
        if (i + 1) == k * num_classes:
            if (i + 1) == num_classes:
                cm = np.array([row])
            else:
                cm_rows = np.array([row])
                cm = np.append(cm, cm_rows, 0)
            row = []
            k += 1
    plot_confusion_matrix(
        cm,
        classes=class_names,
        normalize=True,
        title="Residual Masking Network"
    )

    t = PrettyTable(['', 'precision', 'recall', 'f1-score'])
    j = 0
    for i in range(numbers, len(average) - 7 - 2 * num_classes):
        t.add_row([class_names[j], average[3 * (i - numbers) + numbers], average[3 * (i - numbers) + numbers + 1], average[3 * (i - numbers) + numbers + 2]])
        j += 1

    t.add_row(['------------', '---------', '---------', '---------'])
    t.add_row(['accuracy', '', '', average[len(average) - 7]])
    t.add_row(['macro avg', average[len(average) - 6], average[len(average) - 5], average[len(average) - 4]])
    t.add_row(['weighted avg', average[len(average) - 3], average[len(average) - 2], average[len(average) - 1]])
    print("Classification report")
    print(t)
    Log("\n\nClassification report\n", "./saved/results/{}.txt".format(log_name))
    Log(t, "./saved/results/{}.txt".format(log_name))
    Log("\n\n", "./saved/results/{}.txt".format(log_name))

if __name__ == "__main__":
    main()
