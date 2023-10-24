"""
Author: Aleksa Zatezalo
Date: October 2023
Description: Image stenography tool made in python.
"""

from PIL import Image

class image_steno():
    def __init__(self, image_path="", secret_text="", output_path=""):
         super(image_steno, self).__init__()
         self.image = Image.open(image_path)
         self.image_path = image_path
         self.secret_text = secret_text
         self.output_path = output_path


    def hide_text(self):
        # Open the image

        # Convert the secret text to binary
        binary_secret_text = ''.join(format(ord(char), '08b') for char in self.secret_text)

        # Check if the image can accomidate the secret text
        image_capacity = self.image.width * self.image.height * 3
        if len(binary_secret_text) > image_capacity:
            raise ValueError("Image does not have the sufficient capacity.")

        # Hide the text
        pixels = self.image.load()
        index = 0
        
        for i in range(self.image.width):
            for j in range(self.image.height):
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
        self.image.save(self.output_path)

    def extract_text(self):
        # Open the image
        image = Image.open(self.output_path)

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