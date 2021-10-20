

import cv2
import time 
import json
import os
import shutil
import sys, getopt

def main(argv):
    FILE_NAME = "/home/pradeepsen99/Desktop/Research/1050s1132a1110s3004-2s5310-1.mp4"
    ANNOT_FILE = ""
    SKIP_VAL = 15
    RAW_FOLDER_NAME = "raw_images"
    ANNOT_FOLDER_NAME = "annotated_images"

    try:
        opts, args = getopt.getopt(argv, "i:s:a:")
    except:
        print("Incorrect input!")
        sys.exit(2)

    for opt, args in opts:
        if opt == '-i':
            FILE_NAME = args
        elif opt == '-s':
            SKIP_VAL = int(args)
        elif opt == "-a":
            ANNOT_FILE = open(args)

    cap = cv2.VideoCapture(FILE_NAME)

    annotations = json.load(ANNOT_FILE)['annotations']
    print("Annotations sucessfuly imported")

    if os.path.exists(RAW_FOLDER_NAME):
        shutil.rmtree(RAW_FOLDER_NAME)
    os.mkdir(RAW_FOLDER_NAME)

    if os.path.exists(ANNOT_FOLDER_NAME):
        shutil.rmtree(ANNOT_FOLDER_NAME)
    os.mkdir(ANNOT_FOLDER_NAME)


    frame_num = 0
    while cap.isOpened():
        if frame_num % SKIP_VAL == 0:
            #time.sleep(.2)
            ret, frame = cap.read()
            if ret == True:
                cv2.imwrite(RAW_FOLDER_NAME + "/frame%d.jpg" % frame_num, frame)
                if frame_num > len(annotations) -1:
                    break
                for i in annotations[frame_num]:
                    frame = cv2.rectangle(frame, (int(i['x']), int(i['y'])), (int(i['x'])+int(i['width']), int(i['y'])+int(i['height'])), (255,0,0), 5)
                print(annotations[frame_num])
                frame = cv2.resize(frame, (960, 540))
                cv2.putText(frame, "Frame: " +str( frame_num), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow("Frame", frame)
                cv2.imwrite(ANNOT_FOLDER_NAME + "/frame%d.jpg" % frame_num, frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
            frame_num = frame_num + SKIP_VAL
        else:
            ret, frame = cap.read()
    cap.release()

    ANNOT_FILE.close()

if __name__ == "__main__":
    main(sys.argv[1:])