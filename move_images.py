import shutil
import os
import random


def move_file(source_path_file, destination_path_file):
    # Copy the file from the source to the destination
    shutil.move(source_path_file, destination_path_file)


images_list = os.listdir("./images")

train_percentage = 80 / 100

# training_images = random.sample(images_list, int(len(images_list) * train_percentage))
# print(training_images)

# for training_image in training_images:
#     move_file(f"./images/{training_image}", "./data/images/train")

# validation_images = images_list
# print(validation_images)

# for validation_image in validation_images:
#     move_file(f"./images/{validation_image}", "./data/images/val")
