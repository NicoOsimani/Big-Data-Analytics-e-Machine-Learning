import csv
import PIL.Image
import PIL.ImageTk
import tkinter
import cv2
from os import listdir
from os.path import isfile, join

in_folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video"
out_file_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/video/fold_1/test.csv"

labels = []

def func_0():
    write_0(labels)

def write_0(labels):
    labels.append(0)

def func_1():
    write_1(labels)

def write_1(labels):
    labels.append(1)

def func_2():
    write_2(labels)

def write_2(labels):
    labels.append(2)

def func_3():
    write_3(labels)

def write_3(labels):
    labels.append(3)

def func_4():
    write_4(labels)

def write_4(labels):
    labels.append(4)

def func_5():
    write_5(labels)

def write_5(labels):
    labels.append(5)

def func_6():
    write_6(labels)

def write_6(labels):
    labels.append(6)

def main():
    files = [f for f in listdir(in_folder_path) if isfile(join(in_folder_path, f))]
    images_names = []
    for i in range(0, len(files)):
        images_names.append(str(i + 1) + ".png")

    for i in range(0, len(images_names)):
        image_path = in_folder_path + "/" + images_names[i]

        # Create a window
        window = tkinter.Tk()
        window.title("Frames")

        # Load an image using OpenCV
        cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        cv_img = cv2.resize(cv_img, (224, 224))

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        height, width, no_channels = cv_img.shape

        # Create a canvas that can fit the above image
        canvas = tkinter.Canvas(window, width = width, height = height)
        canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

        # Add a PhotoImage to the Canvas
        canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

        # Buttons
        btn_0 = tkinter.Button(window, text="Angry", width=50, command=lambda:[func_0(), window.destroy()])
        btn_0.pack(anchor=tkinter.CENTER, expand=True)

        btn_1 = tkinter.Button(window, text="Disgust", width=50, command=lambda:[func_1(), window.destroy()])
        btn_1.pack(anchor=tkinter.CENTER, expand=True)

        btn_2 = tkinter.Button(window, text="Fear", width=50, command=lambda:[func_2(), window.destroy()])
        btn_2.pack(anchor=tkinter.CENTER, expand=True)

        btn_3 = tkinter.Button(window, text="Happy", width=50, command=lambda:[func_3(), window.destroy()])
        btn_3.pack(anchor=tkinter.CENTER, expand=True)

        btn_4 = tkinter.Button(window, text="Sad", width=50, command=lambda:[func_4(), window.destroy()])
        btn_4.pack(anchor=tkinter.CENTER, expand=True)

        btn_5 = tkinter.Button(window, text="Surprise", width=50, command=lambda:[func_5(), window.destroy()])
        btn_5.pack(anchor=tkinter.CENTER, expand=True)

        btn_6 = tkinter.Button(window, text="Neutral", width=50, command=lambda:[func_6(), window.destroy()])
        btn_6.pack(anchor=tkinter.CENTER, expand=True)

        # Run the window loop
        window.mainloop()

    out_file = open(out_file_path, "w", newline='')
    csv_writer = csv.writer(out_file, delimiter=",")
    first_row = ["emotion", "image_name", "Usage"]
    csv_writer.writerow(first_row)
    for i in range(0, len(images_names)):
        row = [labels[i], images_names[i], "PrivateTest"]
        csv_writer.writerow(row)

    print("Csv created")

if __name__ == "__main__":
    main()
