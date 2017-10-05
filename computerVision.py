import cv2
import numpy as np

cap = cv2.imread('path/try.jpg', cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

lower = np.array([40,20,0])
upper = np.array([255,255,255])

mask = cv2.inRange(hsv, lower, upper)

mask_inv = cv2.bitwise_not(mask)
res = cv2.bitwise_and(cap, cap, mask = mask)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.blobColor= 255
params.filterByColor = True
'''
params.minThreshold = 10;
params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 1500
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
'''
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(mask_inv)
im_with_keypoints = cv2.drawKeypoints(cap, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print(str(keypoints))

cv2.imshow('orignal', cap)
cv2.imshow('mask', mask)
cv2.imshow('res', res)


cv2.imshow('mask_inv', mask_inv)
#cv2.imshow('im_with_keypoints', im_with_keypoints)

cv2.waitKey(0)
cv2.destroyAllWindows()
