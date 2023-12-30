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
            # Crop the image to the specified region
            cropped_img = img.crop((*top_left, *bottom_right))

            # Save the cropped image
            cropped_img.save(output_path)
            print(f"Zoomed image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")