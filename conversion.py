import os
from pprint import pprint

import cv2

images_path = os.listdir("./segmentations")


def convert(image_path):
    mask = cv2.imread(f"./segmentations/{image_path}", cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    H, W = mask.shape
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # convert the contours to polygons
    polygons = []
    for cnt in contours:
        polygon = []
        for point in cnt:
            x, y = point[0]
            polygon.append(x / W)
            polygon.append(y / H)
        polygons.append(polygon)

    # print the polygons
    with open(f"./labels/{image_path.split('_')[0]}.txt", "w") as f:
        for polygon in polygons:
            for p_, p in enumerate(polygon):
                if p_ == len(polygon) - 1:
                    f.write("{}\n".format(p))
                elif p_ == 0:
                    f.write("0 {} ".format(p))
                else:
                    f.write("{} ".format(p))

        f.close()


for image_path in images_path:
    print(image_path)
    convert(image_path)
