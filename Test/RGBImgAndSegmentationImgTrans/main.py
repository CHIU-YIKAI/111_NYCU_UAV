from distutils import filelist
import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--originDataFolder", type=str, default="./originData/")
parser.add_argument("--outputDataFolder", type=str, default="./outputData/")
parser.add_argument("--chouseFunction", type=int, default= 0)

def segmentationToRGB(originDir, fileList, outputDir):
    for fileName in fileList:
        img = cv2.imread(originDir + fileName)
        w, h, _ = img.shape
        for i in range(w):
            for j in range(h):
                if(img[i,j,0] == 19):
                    color = [128, 192, 128]
                elif(img[i,j,0] == 20):
                    color = [128, 64, 128]
                elif(img[i,j,0] == 21):
                    color = [0, 64, 64]
                elif(img[i,j,0] == 22):
                    color = [128, 192, 0]
                elif(img[i,j,0] == 23):
                    color = [0, 64, 192]
                elif(img[i,j,0] == 24):
                    color = [0, 192, 64]
                img[i,j] = color
        cv2.imwrite(outputDir + fileName, img)

def RGBToSegmentation(originDir, fileList, outputDir):
    for fileName in fileList:
        img = cv2.imread(originDir + fileName)
        w, h, _ = img.shape
        for i in range(w):
            for j in range(h):
                color = 0
                B, G, R = img[i, j]
                if(B == 128 and G == 192 and R == 128):
                    color = 19
                elif(B == 128 and G ==64  and R == 128):
                    color = 20
                elif(B == 0 and G == 64 and R == 64):
                    color = 21
                elif(B == 128 and G == 192 and R == 0):
                    color = 22
                elif(B == 0 and G == 64 and R == 192):
                    color = 23
                elif(B == 0 and G == 192 and R == 64):
                    color = 24
                else:
                    color = 21
                img[i,j] = [color, color, color]
        cv2.imwrite(outputDir + fileName, img)


def main(args):
    fileList = os.listdir(args.originDataFolder)

    if args.chouseFunction == 1:
        RGBToSegmentation(args.originDataFolder, fileList, args.outputDataFolder)
    elif args.chouseFunction == 2:
        segmentationToRGB(args.originDataFolder, fileList, args.outputDataFolder)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
