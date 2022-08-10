import cv2
import argparse
import random



parser = argparse.ArgumentParser()
parser.add_argument("--filePath", type=str, default="./2950")
parser.add_argument("--chouseFunction", type=int, help="1.random each pixel, 2.random same color space, 3.change to HSV", required=True)

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
    imgPath = args.filePath
    imgOrigin = cv2.imread(imgPath + "Origin.png")
    imgSeg = cv2.imread(imgPath + "Seg.png")
    if(args.chouseFunction == 1):
        imgPixel = randomColorWithEachPixel(imgOrigin, imgSeg)
        cv2.imwrite(args.filePath + "EachPixel.png", imgPixel)
    elif(args.chouseFunction == 2):
        for i in range(5):
            imgSameColor = randomColorWithSameColorSpace(imgOrigin, imgSeg)
            cv2.imwrite(args.filePath + "SameColor" + str(i) + ".png", imgSameColor)
    elif(args.chouseFunction == 3):
        imgBGR2HSV = changeColorBGRtoHSV(imgOrigin, imgSeg)
        cv2.imwrite(args.filePath + "HSV.png", imgBGR2HSV)
    elif(args.chouseFunction == 4):
        for i in range(5):
            imgBGR2HSVRandom = changeColorBGRtoHSVWithRandom(imgOrigin, imgSeg)
            cv2.imwrite(args.filePath + "HSVRandom" + str(i) + ".png", imgBGR2HSVRandom)
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
