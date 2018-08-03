from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im, filename):
    im.save(filename,"jpeg")
    show_img(im)
    


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

def obamicon(im):
    #loads pixel data from im 
    pixels = im.getdata()

    new_pixels = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            new_pixels.append(darkBlue)
        if intensity > 182 and intensity <364:
            new_pixels.append(red)
        if intensity > 364 and intensity < 546:
            new_pixels.append(lightBlue)
        if intensity > 546:
            new_pixels.append(yellow)
            
    # save the filtered pixels as a new image
    new_image = Image.new ("RGB",im.size)
    new_image.putdata(new_pixels)
    #Add return statement
    return new_image

def grayscale(im):
    #loads pixel data from im 
    pixels = im.getdata()

    new_pixels = []

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        x=intensity//3
        filler=(x,x,x)
        new_pixels.append(filler)

    
            
    # save the filtered pixels as a new image
    new_image = Image.new ("RGB",im.size)
    new_image.putdata(new_pixels)
    #Add return statement
    return new_image


