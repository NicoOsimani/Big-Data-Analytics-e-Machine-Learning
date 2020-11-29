import os
import glob
import json
import random
import itertools
import csv

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

# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
#rc("font", **{"family": "serif", "serif": ["Computer Modern Roman"]})
#rc("text", usetex=True)


checkpoint_name = "vgg19_rot30_2019Dec01_14.01"

dataset_name = "fer2013" #fer2013

seed = 1234
random.seed(seed)
imgaug.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


from models import resatt18
from utils.datasets.fer2013dataset import fer2013
from utils.datasets.mydatasetdataset import mydataset
from utils.generals import make_batch
from tqdm import tqdm

class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]


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
    print(cm)

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
    fig.savefig("./saved/cm/cm_{}.png".format(checkpoint_name))
    plt.show()
    plt.close(fig)


def main():
    with open("./configs/" + dataset_name + "_config.json") as f:
        configs = json.load(f)

    acc = 0.0
    state = torch.load("./saved/checkpoints/{}".format(checkpoint_name))

    from models import vgg19

    model = vgg19

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

    print("Calc acc on private test with tta..")
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
    print("Accuracy on private test with tta: {:.3f}".format(acc))
    out_path = "./saved/results/accuracy/{}.csv".format(checkpoint_name)
    out_file = open(out_path, "w", newline='')
    csv_writer = csv.writer(out_file, delimiter=",")
    acc_row = [acc]
    csv_writer.writerow(acc_row)

    all_target = np.array(all_target)
    all_output = np.array(all_output)

    matrix = confusion_matrix(all_target, all_output)
    np.set_printoptions(precision=2)

    # plt.figure(figsize=(5, 5))
    plot_confusion_matrix(
        matrix,
        classes=class_names,
        normalize=True,
        # title='{} \n Accuracc: {:.03f}'.format(checkpoint_name, acc)
        title="Vgg19",
    )

    class_report = classification_report(all_target, all_output, target_names=class_names)
    print("Classification report")
    print(class_report)
    # plt.show()
    # plt.savefig('cm_{}.png'.format(checkpoint_name))
    #plt.savefig("./saved/cm/cm_{}.pdf".format(checkpoint_name))
    #plt.close()


if __name__ == "__main__":
    main()
