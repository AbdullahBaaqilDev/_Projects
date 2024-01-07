from json import load, dump
from random import randint
import PIL.Image

support_path = __file__
project_path_list = support_path.split("\\")[:-2]
for index in range(1, len(project_path_list) * 2, 2):
    project_path_list.insert(index, "\\")
PROJECT_PATH = "".join(project_path_list)


def generate_block_id():
    block_id = "3"
    for digit in range(5):
        block_id += str(randint(0,9))

    return int(block_id)

def create_json(path):
    with open(path, "x") as file:
        init_data = {
            "blocks": [
                {
                    "id": generate_block_id(),
                    "hue": 120,
                    "points": [
                        (0,0)
                    ]
                },
            ],
            "saved_games": [],
            "highest_score": 0,
        }
        dump(init_data, file, indent = 4)

def load_json(path):
    with open(path, "r") as file:
        return load(file)

def update_json(path, new_dict):
    with open(path, "w") as file:
        dump(new_dict, file, indent = 4)

def change_saturation(image: PIL.Image.Image, value):
    # Convert the image to the HSV color space
    hsv_image = image.convert("HSV")
    h, s, v = hsv_image.split()

    # Apply the saturation change
    new_s = s.point(lambda x: value)
    
    # Merge the modified HSV channels
    hsv_rotated = PIL.Image.merge("HSV", (h, new_s, v))
    
    # Convert the rotated image back to the RGB color space
    rgb_rotated = hsv_rotated.convert("RGB")

    return rgb_rotated

def hue_rotate(image: PIL.Image.Image, angle):
    # Convert the image to the HSV color space
    hsv_image = image.convert("HSV")
    h, s, v = hsv_image.split()

    # Apply the hue rotation
    h_rotated = h.point(lambda x: angle)

    # Merge the modified HSV channels
    hsv_rotated = PIL.Image.merge("HSV", (h_rotated, s, v))

    # Convert the rotated image back to the RGB color space
    rgb_rotated = hsv_rotated.convert("RGB")

    return rgb_rotated

# # Open the image
# image = PIL.Image.open("D:\Abdullah\PROGRAMES\Coding\.Python\.Projects\Project14_BlockPuzzle\\assets\\block.png")
# # Apply hue rotation
# green_image = change_saturation(image, 255)
# green_image = hue_rotate(green_image, 100)
# # Save the green image
# green_image.save("D:\Abdullah\PROGRAMES\Coding\.Python\.Projects\Project14_BlockPuzzle\\assets\\blockg.png")