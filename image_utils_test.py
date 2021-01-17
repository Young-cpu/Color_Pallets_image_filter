from image_utils import read_ppm, save_ppm, get_width_height
if __name__ == "__main__":
    file = input("image file> ")
    image = read_ppm(file)

    # Test writing it unmodified
    save_ppm("unmodified.ppm", image)

    # rotate the colors, it's a simple manipulation, but it's always a fun one.
    width, height = get_width_height(image)
    for x in range(width):
        for y in range(height):
            r, g, b = image[x][y]
            image[x][y] = (g, r, b)
    save_ppm("modified.ppm", image)


