import cv2
import os

dirName = "./SegmentationClassPNG/"
fileList = ["A_001", "A_002", "A_003", "A_004"]

for fileName in fileList:
    img = cv2.imread(dirName + fileName + ".png")
    print(dirName + fileName)
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
    cv2.imwrite("./TransFinish/" + fileName + ".png", img)