from PIL import Image

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

def color_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        # Отримання значень кольору RGB
        r, g, b = pixel[:3]
        # Визначення символу ASCII відповідно до відтінку кольору
        brightness = (r + g + b) / 3
        ascii_str += ASCII_CHARS[int(brightness / 256 * len(ASCII_CHARS))]
    return ascii_str

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image)
    ascii_str = color_to_ascii(image)
    
    img_width = image.width
    
    ascii_img = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    print(ascii_img)

if __name__ == "__main__":
    image_path = input("Введіть шлях до зображення: ")
    main(image_path)
