import os
import glob
import json
import random
import itertools

import imgaug
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from natsort import natsorted
from sklearn.metrics import confusion_matrix, classification_report
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import transforms

# for consistent latex font
from matplotlib import rc
from matplotlib import rcParams

# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
# rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
#rcParams["font.family"] = "sans-serif"
#rcParams["font.sans-serif"] = ["Computer Modern Sans"]
#rc("text", usetex=True)

# todo: set names
check_name = "resmasking_dropout1_fer2013_fold_{}_train1" #checkpoint names - mettere {} al posto del numero di fold
dataset_name = "fer2013" #fer2013
test_name = "test1"
class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

seed = 1234
random.seed(seed)
imgaug.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


from utils.datasets.fer2013dataset import fer2013
from utils.datasets.mydatasetdataset import mydataset
from utils.generals import make_batch
from tqdm import tqdm

check_test_name = check_name + "_" + test_name

def Log(data, name):
    file = open(name, "a")
    file.write(str(data))
    file.close()

def plot_confusion_matrix(
    cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues, log_name="log_name", check_log_name="check_log_name"
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
    row = []
    Log("Confusion matrix\n", "./saved/results/{}.txt".format(log_name))
    for i in range(0, len(cm)):
        if row != []:
            print(row)
            Log(row, "./saved/results/{}.txt".format(log_name))
            Log("\n", "./saved/results/{}.txt".format(log_name))
        row = []
        for j in range(0, len(cm[0])):
            row.append(round(cm[i][j], 2))
    print(row)
    Log(row, "./saved/results/{}.txt".format(log_name))
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
    fig.savefig("./saved/cm/cm_{}.png".format(check_log_name))
    #plt.show()
    plt.close(fig)


def main():
    with open("./configs/" + dataset_name + "_config.json") as f:
        configs = json.load(f)
    data_path = configs["data_path"]

    for i in range(0, configs["k-fold"]):
        checkpoint_name = check_name.format(i + 1)

        check_log_name = checkpoint_name + "_" + test_name
      
        configs["data_path"] = data_path + "/fold_" + str(i + 1)

        acc = 0.0
        state = torch.load("./saved/checkpoints/{}".format(checkpoint_name))

        from models import resmasking_dropout1

        model = resmasking_dropout1

        model = model(in_channels=3, num_classes=7).cuda()
        model.load_state_dict(state["net"])
        model.eval()

        correct = 0
        total = 0
        all_target = []
        all_output = []

        if dataset_name == "fer2013":
            test_set = fer2013("test", configs, tta=True, tta_size=10)
            # test_set = fer2013('test', configs, tta=False, tta_size=0)
        else:
            test_set = mydataset("test", configs, tta=True, tta_size=10)

        print("Testing fold {} on private test with tta..".format(i + 1))
        with torch.no_grad():
            for idx in tqdm(range(len(test_set)), total=len(test_set), leave=False):
                images, targets = test_set[idx]

                images = make_batch(images)
                images = images.cuda(non_blocking=True)

                outputs = model(images).cpu()
                outputs = F.softmax(outputs, 1)

                # outputs.shape [tta_size, 7]
                outputs = torch.sum(outputs, 0)
                outputs = torch.argmax(outputs, 0)
                outputs = outputs.item()
                targets = targets.item()
                total += 1
                correct += outputs == targets

                all_target.append(targets)
                all_output.append(outputs)

        acc = 100. * correct / total
        #print("Accuracy on private test with tta: {:.3f}".format(acc))

        all_target = np.array(all_target)
        all_output = np.array(all_output)

        matrix = confusion_matrix(all_target, all_output)
        np.set_printoptions(precision=2)

        validated = "all_results"
        log_name = check_test_name.format(validated)
        Log("Test fold {}\n\n".format(i + 1), "./saved/results/{}.txt".format(log_name))

        # plt.figure(figsize=(5, 5))
        plot_confusion_matrix(
            matrix,
            classes=class_names,
            normalize=True,
            # title='{} \n Accuracc: {:.03f}'.format(checkpoint_name, acc)
            title="Residual Masking Network",
            log_name=log_name,
            check_log_name=check_log_name
        )

        class_report = classification_report(all_target, all_output, target_names=class_names)
        print("Classification report")
        print(class_report)
        Log("\n\nClassification report\n", "./saved/results/{}.txt".format(log_name))
        Log(class_report, "./saved/results/{}.txt".format(log_name))
        Log("\n\n", "./saved/results/{}.txt".format(log_name))
        # plt.show()
        # plt.savefig('cm_{}.png'.format(checkpoint_name))
        #plt.savefig("./saved/cm/cm_{}.pdf".format(checkpoint_name))
        #plt.close()
        #print("save at ./saved/cm/cm_{}.pdf".format(checkpoint_name))


if __name__ == "__main__":
    main()
