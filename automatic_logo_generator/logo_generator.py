from PIL import Image, ImageDraw, ImageFont

def generate_simple_logo(company_name, slogan="", output_path="logo.png", 
                         bg_color=(70, 130, 180), text_color=(255, 255, 255),
                         font_size_name=60, font_size_slogan=30):
    
    img_width = 800
    img_height = 400
    img = Image.new('RGB', (img_width, img_height), color = bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font_name = ImageFont.truetype("arial.ttf", font_size_name)
        font_slogan = ImageFont.truetype("arial.ttf", font_size_slogan)
    except IOError:
        font_name = ImageFont.load_default()
        font_slogan = ImageFont.load_default()
        print("Warning: arial.ttf not found, using default font.")

    # Draw company name
    text_width, text_height = draw.textsize(company_name, font_name)
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2 - (font_size_slogan / 2) # Adjust for slogan
    draw.text((text_x, text_y), company_name, font=font_name, fill=text_color)

    # Draw slogan if provided
    if slogan:
        slogan_width, slogan_height = draw.textsize(slogan, font_slogan)
        slogan_x = (img_width - slogan_width) / 2
        slogan_y = text_y + text_height + 10 # Below company name
        draw.text((slogan_x, slogan_y), slogan, font=font_slogan, fill=text_color)

    img.save(output_path)
    print(f"Logo generated and saved to {output_path}")

if __name__ == "__main__":
    print("--- Simple CLI Automatic Logo Generator (requires Pillow: pip install Pillow) ---")
    print("This script generates a simple logo with company name and slogan.")
    print("Example: generate_simple_logo(\"My Company\", \"Innovating the Future\")")

    # Example usage
    generate_simple_logo("Tech Solutions", "Your Partner in Innovation", "tech_logo.png")
    generate_simple_logo("Green Earth", "Sustainable Living", "green_logo.png", bg_color=(60, 179, 113))
