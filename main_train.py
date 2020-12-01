import os
import json
import random
import warnings

# todo: set dataset name
dataset_name = "fer2013"

warnings.simplefilter(action="ignore", category=FutureWarning)

import imgaug
import torch
import torch.multiprocessing as mp
import numpy as np


seed = 1234
random.seed(seed)
imgaug.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


import models
from models import segmentation


def main(config_path):
    """
    This is the main function to make the training up

    Parameters:
    -----------
    config_path : srt
        path to config file
    """
    # load configs and set random seed
    configs = json.load(open(config_path))
    configs["cwd"] = os.getcwd()

    data_path = configs["data_path"]
    model_name = configs["model_name"]

    for k in range(0, configs["k-fold"]):

        configs["data_path"] = data_path + "/fold_" + str(k + 1)

        configs["model_name"] = model_name + "_fold_" + str(k + 1)

        # load model and data_loader
        model = get_model(configs)

        train_set, val_set, test_set = get_dataset(configs)

        # init trainer and make a training
        # from trainers.fer2013_trainer import FER2013Trainer
        from trainers.tta_trainer import FER2013Trainer

        # from trainers.centerloss_trainer import FER2013Trainer
        trainer = FER2013Trainer(model, train_set, val_set, test_set, configs)

        if configs["distributed"] == 1:
            ngpus = torch.cuda.device_count()
            mp.spawn(trainer.train, nprocs=ngpus, args=())
        else:
            trainer.train()


def get_model(configs):
    """
    This function get raw models from models package

    Parameters:
    ------------
    configs : dict
        configs dictionary
    """
    try:
        return models.__dict__[configs["arch"]]
    except KeyError:
        return segmentation.__dict__[configs["arch"]]


def get_dataset(configs):
    """
    This function get raw dataset
    """
    from utils.datasets.fer2013dataset import fer2013
    from utils.datasets.mydatasetdataset import mydataset

    if dataset_name == "fer2013":
        train_set = fer2013("train", configs)
        val_set = fer2013("val", configs)
        test_set = fer2013("test", configs, tta=True, tta_size=10)
    else:
        train_set = mydataset("train", configs)
        val_set = mydataset("val", configs)
        test_set = mydataset("test", configs, tta=True, tta_size=10)
    return train_set, val_set, test_set


if __name__ == "__main__":
    if dataset_name == "fer2013":
        main("./configs/fer2013_config.json")
    else:
        main("./configs/mydataset_config.json")