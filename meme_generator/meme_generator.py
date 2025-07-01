from PIL import Image, ImageDraw, ImageFont
import os

def create_meme(image_path, top_text, bottom_text, output_path="meme.png"):
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        width, height = img.size

        # Try to load a common font, or use default
        try:
            font = ImageFont.truetype("arial.ttf", 40) # Adjust font size as needed
        except IOError:
            font = ImageFont.load_default()
            print("Warning: arial.ttf not found, using default font.")

        # Calculate text size and position
        # Top text
        text_width, text_height = draw.textsize(top_text, font)
        text_x = (width - text_width) / 2
        text_y = 10
        draw.text((text_x, text_y), top_text, font=font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

        # Bottom text
        text_width, text_height = draw.textsize(bottom_text, font)
        text_x = (width - text_width) / 2
        text_y = height - text_height - 10
        draw.text((text_x, text_y), bottom_text, font=font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

        img.save(output_path)
        print(f"Meme created and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("--- Simple CLI Meme Generator (requires Pillow: pip install Pillow) ---")
    print("Usage: python meme_generator.py <image_path> \"Top Text\" \"Bottom Text\" [output_path]")
    print("Example: python meme_generator.py my_image.jpg \"One does not simply\" \"Make a meme\"")

    # Create a dummy image for testing if none is provided
    if not os.path.exists("sample_image.jpg"):
        try:
            img = Image.new('RGB', (600, 400), color = 'gray')
            draw = ImageDraw.Draw(img)
            draw.text((200, 180), "Sample Image", fill=(0,0,0))
            img.save("sample_image.jpg")
            print("Created sample_image.jpg for testing.")
        except Exception as e:
            print(f"Could not create sample_image.jpg: {e}")

    # Example usage (uncomment and modify to run)
    # create_meme("sample_image.jpg", "Hello", "World", "my_first_meme.png")
