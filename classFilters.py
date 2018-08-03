from PIL import Image



def obamicon(im):
    #loads pixels data from im
    pixels = im.getdata()

    new_pixels=[]

    darkBlue= (0,51,76)
    red=(217,26,33)
    lightBlue=(112,150,158)
    yellow=(252,227,166)

    for pixel in pixels:
        intensity=pixel[0]+pixel[1]+pixel[2]
        #or intensity=sum(oixels)

        if intensity <182:
            new_pixels.append(darkBlue)

        elif 182<intensity and intensity<=364:
            new_pixels.append(red)

        elif 364<intensity and intensity<=546:
            new_pixels.append(lightBlue)

        elif intensity>546:
            new_pixels.append(yellow)

        #save the filtered pixels as a new image
    new_image= Image.new("RGB",im.size)
    new_image.putdata(new_pixels)
    return new_image

#################################################
################ NEW FILTERS! ###################
#################################################

def newfilter(im):
    #loads pixels data from im
    pixels = im.getdata()

    new_pixels=[]

    paleBlue= (169, 252, 252)
    pink=(244, 97, 220)
    lightBlue=(7, 239, 216)
    paleGreen=(174, 252, 159)

    for pixel in pixels:
        intensity=pixel[0]+pixel[1]+pixel[2]
        #or intensity=sum(oixels)

        if intensity <182:
            new_pixels.append(paleBlue)

        elif 182<intensity and intensity<=364:
            new_pixels.append(pink)

        elif 364<intensity and intensity<=546:
            new_pixels.append(lightBlue)

        elif intensity>546:
            new_pixels.append(paleGreen)

        #save the filtered pixels as a new image
    new_image= Image.new("RGB",im.size)
    new_image.putdata(new_pixels)
    return new_image

def invert(im):
        #loads pixels data from im
    pixels = im.getdata()

    new_pixels=[]


    for pixel in pixels:
        new_pixels.append((255-pixel[0], 255-pixel[1], 255-pixel[2]))


    new_image= Image.new("RGB",im.size)
    new_image.putdata(new_pixels)
    return new_image


def pink(im):
    pixels = im.getdata()

    new_pixels = []

    deepPink = (255,20,147)
    pink = (255,192,203)
    orchid = (218,112,214)

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            new_pixels.append(deepPink)
        elif intensity > 182 and intensity < 364:
           new_pixels.append(pink)
        elif intensity > 546:
           new_pixels.append(orchid)

     # save the filtered pixels as new image
    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return(new_image)
    #add a return statement


def obamicons(im):
    #loads pixed data from im
    pixels = im.getdata()

    new_pixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    #to do: make variables for the rest of the colors

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 260:
            new_pixels.append(darkBlue)

        elif 182 < intensity < 400:
            new_pixels.append(red)

        elif 364 < intensity < 560:
            new_pixels.append(lightBlue)

        elif intensity > 500:
            new_pixels.append(yellow)
        #TODO: check if pixel is in other ranges, use elif ststements

    #save the filtered pixels as a new image
    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
     #TODO: add a return statement
    return new_image


def invert(im):
    pixels = im.getdata()
    new_pixels = []

    for pixel in pixels:
        new_pixels.append((255-pixel[0],255-pixel[1],255-pixel[2]))

    new_image = Image.new("RGB",im.size)
    new_image.putdata(new_pixels)
    return new_image

def dogFilter(im):
    pixels = im.getdata()

    colors = (86,224,94)

    new_pixels = []

    for pixel in pixels:

        new_pix = (pixel[0] + colors[0], pixel[1] + colors[1], pixel[2] + colors[2])

        new_pixels.append(new_pix)
    new_image = Image.new("RGB",im.size)
    new_image.putdata(new_pixels)
    return new_image

def experiment1(im):
    pixels = im.getdata()

    new_pixels = []


    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        x = intensity//3
        chicken = (x,x,x)
        new_pixels.append(chicken)


        #save the filtered pixels as

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image


def redScale(im):
    pixels = im.getdata()

    new_pixels = []

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        x = intensity//3
        new_pixels.append(x)


    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image


def kelliecon(im):
    pixels = im.getdata()

    new_pixels = []

    purple = (193,0,219)
    orange = (225,58,0)
    brown = (112,42,0)
    yellow = (252,227,66)
    #TODO: make variables for the rest of colors

    for pixel in pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            new_pixels.append(brown)
        elif 182< intensity < 364:
            new_pixels.append(purple)
        elif 364< intensity < 546:
            new_pixels.append(orange)
        elif intensity> 546:
            new_pixels.append(yellow)

    #Save the filtered pixels as a new image
    new_image = Image.new("RGB",im.size)
    new_image.putdata(new_pixels)

    #TODO add a return statement
    return new_image
