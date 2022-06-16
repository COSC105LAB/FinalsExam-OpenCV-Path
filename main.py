import cv2
filePath = 'somerandomimage.csv'
imgFlag = int(0)
img = cv2.imread(filePath, imgFlag)
cv2.imshow("Some window title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
