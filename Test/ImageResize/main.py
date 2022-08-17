import cv2 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--originDataFolder", type=str, default="./originData/")
parser.add_argument("--outputDataFolder", type=str, default="./outputData/")

def main(args):
    fileList = os.listdir(args.originDataFolder)
    for fileName in fileList:
        img = cv2.imread(args.originDataFolder + fileName)
        img = cv2.resize(img, (2048, 1024), interpolation=cv2.INTER_AREA)
        cv2.imwrite(args.outputDataFolder + fileName, img)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

