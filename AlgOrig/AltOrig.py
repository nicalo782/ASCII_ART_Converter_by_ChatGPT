from PIL import Image
from colorama import Fore, Style

# Визначення ASCII символів, які будуть використовуватися для створення ASCII ART з кольорами
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def resize_image(image, new_width=None):
    width, height = image.size
    if not new_width:
        aspect_ratio = height / width
        new_width = int(100 / aspect_ratio)
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def color_to_ascii(pixel):
    # Отримання значень кольору RGB
    r, g, b = pixel[:3]
    # Визначення символу ASCII відповідно до відтінку кольору
    brightness = (r + g + b) / 3
    # Вибір символу ASCII відповідно до відтінку кольору та його кольору
    index = int(brightness / 255 * (len(ASCII_CHARS)-1))
    return Fore.WHITE + ASCII_CHARS[index] + Style.RESET_ALL

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image)
    
    img_width, img_height = image.size
    
    ascii_img = ""
    for y in range(img_height):
        for x in range(img_width):
            pixel = image.getpixel((x, y))
            ascii_img += color_to_ascii(pixel)
        ascii_img += "\n"
    
    print(ascii_img)

if __name__ == "__main__":
    image_path = input("Введіть шлях до зображення: ")
    main(image_path)
