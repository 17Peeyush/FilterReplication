# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

def copy(image):
    """
    param image: Input image
    :return: copy of the input image
    """
    width = image.width
    height = image.height

    # Create new image to create copy of original image
    copy_image = SimpleImage.blank(width , height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            copy_image.set_pixel(x, y, pixel)
    return copy_image

def truncate(b):
    return min(255,max(0, b))

def red_filter(image, control):
    """
    :param image: Input image
    :param control: integer value by user to control the effect of filter
    :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        pixel.red = truncate(pixel.red + control)
        pixel.green = truncate(pixel.red + control)
        pixel.blue = truncate(pixel.red + control)
    image.pil_image.save('red_filter1.png')

def brightness(image, control):
    """
        :param image: Input image
        :param control: integer value by user to control the effect of filter(increase or decrease brightness)
        :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        pixel.red = truncate(pixel.red + control)
        pixel.green = truncate(pixel.green + control)
        pixel.blue = truncate(pixel.blue + control)
    image.pil_image.save('brightness_filter1.png')


def blue_filter(image, control):
    """
        :param image: Input image
        :param control: integer value by user to control the effect of filter
        :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        pixel.red = truncate(pixel.blue + control)
        pixel.green = truncate(pixel.blue + control)
        pixel.blue = truncate(pixel.blue + control)
    image.pil_image.save('blue_filter1.png')

def green_filter(image, control):
    """
        :param image: Input image
        :param control: integer value by user to control the effect of filter
        :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        pixel.red = truncate(pixel.red + control)
        pixel.green = truncate(pixel.red + control)
        pixel.blue = truncate(pixel.red + control)
    image.pil_image.save('green_filter1.png')

def luminosity(r, g, b):
    """
    :param r: rgb red value of a pixel
    :param g: rgb green value of a pixel
    :param b: rgb blue value of a pixel
    :return: luminosity of a pixel having rgb values r, g, b
    """
    r = r / 255
    g = g / 255
    b = b / 255
    max_rgb = max(max(r, b), max(b, g))
    min_rgb = min(min(r, b), min(r, b))
    return 1 / 2 * (max_rgb + min_rgb), max_rgb, min_rgb


def hue(r, g, b):
    """
       :param r: rgb red value of a pixel
       :param g: rgb green value of a pixel
       :param b: rgb blue value of a pixel
       :return: hue of a pixel having rgb values r, g, b
       """
    r = r / 255
    g = g / 255
    b = b / 255
    h = -1
    if (r >= g) and (g >= b):
        if(r-b) != 0:
            h = 60 * ((g - b) / (r - b))
        else:
            h=0
    elif (g > r) and (r >= b):
        h = 60 * (2 - (r - b) / (g - b))
    elif (g >= b) and (b > r):
        h = 60 * (2 + (b - r) / (g - r))
    elif (b > g) and (r > g):
        if(b - r) != 0:
            h = 60 * (4 - (g - r) / (b - r))
        else:
            h = 0
    elif (b > r) and (r >= g):
        h = 60 * (4 + (r - g) / (b - g))
    elif (r >= b) and (b > g):
        h = 60 * (6 - (b - g) / (r - g))
    rng = 255
    h = 0 + (h * rng) / 360
    return h


def saturation(l, max_rgb, min_rgb):
    """
       :param r: rgb red value of a pixel
       :param g: rgb green value of a pixel
       :param b: rgb blue value of a pixel
       :return: saturation of a pixel having rgb values r, g, b
       """
    if (l < 1):
        deno = (1 - abs(2 * l - 1))
        if deno != 0:
            s = (max_rgb - min_rgb) / deno
        else:
            s = 0
    else:
        s = 0
    return s


def compute_luminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula
    to weight red, green, and blue values appropriately.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def gray_filter(image):
    """
        :param image: Input image
        :return: new image with grayscale filter
    """
    image = copy(image)
    for pixel in image:
        luminosity_image=compute_luminosity(pixel.red,pixel.green,pixel.blue)
        pixel.red = luminosity_image
        pixel.green = luminosity_image
        pixel.blue = luminosity_image
    image.pil_image.save('gray_filter1.png')

def ghost_filter(image):
    """
        :param image: Input image
        :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        l, max_rgb, min_rgb = luminosity(pixel.red, pixel.green, pixel.blue)
        h = hue(pixel.red, pixel.green, pixel.blue)
        s = saturation(l, max_rgb, min_rgb)
        pixel.red = h
        pixel.green = s
        pixel.blue = l
    image.pil_image.save('ghost_filter1.png')

def negative_filter(image):
    """
        :param image: Input image
        :return: new image with applied filter
    """
    image = copy(image)
    for pixel in image:
        pixel.red = 255 - pixel.red
        pixel.green = 255 - pixel.green
        pixel.blue = 255 - pixel.blue
    image.pil_image.save('negative_filter1.png')

def sepia_filter(image):
    """
      :param image: Input image
      :return: new image with sepia filter
    """
    image = copy(image)
    for pixel in image:
        tr = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        tg = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        tb = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        if tr > 255:
            tr = 255
        if tg > 255:
            tg = 255
        if tb > 255:
            tb = 255
        pixel.red = tr
        pixel.green = tg
        pixel.blue = tb
    image.pil_image.save('sepia_filter1.png')

def main():
    original = SimpleImage('a.jpg')
    # ghost_filter(original)
    # negative_filter(original)
    sepia_filter(original)
    # brightness(original, 20)
    # blue_filter(original, 30)
    # gray_filter(original)
    # green_filter(original, 45)

if __name__ == '__main__':
    main()
