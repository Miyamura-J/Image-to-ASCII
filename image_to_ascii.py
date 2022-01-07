from PIL import Image

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)

    resized_image = image.resize((new_width, new_height))

    return resized_image


def graying(resized_image):
    grayed_image = resized_image.convert("L")
    return grayed_image


def pixel_to_ascii(grayed_image):

    pixels = grayed_image.getdata()
    ascii_list = "".join(ascii_chars[pixel // 25] for pixel in pixels)

    return ascii_list


def ascii_to_image(ascii_list, new_width):
    pixel_num = len(ascii_list)

    finished_image = "\n".join(
        ascii_list[i : (i + new_width)] for i in range(0, pixel_num, new_width)
    )

    return finished_image


def main():
    path = input("Enter a path to an image:\n")
    new_width = int(input("Enter the wanted width:\n"))

    image = Image.open(path)

    finished_image = ascii_to_image(
        pixel_to_ascii(graying(resize(image, new_width))), new_width
    )
    print(finished_image)

    with open("ascii_image.txt", "w") as f:
        f.write(finished_image)


main()
