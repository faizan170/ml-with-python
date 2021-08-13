import cv2
import matplotlib.pyplot as plt
import os

BASE_DIR = "E:/Datasets/IntelEnv/seg_test/seg_test/buildings/"

images = os.listdir(BASE_DIR)

'''
    
image1 = cv2.imread(BASE_DIR + images[0])
image2 = cv2.imread(BASE_DIR + images[1])


image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

# ROWS, COLUMNS

plt.figure(figsize=(15, 10))

plt.subplot(1, 10, 1)
plt.imshow(image1)
plt.title(images[0])
plt.axis('off')
plt.subplot(1, 10, 2)
plt.imshow(image2)
plt.title(images[1])
plt.axis('off')


plt.show()

'''

plt.figure(figsize=(15, 10))

for i, image_name in enumerate(images[:50]):
    image = cv2.imread(BASE_DIR + image_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.subplot(5, 10, i+1)
    plt.title(image_name)
    plt.axis('off')
    plt.imshow(image)


plt.show()