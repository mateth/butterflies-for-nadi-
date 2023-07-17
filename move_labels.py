import shutil
import os
import random


def move_file(source_path_file, destination_path_file):
    # Copy the file from the source to the destination
    shutil.move(source_path_file, destination_path_file)


labels_list = os.listdir("./labels")

## Movemos las de training

# train_percentage = 80 / 100

# training_labels = random.sample(labels_list, int(len(labels_list) * train_percentage))
# print(training_labels)

# for training_label in training_labels:
#     move_file(f"./labels/{training_label}", "./data/labels/train")


## Movemos las de validation
validation_labels = labels_list
print(validation_labels)

for validation_label in validation_labels:
    move_file(f"./labels/{validation_label}", "./data/labels/val")
