import multiprocessing
import os
import time

import cv2

from common import apply_transformation, get_parsed_args, write_output_to_file


def augment_images(input_dir, output_dir, num_augmented, num_processes, result_file):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    start_time = time.time()
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        image = cv2.imread(input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        with multiprocessing.Pool(processes=num_processes) as pool:
            pool.starmap(apply_transformation, [(image, output_dir, filename, i) for i in range(num_augmented)])

    end_time = time.time()
    write_output_to_file(end_time, 1, num_augmented, result_file, start_time)


if __name__ == '__main__':
    args = get_parsed_args()
    augment_images(args.input_folder, args.output_folder, args.num_augmented, args.processes, args.result_file)
