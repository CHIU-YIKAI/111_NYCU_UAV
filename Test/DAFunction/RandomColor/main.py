from os import nice
import cv2
import argparse
import random



parser = argparse.ArgumentParser()
parser.add_argument("--filePath", type=str, default="./2950")

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
    randomR = random.uniform(0.5,1.5)
    randomG = random.uniform(0.5,1.5)
    randomB = random.uniform(0.5,1.5)
    
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



def main(args):
    imgPath = args.filePath
    imgOrigin = cv2.imread(imgPath + "Origin.png")
    imgSeg = cv2.imread(imgPath + "Seg.png")
    # imgPixel = randomColorWithEachPixel(imgOrigin, imgSeg)
    # cv2.imwrite(args.filePath + "EachPixel.png", imgPixel)
    for i in range(5):
        imgSameColor = randomColorWithSameColorSpace(imgOrigin, imgSeg)
        cv2.imwrite(args.filePath + "SameColor"+str(i)+".png", imgSameColor)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
