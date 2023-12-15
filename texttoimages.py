import os
from PIL import Image
import matplotlib.pyplot as plt

# Define the path to your sign language alphabet images folder
images_folder = r'D:\Miniproject\www.bemysenses.com\Dataset ASL Hand Gestures\grayscale_frames'

# Define a mapping from text to image filenames
sign_language_dict = {
    'A': 'a_1-19.png',
    'B': 'b_1-19.png',
    'C': 'c_1-19.png',
    'D': 'd_1-19.png',
    'E': 'e_1-19.png',
    'F': 'f_1-19.png',
    'G': 'g_1-19.png',
    'H': 'h_1-19.png',
    'I': 'i_1-19.png',
    'J': 'j_1-19.png',
    'K': 'k_1-19.png',
    'L': 'l_1-19.png',
    'M': 'm_1-19.png',
    'N': 'n_1-19.png',
    'O': 'o_1-19.png',
    'P': 'p_1-19.png',
    'Q': 'q_1-19.png',
    'R': 'r_1-19.png',
    'S': 's_1-19.png',
    'T': 't_1-19.png',
    'U': 'u_1-19.png',
    'V': 'v_1-19.png',
    'W': 'w_1-19.png',
    'X': 'x_1-19.png',
    'Y': 'y_1-19.png',
    'Z': 'z_1-19.png',
    ' ': 'space.png',  # Define a blank image for spaces
}

# Function to translate text to sign language images
def text_to_sign_language(text, sign_language_dict):
    # Create a list to store the sign language images
    sign_language_images = []

    for letter in text.upper():
        if letter in sign_language_dict:
            image_filename = sign_language_dict[letter]
            image_path = os.path.join(images_folder, image_filename)
            try:
                img = Image.open(image_path)
                sign_language_images.append(img)
            except FileNotFoundError:
                print(f"Image not found for letter: {letter}")

    return sign_language_images

# Translate text to sign language images
text_to_translate = input("Enter text: ")
translated_images = text_to_sign_language(text_to_translate, sign_language_dict)

# Concatenate and display the translated images using matplotlib
if translated_images:
    plt.figure(figsize=(12, 4))
    total_width = sum(img.width for img in translated_images)
    max_height = max(img.height for img in translated_images)
    combined_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for img in translated_images:
        combined_image.paste(img, (x_offset, 0))
        x_offset += img.width

    plt.imshow(combined_image)
    plt.axis('off')  # Turn off axis labels and ticks
    plt.show()
