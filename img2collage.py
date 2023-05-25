from PIL import Image
import os

# Function to resize images while maintaining aspect ratio
def resize_image(image, target_size):
    image.thumbnail(target_size, Image.ANTIALIAS)
    return image

# Function to create a black square image with specified dimensions
def create_black_image(width, height):
    black_image = Image.new("RGB", (width, height), (0, 0, 0))
    return black_image

# Function to create the collage
def create_collage(images):
    # Create a blank canvas for the collage
    collage_width = 2 * image_size[0] if len(images) > 1 else image_size[0]
    collage_height = 2 * image_size[1] if len(images) > 2 else image_size[1]
    collage = create_black_image(collage_width, collage_height)

    # Paste images into the collage
    if len(images) >= 1:
        collage.paste(resize_image(images[0], image_size), (0, 0))
    if len(images) >= 2:
        collage.paste(resize_image(images[1], image_size), (image_size[0], 0))
    if len(images) >= 3:
        collage.paste(resize_image(images[2], image_size), (0, image_size[1]))
    if len(images) >= 4:
        collage.paste(resize_image(images[3], image_size), (image_size[0], image_size[1]))

    # Create the "output" directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Save the collage as PNG in the "output" directory
    collage_path = os.path.join("output", "collage.png")
    collage.save(collage_path, "PNG")
    print("Collage saved successfully!")

# Prompt the user to provide image paths
image_paths = []
while len(image_paths) < 4:
    image_path = input("Enter image path (leave blank to finish): ")
    if image_path == "":
        break
    image_paths.append(image_path)

# Load the images
images = []
for image_path in image_paths:
    image = Image.open(image_path)
    images.append(image)

# Determine the size of the images
image_size = images[0].size

# Fill in any missing images with black squares
while len(images) < 4:
    images.append(create_black_image(*image_size))

# Create the collage
create_collage(images)
