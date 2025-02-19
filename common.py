import argparse
import os
import random
import albumentations as A
import cv2

transformations = [
        A.RandomBrightnessContrast(brightness_limit=(0.2, 0.8), contrast_limit=(0.2, 0.8), p=1),
        A.GaussNoise(std_range=(0.2, 0.8), mean_range=(-0.8, 0.8), p=1),
        A.RandomGamma(gamma_limit=(80, 120), p=1),
        A.Blur(blur_limit=(3, 5), p=1),
        A.CLAHE(clip_limit=(1, 4), p=1)
    ]

def apply_transformation(image, output_dir, filename, i):
    transform_n = random.randint(0, len(transformations))
    transform_list = random.sample(transformations, transform_n)
    transform_compose = A.Compose(transform_list)
    augmented = transform_compose(image=image)['image']
    output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_aug_{i}.jpg")
    cv2.imwrite(output_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))

def get_parsed_args(parallel: bool = True):
    parser = argparse.ArgumentParser(description="Augment images in a folder.")
    parser.add_argument("-i", "--input_folder", type=str, required=True, help="Path to the input folder containing images")
    parser.add_argument("-o", "--output_folder", type=str, required=True, help="Path to the output folder for augmented images")
    parser.add_argument("-a", "--num_augmented", type=int, required=True, help="Number of augmented images to generate per input image")
    if parallel:
        parser.add_argument("-p", "--processes", type=int, required=True, help="Number of parallel processes")
    return parser.parse_args()