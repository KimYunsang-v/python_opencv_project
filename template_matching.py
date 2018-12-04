import cv2
import numpy as np
import Midi

class findNote:        
#img2 = img.copy()
    def find(self,searchImage):
        #img = cv2.imread(searchImage,0)
        template = cv2.imread('template7.png',0)
        img_gray = cv2.cvtColor(searchImage, cv2.COLOR_BGR2GRAY)
        w,h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.5 
        loc = np.where( res >= threshold)
        
        note = {}
        for pt in zip(*loc[::-1]):
            cv2.rectangle(searchImage, pt , (pt[0] + w, pt[1] + h), (0,0,255), 1)
            if pt[0] not in note.keys():
                note[pt[0]] = pt[1]
            
        midi = Midi.Midi()
        for x in sorted(note):
            midi.playNote(note[x])
            print(note[x])
            
        cv2.imshow("img", searchImage)
        cv2.waitKey(0)
