import os
from PIL import Image

def resize_images_in_folder(folder_path, size=(100, 100)):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, filename)
            with Image.open(file_path) as img:
                resized_img = img.resize(size, Image.LANCZOS)
                resized_img.save(file_path)
                print(f'Resized and saved: {file_path}')

resize_images_in_folder('./')
