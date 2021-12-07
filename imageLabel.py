import os
from PIL import Image

folder_images = "C:/Users/samue/OneDrive/Documents/Samuel_Studies/Y3 Sem 1/Machine Learning/Project/plant-seedlings-classification/Loose Silky-bent/Loose Silky Bent/train"
className = "Loose Silky-bent"
size_images = dict()

file = open(folder_images+".csv", "w")
file.write("filename, width, height, class, xmin, ymin, xmax, ymax \n")
file.close()

for dirpath, _, filenames in os.walk(folder_images):
    for path_image in filenames:
        image = os.path.abspath(os.path.join(dirpath, path_image))
        with Image.open(image) as img:
            width, height = img.size
            with open(folder_images+".csv", "a") as file_object:
                file_object.write(path_image + ", "+ str(width)+ ", "+ str(height)+", "+ className +", 1, 1, "+ str(width)+ ", "+ str(height)+ "\n")
                print(path_image, ", " ,str(width), ", ", str(height))
                file_object.close()
print(folder_images +".csv")
