import numpy as np
import argparse
import cv2
import template_matching as match

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image2 = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", image)

edged = cv2.Canny(gray, 100, 300,apertureSize = 3)

minLineLength = 30
maxLineGap = 5
lines = cv2.HoughLinesP(edged,1,np.pi/180, 100,minLineLength,maxLineGap)

print(lines[0])
print(lines[0][0][1])

yList = [lines[0][0][1]]

for x in range(0, len(lines)):
     for x1, y1, x2, y2 in lines[x]:
          yList.append(y1)
          print(lines[x-1])
          cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

yList.sort()
yArea = [yList[0]-12]
print(yList[0])
for x in range(len(yList)) :
     if x != 0:
          if yList[x] - yList[x-1]  > 20 :
               print(yList[x-1])
               yArea.append(yList[x-1]  + 12)
               print(yList[x])
               yArea.append(yList[x]-12)
print(yList[len(yList) -1])
yArea.append(yList[len(yList) -1] + 12)
sheet = image.copy()


for x in range(len(yArea)):
    print(yArea[x])
    
cv2.imshow("Sheet", sheet)
cv2.waitKey(0)

match = match.findNote()
for x in range(len(yArea)):
    #sheet2 = sheet[109:150, 0:500]
    if x % 2 == 0:
        sheet2 = image2[yArea[x]:yArea[x+1], 0:500]
        cv2.imshow("Sheet2", sheet2)
        cv2.waitKey(0)
        match.find(sheet2)
        

    
    










