

#Display an Image Using Open CV
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("logo.jpg")
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()
plt.imshow(newImg)
plt.show()

#Wait for any key before image disappears
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(img)