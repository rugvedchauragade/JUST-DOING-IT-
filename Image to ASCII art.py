from PIL import Image, ImageOps

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def resize_image(image, new_width=150):
    width, height = image.size
    ratio = height / width / 1.9  # tweak between 1.8-2.2 if stretched/squished
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayscale(image):
    image = image.convert("L")
    return ImageOps.autocontrast(image)  # stretches brightness range for more contrast

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join(ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels)

def main():
    path = input("Enter image path: ").strip().strip('"').strip("'")

    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Error: {e}")
        return

    image = resize_image(image)
    image = grayscale(image)

    ascii_str = pixels_to_ascii(image)
    width = image.width

    ascii_art = "\n".join(
        ascii_str[i:i + width] for i in range(0, len(ascii_str), width)
    )

    print(ascii_art)

    with open("ascii_output.txt", "w") as f:
        f.write(ascii_art)
    print("\n✓ Saved as ascii_output.txt")

if __name__ == "__main__":
    main()