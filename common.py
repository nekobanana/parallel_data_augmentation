import albumentations as A

transformations = [
        A.RandomBrightnessContrast(brightness_limit=(0.2, 0.8), contrast_limit=(0.2, 0.8), p=1),
        A.GaussNoise(std_range=(0.2, 0.8), mean_range=(-0.8, 0.8), p=1),
        A.RandomGamma(gamma_limit=(80, 120), p=1),
        A.Blur(blur_limit=(3, 5), p=1),
        A.CLAHE(clip_limit=(1, 4), p=1)
    ]

input_folder = "input_images"
output_folder = "output_images"
num_augmented = 100