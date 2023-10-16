"""
Author: Aleksa Zatezalo
Date: October 2023
Description: Image stenography tool made in python.
"""

# Based on https://www.geeksforgeeks.org/image-based-steganography-using-python/

from PIL import Image
import pyfiglet
import argparse
import progressBar
import time

def banner():
    """
    A function to print the image-steno banner to stdout.
    """
    
    result = pyfiglet.figlet_format("Image-Steno")
    print(result)


def createSteno():
    pBar = progressBar.progressBar("Fetching base image.")
    pBar.start()
    time.sleep(2)
    pBar.setMsg("Encoding Data.")
    time.sleep(2)
    pBar.setMsg("Creating destination image.")
    time.sleep(2)
    pBar.stop()
    time.sleep(0.2)
    return True

def main():
    banner()
    createSteno()

if __name__ == "__main__":
    main()