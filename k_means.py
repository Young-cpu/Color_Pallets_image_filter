"""
Younghyun Jung

I follow most of guideline of project. It means that I created most of functions that professor recommended us.
However, I think that I better break into separate parts for update_means because it is quite hard to check the error
when I make "assigned_color" at the same function.
Except for that, I created rest of recommended functions for k-means algorithms.
"""
from image_utils import *
from math import *

def k_means(image, k):
    """
    Function of k_algorithms, it takes k number of random guess as initial guess.
    With this initial guess, we are able to update an assignment and means list
    :param image: image is the input from the user
    :param k: k is the number of colors from the user.
    :return: It is going to return 2 tuples, the means list and assignment list.
    """
    #make a initial means_list
    means = initial_guess(k)

    #With this means_list, it creates new assignment.
    assignment = create_assignment(image, means)
    assignment = update_assignment(image, means)

    #I made temp_assignemnt list for comparing between initial assignment and updated assignments.
    temp_assignment = []

    # Since the assignment and temp_assignment eventually converge with each other. Hence, I set the
    # boolean expression as assignment != assignment.
    while assignment != temp_assignment:
        temp_assignment = assignment
        means = update_means_list(image, assignment, k)
        assignment = update_assignment(image, means)
    return means, assignment

def initial_guess(k):
    """
    It is the function for making a random tuple for initial means list.
    With this means, I am going to create assignments and update means list.
    :param k: k is the number of colors from the user.
    :return: it will return the random r, g, b for number of k tuples.
    """
    i = 1
    #make an empty list for appending random means.
    random_guess = []
    # It is the loop making random tuples in the random_guess list until the size of k.
    while i <= k:
        r, g, b = random_color()
        random_guess.append((r, g, b))
        i += 1
    return random_guess

def create_assignment(image, means):
    """
    :param image: it is the image from the user
    :param means: it is the initial means list
    :return: It will create initial assignment list-of-lists based on the means list.
    """
    # make an empty list of assignment and temp_assignment.
    # temp_assignment is needed to make a list of list.
    # it will take list of element and will put a list into assignment.
    assignment = []
    temp_assignment = []

    # create the assignment list which is as big as image file.
    for w in range(len(image)):
        for h in range(len(image[0])):
            temp_assignment.append(0)
        assignment.append(temp_assignment)
    #temp_assignment will be empty list.
        temp_assignment = []

    return assignment

def update_assignment(image, means):
    """
    This function updates assignments.
    :param image: It is the image file from the user.
    :param means: k long means list, It represents the center of each cluster of colors.
    :return: It is going to return the "assignments" which is filled with indexes closets meant to image pixel.
    """
    # make an empty list of assignment and temp_assignment.
    # temp_assignment is needed to make a list of list.
    assignment = []
    temp_assignment = []

    # update the list of closest indexes based on the image and means.
    for w in range(len(image)):
        for h in range(len(image[0])):
            #temp_assignment will append the list of closest indexs into the assignment.
            temp_assignment.append(label(image[w][h], means))
        assignment.append(temp_assignment)
        # temp assignemnt will be emptied
        temp_assignment = []
    return assignment

def update_means_list(image, assignments, k):
    """
    :param image:image is the file from the user
    :param assignments: assignments have the indexes where the pixels belongs to.
    :param k: the numbers of color from the user
    :return: It will return the updated means_list which has the average of color assigned to particular indexes.
    """
    #Make an empty k long means - list it has k number of zeroes in the list.
    means = [0] * k

    for i in range(k):
        # take a list of the colors in image that are assigned to assignments.
        assigned_colors = []
        assigned_colors = update_assigned_colors(image, assignments, i, assigned_colors)

        #If no color is assigned in the assigned_color. It will return the black.
        if len(assigned_colors) == 0:
            means[i] = (0,0,0)
        else:
            means[i] = average_color(assigned_colors)
    return means

def update_assigned_colors(image, assignments, i, assigned_colors):
    """
    :param image: image is the input from the user.
    :param assignments: the list-of-list which has the index of "closest" means to image pixels.
    :param i: i is the index in the "update_means_list" it keeps changing.
    :return:  It is going to return the assigned_colors which has bunch of image pixels assigned to to cluster i.
    """
    index = i
    #If assignments_list has the same value with the index, it will put the pixels into the assigned_colors.
    for h in range(len(image)):
        for w in range(len(image[0])):
            if index == assignments[h][w]:
                assigned_colors.append(image[h][w])
    return assigned_colors

def distance(c1, c2):
    """
    This function is computing the distance between two tuples(colors)
    :param c1:Tuple from the image
    :param c2:Tuple from the means list
    :return: It is going to return double type of the length between c1 and c2
    """
    r_1, g_1, b_1 = c1
    r_2, g_2, b_2 = c2
    # Calculating the distance between two tuples.
    length = sqrt(((r_1 - r_2) **2) + ((g_1 - g_2) **2) + ((b_1 - b_2) ** 2))
    return length

def label(tuple, means):
    """
    Ths function is looking for the closest tuple with means list
    :param tuple: It is the pixel from the image file.
    :param means: It is the random means that I get initially.
    :return: It is going to return the index of closest tuple in the means list.
             It will be helpful to find out which tuple list in means is closest to tuple which is assigned from user.
    """
    # closest_1 is setting the initial distance between means list and tuple
    closest_1 = distance(tuple, means[0])
    # set the initial closest tuple in means list.
    closest_tuple = 0
    # loop looking for the closest tuple in means list.
    for i in range(1, len(means)):
        closest_2 = distance(tuple, means[i])
        if closest_2 < closest_1:
            closest_1 = closest_2
            closest_tuple = i
    return closest_tuple

# This function is making average color of list.
def average_color(list_colors):
    """
    This function is for making the average of list of colors.
    :param list_colors: list_colors is the list. It is mainly from assigned_colors above.
    :return: returns the average of each r, g, b colors in list_colors
    """
    #r,g,b are the red, green and blue
    r = g = b = 0

    #This is the length of list_colors.
    #I will use this number for the range of loop below.
    #Also, I will use this when I divide r, g, b.

    length_list = len(list_colors)

    # Since the list_colors is a tuple in the list, I have to extract each number every in list_colors by using list_colors[i][0, 1, 2].
    # Add each r, g, b because of looking for the average color.
    for i in range(length_list):
        r_1, g_1, b_1 = list_colors[i]
        r += r_1
        g += g_1
        b += b_1

    # makes a mean of colors divided by length_list
    # Use the "//" because pixel does not have decimals.
    r = r // length_list
    g = g // length_list
    b = b // length_list

    return((r, g ,b))