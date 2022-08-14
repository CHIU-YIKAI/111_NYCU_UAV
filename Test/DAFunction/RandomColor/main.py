import cv2
import argparse
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument("--originImgFolder", type=str, default="./cityscapes/JPEGImage/")
parser.add_argument("--segImgFolder", type=str, default="./finish/")
parser.add_argument("--saveName", type=str, default="./data")
parser.add_argument("--chouseFunction", type=int, required=True)

def randomColorWithEachPixel(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to set the random color to the origin image based on segmentation result with Each Pixel
    input
        imgOrigin: The image befor random set the new color
        imgSeg: The image use segmentation to get the different tag
    output
        imgNew: The image after random set the new color
    '''
    imgNew = imgOrigin.copy()
    w, h ,_ = imgOrigin.shape
    
    for i in range(w):
        for j in range(h):
            # 24 is the tag for oil segmentation
            if(imgSeg[i, j, 0] == 24):
                newColor = [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)]
                imgNew[i,j] = newColor
    return imgNew    

def randomColorWithSameColorSpace(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to set the random color to the origin image based on segmentation resul twith same color space use power
    input
        imgOrigin: The image befor random set the new color
        imgSeg: The image use segmentation to get the different tag
    output
        imgNew: The image after random set the new color
    '''
    imgNew = imgOrigin.copy()
    w, h ,_ = imgOrigin.shape
    randomR = random.uniform(0,1.5)
    randomG = random.uniform(0,1.5)
    randomB = random.uniform(0,1.5)
    
    for i in range(w):
        for j in range(h):
            # 24 is the tag for oil segmentation
            if(imgSeg[i, j, 0] == 24):
                
                imgB = int(pow((imgOrigin[i,j,0] / 255), randomB) * 255)
                imgG = int(pow((imgOrigin[i,j,1] / 255), randomG) * 255)
                imgR = int(pow((imgOrigin[i,j,2] / 255), randomR) * 255)

                newColor = [imgB, imgG, imgR]

                imgNew[i,j] = newColor
    return imgNew    

def randomOneColorWithSameColorSpace(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to set the random color to the origin image based on segmentation resul twith same color space
        use power
    input
        imgOrigin: The image befor random set the new color
        imgSeg: The image use segmentation to get the different tag
    output
        imgNew: The image after random set the new color
    '''
    imgNew = imgOrigin.copy()
    w, h ,_ = imgOrigin.shape
    randomValue = random.uniform(0,1.5)
    
    for i in range(w):
        for j in range(h):
            # 24 is the tag for oil segmentation
            if(imgSeg[i, j, 0] == 24):
                
                imgB = int(pow((imgOrigin[i,j,0] / 255), randomValue) * 255)
                imgG = int(pow((imgOrigin[i,j,1] / 255), randomValue) * 255)
                imgR = int(pow((imgOrigin[i,j,2] / 255), randomValue) * 255)

                newColor = [imgB, imgG, imgR]

                imgNew[i,j] = newColor
    return imgNew    
    
def changeColorBGRtoHSV(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to change oil area to the HSV color space
    input
        imgOrigin: The image befor random set the new color
        imgSeg: The image use segmentation to get the different tag
    output
        imgNew: The image after change to HSV color space
    '''
    imgHSV = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2HSV)
    imgNew = imgOrigin.copy()
    w, h ,_ = imgOrigin.shape
    
    for i in range(w):
        for j in range(h):
            # 24 is the tag for oil segmentation
            if(imgSeg[i, j, 0] == 24):
                imgNew[i,j] = imgHSV[i,j]
    return imgNew    

def changeColorBGRtoHSVWithRandom(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to change oil area to the HSV color space
    input
        imgOrigin: The image befor random set the new color
        imgSeg: The image use segmentation to get the different tag
    output
        imgNew: The image after change to HSV color space
    '''
    imgHSV = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2HSV)
    imgNew = imgOrigin.copy()
    w, h ,_ = imgOrigin.shape
    randomH = random.uniform(0, 2)
    randomS = random.uniform(0, 2)
    randomV = random.uniform(0, 2)
    for i in range(w):
        for j in range(h):
            # 24 is the tag for oil segmentation
            if(imgSeg[i, j, 0] == 24):
                imgHSV[i,j,0] = int(pow((imgHSV[i,j,0] / 180), randomH) * 180)
                imgHSV[i,j,1] = int(pow((imgHSV[i,j,1] / 255), randomS) * 255)
                
                # imgHSV[i,j,2] = int(pow((imgHSV[i,j,2] / 255), randomV) * 255)
    imgNew = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)
    return imgNew    

def main(args):
    
    originImgPath = args.originImgFolder
    segImgPath = args.segImgFolder

    filelist = os.listdir(originImgPath)
    segFileList = os.listdir(segImgPath)
    f = open(args.saveName + "list.lst", 'w')

    for i, filePath in enumerate(filelist):
        imgOrigin = cv2.imread(originImgPath + filePath)
        imgSeg = cv2.imread(segImgPath + segFileList[i])
        print(originImgPath + filePath + "\t." + segImgPath + segFileList[i])

        if(args.chouseFunction == 1):
            imgPixel = randomColorWithEachPixel(imgOrigin, imgSeg)
            cv2.imwrite(args.saveName + "/Img/" + filePath + "EachPixel.jpg", imgPixel)
            cv2.imwrite(args.saveName + "/Seg/" + filePath + "EachPixel.jpg", imgSeg)
            f.write(args.saveName + "/Img/" + filePath + "EachPixel.jpg" + "\t" + args.saveName + "/Seg/" + filePath + "EachPixel.jpg\n")
        elif(args.chouseFunction == 2):
            cv2.imwrite(args.saveName + "/Img/" + filePath + "SameColor.jpg", imgOrigin)
            cv2.imwrite(args.saveName + "/Seg/" + filePath + "SameColor.jpg", imgSeg)
            f.write(args.saveName + "/Img/" + filePath + "SameColor.jpg" + "\t" + args.saveName + "/Seg/" + filePath + "SameColor.jpg\n")
            for i in range(5):
                imgSameColor = randomColorWithSameColorSpace(imgOrigin, imgSeg)
                cv2.imwrite(args.saveName + "/Img/" + filePath + "SameColor" + str(i) + ".jpg", imgSameColor)
                cv2.imwrite(args.saveName + "/Seg/" + filePath + "SameColor" + str(i) + ".jpg", imgSeg)
                f.write(args.saveName + "/Img/" + filePath + "SameColor" + str(i) + ".jpg" + "\t" + args.saveName + "/Seg/" + filePath + "SameColor" + str(i) + ".jpg\n")

        elif(args.chouseFunction == 3):
            f.write(args.saveName + "/Img/" + filePath + "RandomOneSameColor.jpg" + "\t" + args.saveName + "/Seg/" + filePath + "RandomOneSameColor.jpg\n")
            cv2.imwrite(args.saveName + "/Img/" + filePath + "RandomOneSameColor.jpg", imgOrigin)
            cv2.imwrite(args.saveName + "/Seg/" + filePath + "RandomOneSameColor.jpg", imgSeg)

            for i in range(5):
                imgSameColor = randomOneColorWithSameColorSpace(imgOrigin, imgSeg)
                cv2.imwrite(args.saveName + "/Img/" + filePath + "RandomOneSameColor" + str(i) + ".jpg", imgSameColor)
                cv2.imwrite(args.saveName + "/Seg/" + filePath + "RandomOneSameColor" + str(i) + ".jpg", imgSeg)
                f.write(args.saveName + "/Img/" + filePath + "RandomOneSameColor" + str(i) + ".jpg" + "\t" + args.saveName + "/Seg/" + filePath + "RandomOneSameColor" + str(i) + ".jpg\n")

        elif(args.chouseFunction == 4):
            imgBGR2HSV = changeColorBGRtoHSV(imgOrigin, imgSeg)
            cv2.imwrite(args.saveName + "/Img/" + filePath + "HSV.jpg", imgBGR2HSV)
            cv2.imwrite(args.saveName + "/Seg/" + filePath + "HSV.jpg", imgBGR2HSV)
            f.write(args.saveName + "/Img/" + filePath + "HSV.jpg" + "\t" + args.saveName + "/Seg/" + filePath + "HSV.jpg\n")

        elif(args.chouseFunction == 5):
            f.write(args.saveName + "/Img/" + filePath + "HSVRandom.jpg" + "\t" + args.saveName + "/Seg/" + filePath + "HSVRandom.jpg\n")
            cv2.imwrite(args.saveName + "/Img/" + filePath + "HSVRandom.jpg", imgOrigin)
            cv2.imwrite(args.saveName + "/Seg/" + filePath + "HSVRandom.jpg", imgSeg)

            for i in range(5):
                imgBGR2HSVRandom = changeColorBGRtoHSVWithRandom(imgOrigin, imgSeg)
                cv2.imwrite(args.saveName + "/Img/" + filePath + "HSVRandom" + str(i) + ".jpg", imgBGR2HSVRandom)
                cv2.imwrite(args.saveName + "/Seg/" + filePath + "HSVRandom" + str(i) + ".jpg", imgSeg)
                f.write(args.saveName + "/Img/" + filePath + "HSVRandom" + str(i) + ".jpg" + "\t" + args.saveName + "/Seg/" + filePath + "HSVRandom" + str(i) + ".jpg\n")
                
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
