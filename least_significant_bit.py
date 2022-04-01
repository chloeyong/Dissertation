# -*- coding: utf-8 -*-
"""
@author: Chloe Yong

This program:
    > hides a given message within a given cover image
    > extracts a message from a given stego image
"""

import numpy as np
from PIL import Image

#This function encodes the image with the secret message
def encode(imagePath, message, destination):
    #imagePath = where the image is
    #message = message you want to convert
    #dest = where you want to save the image after
    
    image = Image.open(imagePath, 'r')
    #opens the image
    
    width, height = image.size
    #width and height of image
    
    imageArray = np.array(list(image.getdata()))
    #all the bits of each pixel of the image as an array
    
    #Checking what format the image is:
    # RGB (3 x 8 bit pixels - colours)
    # RGBA (4 x 8 bit pixels - colours with transparency mask)
    if image.mode == "RGB":
        n=3
    elif image.mode == "RGBA":
        n=4
        
    #Calculates the total number of pixels in the image
    total_pixels = imageArray.size//n
    
    #Converting the message into binary
    message = message + "!STOP" #so we know when to stop decoding the message
    binary_message = ''.join([ format(ord(i), "08b") for i in message ])
    required_pixels = len(binary_message)
    
    #Check whether the image is large enough to hide the secret image
    if required_pixels > total_pixels:
        print("Image size too small")
    else: #If it change the lsb of the pixels to the bits of the message
        i = 0
        for p in range(total_pixels):
            for q in range(0,3):
                if i < required_pixels:
                    imageArray[p][q] = int(bin(imageArray[p][q]) [2:9] + binary_message[i], 2)
                    i = i + 1
    
    #we now save the new array of pixels of the image, and can use it to create the stego image
    imageArray = imageArray.reshape(height, width, n)
    stegoImage = Image.fromarray(imageArray.astype('uint8'), image.mode)
    stegoImage.save(destination)
    print('Image Encoded')
        
def decode(imagePath):
    
    image = Image.open(imagePath, 'r')
    
    imageArray = np.array(list(image.getdata()))
    
    if image.mode == 'RGB':
        n=3
    elif image.mode == 'RGBA':
        n=4
    
    total_pixels = imageArray.size//n
    
    #We need to extract the lsb of each of the pixels in the image, starting from the top left corner and storing them in groups of 8, so it is easier to convert the message back from binary to ASCII characters
    messageBits = ""
    
    for p in range(total_pixels):
        for q in range(0,3):
            messageBits = messageBits + (bin(imageArray[p][q]) [2:][-1])
    
    messageBits = [messageBits[i:i+8] for i in range(0,len(messageBits),8)]
    
    #Convert the message back from binary to ASCII characters
    message = ""
    for i in range(len(messageBits)):
            #checks whether the delimiter is at the end of the message if it is, then we can stop converting the bits, as the message has been converted back completely.
        if message[-5:] == "!STOP":
            break
        else:
            message = message + chr(int(messageBits[i], 2))
    
    if "!STOP" in message:
        print("The hidden message is: ", message[:-5])
    else:
        print("No hidden message")


def LSBS():
    print("Please select a function")
    print("1: Encode ")
    print("2: Decode ")
    function = input()
    
    if function == "1":
        print("Please enter the cover image Path: ")
        imagePath = input()
        print("Please enter the message you want to hide: ")
        message = input()
        print("Please enter the destination path to save the stego image: ")
        destination = input()
        print("Encoding...")
        encode(imagePath, message, destination)
    elif function == "2":
        print("Please enter the image path")
        imagePath = input()
        print("Decoding...")
        decode(imagePath)
    else:
        print("Invalid option chosen")
        

LSBS()
    
    
    
    
    
    
    