import matplotlib.pyplot as plt

img = plt.imread('./deveino.png')

# slice that represents the top pixels
top = img[ :-2, 1:-1]

# slice for the left pixel selection
left = img[1:-1, :-2]

# slice for the right pixel
right = img[1:-1, 2:]

#slice for the bottom pixels
bottom = img[2:, 1:-1]

# center slice pixels
center = img[1:-1, 1:-1]

# Bluring the image
blurred = (top + left + right + center + bottom) / 6

plt.imshow(img, cmap=plt.cm.hot)
plt.figure()
plt.imshow(blurred, cmap=plt.cm.hot)
plt.show()