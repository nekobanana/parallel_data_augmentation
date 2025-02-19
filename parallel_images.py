import os
import random
import cv2
import albumentations as A
import multiprocessing

from common import transformations, input_folder, output_folder, num_augmented


def apply_transformation(image, output_dir, filename, i):
    transform_n = random.randint(0, len(transformations))
    transform_list = random.sample(transformations, transform_n)
    transform_compose = A.Compose(transform_list)
    augmented = transform_compose(image=image)['image']
    output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_aug_{i}.jpg")
    cv2.imwrite(output_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))


def process_image(filename, input_dir, output_dir, num_augmented):
    input_path = os.path.join(input_dir, filename)
    image = cv2.imread(input_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(num_augmented):
        apply_transformation(image, output_dir, filename, i)


def augment_images(input_dir, output_dir, num_augmented=5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.starmap(process_image, [(filename, input_dir, output_dir, num_augmented) for filename in os.listdir(input_dir)])


if __name__ == '__main__':
    augment_images(input_folder, output_folder, num_augmented=num_augmented)
