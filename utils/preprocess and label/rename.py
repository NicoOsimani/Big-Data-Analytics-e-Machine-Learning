import cv2
from os import listdir
from os.path import isfile, join

in_folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/pre-processed/photos/"
out_folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video/fold_1/"
rename_since = 1

def main():
    files = [f for f in listdir(in_folder_path) if isfile(join(in_folder_path, f))]

    for i in range(0, len(files)):
        image = cv2.imread(in_folder_path + "/" + files[i])
        cv2.imwrite(out_folder_path + "{}.png".format(i + rename_since), image)

    print("Photos renamed!")

if __name__ == "__main__":
    main()
