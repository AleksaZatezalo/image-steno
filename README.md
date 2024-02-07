# Image Steno
An image stenography tool made in python. Takes an input image via standart input, an ouput image name, and a message. It encodes the message in the input image and saves to file with the name output image. A flag and an input image can also be used to decode a message.

## Image Stenography Overview
Stenography is a method of hiding secret data in images, audio, or video. When properly done, this hidden message is not visible to the human eye and special tools must be used to reveal it. In this manner the hidden messages appear to be something else: images, articles, shopping lists, or some other cover text. The word steganography comes from the Greek word steganographia, which combines the words steganós, meaning "covered or concealed", and -graphia meaning "writing". The advantage of stenography is that a concealed message can not be identified as such.

The idea behind image stenography is very simple. Images are composed of digital data (pixels), which describes what’s inside the picture, usually the colors of all the pixels. Select pixels are altered to represent characters in an encoded message. 

Find more info and a detailed tutorial on image stenography here: https://www.geeksforgeeks.org/image-based-steganography-using-python/.

# Project Structure
This project contains three files critical files: main.py, image-steno.py, and progressBar.py.  The main.py file combines and exacutes image-steno.py & progressBar.py in one file. The image-steno.py file performs the stenogrphy while progressBar.py adds visual flair.

## Contribution Guidelines
When contributing to this repository, please first discuss the change you wish to make via issue here on GitHub. Make sure all pull requests are tagged with a specific ticket number found in the repositories issues section.Before making any changes please create your own branch. Follow all three points below before opening a PR:
1. Any changes you want to create must be tagged to an issue opened on this repo. If an issue you've found does not yet exit, please open it.
2. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
3. Make sure all corresponding test cases pass.
4. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.

## Known Issues
A list of known issues and features that are currently being addressed are maintained on the github issues tab. Please look at the list of known issues before raising a new issue.

## Donation Link
If you have benefited from this project and use Monero please consider donanting to the following address:
47RoH3K4j8STLSh8ZQ2vUXZdh7GTK6dBy7uEBopegzkp6kK4fBrznkKjE3doTamn3W7A5DHbWXNdjaz2nbZmSmAk8X19ezQ
