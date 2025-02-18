import os
import random

import cv2
import albumentations as A

def augment_images(input_dir, output_dir, num_augmented=5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if not os.path.isfile(input_path):
            continue

        image = cv2.imread(input_path)
        if image is None:
            print(f'Error reading {filename}')
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        for i in range(num_augmented):
            transform = A.Compose([
                A.RandomBrightnessContrast(brightness_limit=(0.2, 0.8), contrast_limit=(0.2, 0.8), p=get_rand()),
                A.GaussNoise(std_range=(0.2, 0.8), mean_range=(-0.8, 0.8), p=get_rand()),
                A.RandomGamma(gamma_limit=(80, 120), p=get_rand()),
                A.Blur(blur_limit=(3, 5), p=get_rand()),
                A.CLAHE(clip_limit=(1, 4), p=get_rand()),
            ])

            augmented = transform(image=image)['image']
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_aug_{i}.jpg")
            cv2.imwrite(output_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))


def get_rand():
    return random.uniform(0, 1)


if __name__ == '__main__':
    input_folder = "input_images"
    output_folder = "output_images"
    augment_images(input_folder, output_folder, num_augmented=5)