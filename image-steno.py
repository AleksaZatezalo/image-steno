"""
Author: Aleksa Zatezalo
Date: October 2023
Description: Image stenography tool made in python.
"""

from PIL import Image

def hide_text(image_path, secret_text, output_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the secret text to binary
    binary_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)

    # Check if the image can accomidate the secret text
    image_capacity = image.width * image.height * 3
    if len(binary_secret_text) > image_capacity:
        raise ValueError("Image does not have the sufficient capacity.")

    # Hide the text
    pixels = image.load()
    index = 0
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Modify the least significant bit of each color chanel
            if index < len(binary_secret_text):
                r = (r & 0xFE) | int(binary_secret_text[index])
                index += 1
            if index < len(binary_secret_text):
                g = (g & 0xFE) | int(binary_secret_text[index])
                index += 1
            if index < len(binary_secret_text):
                b = (b & 0xFE) | int(binary_secret_text[index])
                index += 1
            pixels[i, j] = (r, g, b)

    # Save the image
    image.save(output_path)

def extract_text(image_path):
    # Open the image
    image = Image.open(image_path)

    # Extract the text
    pixels = image.load()
    binary_secret_text = ""
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

        # Extract the least significant bit of each color
        binary_secret_text += str(r & 1)
        binary_secret_text += str(g & 1)
        binary_secret_text += str(b & 1)
        
    # Convert the binary text to ASCII
    secret_text = ""
    for i in range(0, len(binary_secret_text), 8):
        char = chr(int(binary_secret_text[i:i+8], 2))
        secret_text += char
 
    return secret_text

### Test
image_path = 'image.jpg'
secret_text = "Hello, world!."
output_path = "output_image.jpg"

hide_text(image_path, secret_text, output_path)
exttext = extract_text(output_path)
print("Extracted text:", exttext)