import cv2
import numpy as np

def main(image_path):
    # Завантаження зображення
    img = cv2.imread(image_path)

    # Конвертація зображення в чорно-білий та зменшення роздільної здатності
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img_gray.shape
    img_small = cv2.resize(img_gray, (width // 10, height // 10))

    # Створення потоку зелених символів
    symbols = "@%#*+=-:. "
    matrix = ""
    for row in img_small:
        for pixel in row:
            # Обчислення індексу символу залежно від інтенсивності пікселя
            index = int((255 - pixel) / 25)
            matrix += symbols[index]
        matrix += "\n"

    # Відображення результату
    print(matrix)

if __name__ == "__main__":
    image_path = input("Введіть шлях до зображення: ")
    main(image_path)
