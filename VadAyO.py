import os
import cv2 as cv

path = "Images/"
images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = path + "/" + file
        images.append(file)

count = len(images)
frame = cv.imread(images[0])
width, height, layers = frame.shape
size = (width, height)
print(size)
out = cv.VideoWriter("project.avi", cv.VideoWriter.fourcc(*"DIVX"), 0.8, size)
for i in range(0, count-1):
    out.write(cv.imread(images[i]))

out.release()
cv.waitKey(0)
print("Done")
