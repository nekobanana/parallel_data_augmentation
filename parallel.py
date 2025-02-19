import os
import random
import cv2
import albumentations as A
import multiprocessing

from common import transformations


def apply_transformation(image, output_dir, filename, i):
    transform_n = random.randint(0, len(transformations))
    transform_list = random.sample(transformations, transform_n)
    transform_compose = A.Compose(transform_list)
    augmented = transform_compose(image=image)['image']
    output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_aug_{i}.jpg")
    cv2.imwrite(output_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))


def process_image(filename, input_dir, output_dir, num_augmented):
    input_path = os.path.join(input_dir, filename)
    # if not os.path.isfile(input_path):
    #     return

    image = cv2.imread(input_path)
    # if image is None:
    #     print(f'Error reading {filename}')
    #     return

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with multiprocessing.Pool(processes=min(num_augmented, multiprocessing.cpu_count())) as pool:
        pool.starmap(apply_transformation,
                     [(image, output_dir, filename, i) for i in range(num_augmented)])


def augment_images(input_dir, output_dir, num_augmented=5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        process_image(filename, input_dir, output_dir, num_augmented)


    # with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    #     pool.starmap(process_image, [(filename, input_dir, output_dir, num_augmented) for filename in filenames])


if __name__ == '__main__':
    input_folder = "input_images"
    output_folder = "output_images"
    augment_images(input_folder, output_folder, num_augmented=5)
