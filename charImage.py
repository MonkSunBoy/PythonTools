from PIL import Image

#ASCII_CHARS = ['@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', ' ']
#ASCII_CHARS = [' ', ' ', ':', '?', '*', 'O', 'E', 'G', 'B', '#', '@']
#ASCII_CHARS = [".","`","'",":","-",",",";","\"","_","~","!","^","i","r","|","/","I","=","<", ">","*","l","\\","1","t","+","j","?","v",")","(","L","f","{","7","}","J","T", "c","x","z","]","[","u","n","s","Y","o","F","y","e","2","a","V","k","3","h", "Z","C","4","P","5","A","q","X","p","E","%","0","U","d","b","6","K","S","9", "#","H","w","G","$","O","g","D","8","R","Q","m","B","&","N","W","M","@"]
ASCII_CHARS = ["@","M","W","N","&","B","m","Q","R","8","D","g","O","$","G","w","H","#","9", "S","K","6","b","d","U","0","%","E","p","X","q","A","5","P","4","C","Z","h", "3","k","V","a","2","e","y","F","o","Y","s","n","u","[","]","z","x","c","T", "J","}","7","{","f","L","(",")","v","?","j","+","t","1","\\","l","*",">","<", "=","I","/","|","r","i","^","!","~","_","\"",";",",","-",":","'","`","."]

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=3):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    print image_ascii

if __name__=='__main__':
    import sys

    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)
