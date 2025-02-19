import os
import cv2

from common import apply_transformation, get_parsed_args


def augment_images(input_dir, output_dir, num_augmented):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        image = cv2.imread(input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        for i in range(num_augmented):
            apply_transformation(image, output_dir, filename, i)


if __name__ == '__main__':
    args = get_parsed_args(parallel=False)
    augment_images(args.input_folder, args.output_folder, args.num_augmented)
