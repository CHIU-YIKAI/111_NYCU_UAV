import cv2
import argparse
import random



parser = argparse.ArgumentParser()
parser.add_argument("--filePath", type=str, default="./2950")

def randomColorWithEachPixel(imgOrigin, imgSeg):
    '''
    indtoduce
        This function is use to set the random color to the origin image based on segmentation result
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


def main(args):
    imgPath = args.filePath
    imgOrigin = cv2.imread(imgPath + "Origin.png")
    imgSeg = cv2.imread(imgPath + "Seg.png")
    imgNew = randomColorWithEachPixel(imgOrigin, imgSeg)
    cv2.imwrite(args.filePath + "EachPixel.png", imgNew)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
