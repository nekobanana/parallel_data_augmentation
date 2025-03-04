import argparse
import json
import os
import random
import albumentations as A
import cv2

transformations = [
        A.RandomBrightnessContrast(brightness_limit=(0.2, 0.8), contrast_limit=(0.2, 0.8), p=1),
        A.GaussNoise(std_range=(0.2, 0.8), mean_range=(-0.8, 0.8), p=1),
        A.RandomGamma(gamma_limit=(80, 120), p=1),
        A.Blur(blur_limit=(3, 5), p=1),
        A.CLAHE(clip_limit=(1, 4), p=1),
        A.OpticalDistortion(distort_limit=(-0.05, 0.05), p=1),
        A.GridDistortion(distort_limit=(-0.3, 0.3), p=1),
        A.HueSaturationValue(hue_shift_limit=(-180, 180)),
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
    parser.add_argument("-r", "--result_file", type=str, required=True, help="Path to the result file")
    return parser.parse_args()

def write_output_to_file(end_time, num_processes, num_augmented, result_file, start_time):
    result = {
        'num_processes': num_processes,
        'num_augmented': num_augmented,
        'time': end_time - start_time
    }
    print(f'Execution time: {end_time - start_time} seconds')
    if result_file:
        if not os.path.exists(os.path.dirname(result_file)):
            os.makedirs(os.path.dirname(result_file))
        with open(result_file, 'w') as f:
            json.dump(result, f)
