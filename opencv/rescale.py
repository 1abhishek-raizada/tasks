import cv2 as cv

img=cv.imread('photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)

    dimensions= (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
cv.imshow('Catresized',rescaleFrame(img,scale=.30))

# capture=cv.VideoCapture('videos/dog.mp4')
# while True:
#     isTrue,frame=capture.read()
#     resizedFrame=rescaleFrame(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('Video_Resized',resizedFrame)
#     if cv.waitKey(60) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()



cv.waitKey(0)