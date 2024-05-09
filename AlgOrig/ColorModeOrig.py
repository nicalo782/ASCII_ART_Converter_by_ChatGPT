from PIL import Image
#ColorMode
# Визначення ASCII символів, які будуть використовуватися для створення ASCII ART з кольорами
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

# Функція для конвертації кольорів RGB у відповідний ANSI escape код кольору
def rgb_to_ansi(r, g, b):
    return "\033[38;2;%d;%d;%dm" % (r, g, b)

def resize_image(image, new_width=None):
    width, height = image.size
    if not new_width:
        aspect_ratio = height / width
        new_width = int(100 / aspect_ratio)
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def brightness(pixel):
    # Перевіряємо, чи є альфа-канал у пікселя
    if len(pixel) == 4:
        # Якщо є, перевіряємо, чи альфа-канал не рівний нулю
        if pixel[3] != 0:
            # Якщо альфа-канал не рівний нулю, враховуємо його для обчислення яскравості
            r, g, b, a = pixel
            return ((r * a) + (g * a) + (b * a)) / (255 * 3 * a)
        else:
            # Якщо альфа-канал рівний нулю, повертаємо 0 для уникнення помилки ділення на 0
            return 0
    else:
        # Якщо немає альфа-каналу, використовуємо тільки значення RGB для обчислення яскравості
        r, g, b = pixel
        return (r + g + b) / (255 * 3)

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
            # Визначення символу ASCII на основі яскравості кольору
            index = int(brightness(pixel) / 255 * (len(ASCII_CHARS)-1))
            # Використання символу ASCII та відповідного кольору
            if len(pixel) == 4:
                # Якщо є альфа-канал, використовуємо його для визначення кольору
                ascii_img += rgb_to_ansi(pixel[0], pixel[1], pixel[2]) + ASCII_CHARS[index]
            else:
                # Якщо немає альфа-каналу, використовуємо тільки значення RGB
                ascii_img += rgb_to_ansi(*pixel) + ASCII_CHARS[index]
        # Додамо символ переносу рядка лише після завершення кожного рядка символів
        ascii_img += "\033[0m\n"  
    
    print(ascii_img)

if __name__ == "__main__":
    image_path = input("Введіть шлях до зображення: ")
    main(image_path)
