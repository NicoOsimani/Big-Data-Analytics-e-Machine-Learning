import cv2

video_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/pre-processed/videos/Looney Tunes in italiano Introduzioni Vol. 1 WB Kids.mp4"
out_folder_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/pre-processed/photos/"
classifier_path = "/home/nico/Scrivania/Big data/Progetto/Big-Data-Analytics-e-Machine-Learning/saved/data/pre-processed/haarcascade_frontalface_alt_tree.xml" # questo va bene haarcascade_frontalface_alt_tree.xml
outputDim = (224, 224)
frameRate = 1

def main():
    vidcap = cv2.VideoCapture(video_path)
    sec = 0
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    success, image = vidcap.read()
    face_cascade = cv2.CascadeClassifier(classifier_path)
    final_frames = 0
    while success:
        sec = sec + frameRate
        sec = round(sec, 2)
        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)
        # show frame
        '''
        cv2.imshow("Frame", image)
        k = cv2.waitKey()
        '''
        # detect faces
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x, y, w, h) in faces:
            adjustCrop = int(((h + w)/2)*0.5)
            adjustcenterCrop = int(adjustCrop/2)
            crop_img = image[y:y - adjustcenterCrop + h + adjustCrop, x:x - adjustcenterCrop + w + adjustCrop]
            resized = cv2.resize(crop_img, outputDim)
            # show and save faces
            '''
            cv2.imshow("Cropped face", resized)
            k = cv2.waitKey()
            if k == ord("s"):
                final_frames += 1
                cv2.imwrite(out_folder_path + "{}.png".format(final_frames), resized)
            '''
            # only save all faces

            final_frames += 1
            cv2.imwrite(out_folder_path + "{}.png".format(final_frames), resized)

        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        success, image = vidcap.read()
        print("Read a new frame:", success)

if __name__ == "__main__":
    main()
