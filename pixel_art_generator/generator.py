from PIL import Image
import random

def image_to_pixel_art(image_path, pixel_size, output_path="pixel_art.png"):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    img = img.resize((img.size[0] // pixel_size, img.size[1] // pixel_size), Image.NEAREST)
    img = img.resize((img.size[0] * pixel_size, img.size[1] * pixel_size), Image.NEAREST)
    img.save(output_path)
    print(f"Pixel art saved to {output_path}")

def generate_random_pixel_art(width, height, pixel_size, output_path="random_pixel_art.png"):
    img = Image.new('RGB', (width // pixel_size, height // pixel_size))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    img = img.resize((width, height), Image.NEAREST)
    img.save(output_path)
    print(f"Random pixel art saved to {output_path}")

if __name__ == "__main__":
    # Example: Convert an image to pixel art
    # You'll need a sample image file (e.g., 'sample.png') in the same directory
    # image_to_pixel_art("sample.png", pixel_size=10, output_path="sample_pixelated.png")

    # Example: Generate random pixel art
    generate_random_pixel_art(width=200, height=200, pixel_size=10, output_path="random_art.png")
