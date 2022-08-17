import cv2 
import os



fileList = ["001", "002", "003", "004", "005"]
fileList = ["006"]

for fileName in fileList:
    img = cv2.imread("./" + fileName + ".jpeg")
    img = cv2.resize(img, (2048, 1024), interpolation=cv2.INTER_AREA)
    cv2.imwrite("./" + fileName + ".jpg", img)