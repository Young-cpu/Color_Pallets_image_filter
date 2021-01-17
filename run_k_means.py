"""
Younghyun Jung
This file is making a new file with the number of "k" which is input from the user.
As it goes through k-means algorithm, it will replace pixels of original image.
In the end, it will recreate image file only with number of "k"
"""
from k_means import *
from image_utils import *

if __name__ == "__main__":
    input_file = input("Name of image file > ")
    k = int(input("How many number of colors do you want for this image? > "))
    output_file = input("Name of output file > ")

    #reading the image file.
    image = read_ppm(input_file)

    #Get the means list and assignment list
    means, assignments = k_means(image, k)

    #Changing the pixels of image with the pixels gotten from means list and assignment.
    for w in range(len(image)):
        for h in range(len(image[0])):
            image[w][h] = means[assignments[w][h]]

    save_ppm(output_file, image)

