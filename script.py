import cv2


model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


photo1 = cv2.imread('Capture1.JPG')
face1 = model.detectMultiScale(photo1)
p1x1 = face1[0][0]
p1y1 = face1[0][1]
p1x2 = p1x1 + face1[0][3]
p1y2 = p1y1 + face1[0][2]

photo2 = cv2.imread('Capture.JPG')
tphoto2 = cv2.imread('Capture.JPG')



face2 = model.detectMultiScale(photo2)
p2x1 = face2[0][0]
p2y1 = face2[0][1]
p2x2 = p2x1 + face2[0][3]
p2y2 = p2y1 + face2[0][2]

cphoto1 = photo1[p1y1:p1y2, p1x1:p1x2]
cphoto2 = photo2[p2y1:p2y2, p2x1:p2x2]
tcphoto2 = tphoto2[p2y1:p2y2, p2x1:p2x2]

for i in range(p2y1, p2y1+len(cphoto1)):
    for j in range(p2x1, p2x1+len(cphoto1)):
        tphoto2[i][j] = cphoto1[i-p2y1][j-p2x1]
for i in range(p1y1, p1y1+len(cphoto2)):
    for j in range(p1x1, p1x1+len(tcphoto2)):
        photo1[i][j] = cphoto2[i-p1y1][j-p1x1]


photo1 = cv2.resize(photo1, (600, 500))
tphoto2 = cv2.resize(tphoto2, (600, 500))

cv2.imshow('Pic 1', photo1)
cv2.imshow('Pic 2', tphoto2)
cv2.waitKey()
cv2.destroyAllWindows()