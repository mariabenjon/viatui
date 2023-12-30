from PIL import Image

def zoom_image(image_path, output_path, top_left, bottom_right):
    """
    Zooms into a region of an image.

    :param image_path: Path to the input image.
    :param output_path: Path to save the zoomed image.
    :param top_left: Tuple (x,y) of the top left corner of the zoom region.
    :param bottom_right: Tuple (x,y) of the bottom right corner of the zoom region.
    """
    try:
        # Open an image file
        with Image.open(image_path) as img:
            original_size = img.size
            # Crop the image to the specified region
            cropped_img = img.crop((*top_left, *bottom_right))

            # Resize cropped image to original dimensions
            resized_img = cropped_img.resize(original_size, Image.ANTIALIAS)

            # Save the cropped image
            resized_img.save(output_path)
            print(f"Zoomed and resized image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")