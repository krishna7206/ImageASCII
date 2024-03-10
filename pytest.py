from PIL import Image

# Open the image file
image_path = '/home/knambiar41/workspace/image.jpeg'
image = Image.open(image_path)

# Define ASCII characters to represent different shades of gray
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Resize the image to reduce the number of pixels
width, height = image.size
aspect_ratio = height / width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.5)
resized_image = image.resize((new_width, new_height))

# Convert the image to grayscale
grayscale_image = resized_image.convert('L')

# Convert each pixel to an ASCII character
pixels = grayscale_image.getdata()
ascii_str = ''
for pixel_value in pixels:
    ascii_str += ASCII_CHARS[pixel_value // 25]

# Print the ASCII art
for i in range(0, len(ascii_str), new_width):
    print(ascii_str[i:i+new_width])

# Save ASCII art to a file
with open('ascii_art.txt', 'w') as f:
    for i in range(0, len(ascii_str), new_width):
        f.write(ascii_str[i:i+new_width] + '\n')