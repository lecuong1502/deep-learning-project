import cv2

img = cv2.imread("")
if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
g = cv2.medianBlur(g, 5)

# Detect edges
e = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Smooth the image
c = cv2.bilateralFilter(img, 9, 250, 250)

# Combine
cartoon = cv2.bitwise_and(c, c, mask=e)

cv2.imshow("Cartoon", cartoon)
cv2.imwrite("cartoon_output.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()