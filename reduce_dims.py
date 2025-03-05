import os
from PIL import Image


def resize_images_in_folder(folder_path):
    output_folder = os.path.join("input_images_resized")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        input_path = os.path.join(folder_path, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):
            with Image.open(input_path) as img:
                new_size = (img.width // 10, img.height // 10)
                resized_img = img.resize(new_size, Image.LANCZOS)

                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f"Immagine ridotta: {filename} -> {new_size}")


folder_path = "input_images"  # Cambia con il percorso corretto
resize_images_in_folder(folder_path)
