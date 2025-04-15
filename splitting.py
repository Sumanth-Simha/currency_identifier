import os
import random
import shutil
from pathlib import Path

# SET THESE: Update the paths accordingly
dataset_dir = r"C:\Users\rsuma\OneDrive\Desktop\My Project\currencyclassify\dataset"
image_dir = os.path.join(dataset_dir, "images")
label_dir = os.path.join(dataset_dir, "labels")

# Create new folders for train and val
for split in ['train', 'val']:
    os.makedirs(os.path.join(image_dir, split), exist_ok=True)
    os.makedirs(os.path.join(label_dir, split), exist_ok=True)

# Get all image files
images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(images)

# Split ratio (80% train, 20% validation)
split_ratio = 0.8
split_idx = int(len(images) * split_ratio)
train_images = images[:split_idx]
val_images = images[split_idx:]

# Move image files
def move_files(image_list, split):
    for img_file in image_list:
        # Move image
        src_img = os.path.join(image_dir, img_file)
        dst_img = os.path.join(image_dir, split, img_file)
        shutil.move(src_img, dst_img)

        # Move label file
        label_file = Path(img_file).with_suffix('.txt').name
        src_label = os.path.join(label_dir, label_file)
        dst_label = os.path.join(label_dir, split, label_file)

        if os.path.exists(src_label):
            shutil.move(src_label, dst_label)

# Move images and labels into their respective folders
move_files(train_images, 'train')
move_files(val_images, 'val')

print("✅ Dataset successfully split into 'train' and 'val'.")
