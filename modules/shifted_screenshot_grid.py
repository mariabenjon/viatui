from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
    image_path: Path to the image file.
    """
    return Image.open(image_path)

def draw_shifted_grid(image, origin, grid_size):
    """
    Draws a grid on the image as if it's part of a larger grid, with the given origin.

    Args:
    image: PIL Image object
    origin: Origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size
    start_x, start_y = origin

    # Adjust start point for the grid
    for x in range(-start_x % grid_size, width, grid_size):
        draw.line(((x, 0), (x, height)), fill=128)
    for y in range(-start_y % grid_size, height, grid_size):
        draw.line(((0, y), (width, y)), fill=128)

    del draw

def label_shifted_grid_vertices(image, origin, grid_size):
    """
    Labels the vertices of the shifted grid on the image.

    Args:
    image: PIL Image object
    origin: Origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    width, height = image.size
    start_x, start_y = origin

    for x in range(-start_x % grid_size, width, grid_size):
        for y in range(-start_y % grid_size, height, grid_size):
            grid_x = x + start_x - (-start_x % grid_size)
            grid_y = y + start_y - (-start_y % grid_size)
            label = f"({grid_x},{grid_y})"
            draw.text((x + 5, y + 5), label, fill="red", font=font)

    del draw

def create_image_with_shifted_grid(image_path, origin, grid_size):
    """
    Loads an image and creates a shifted grid with labeled vertices.

    Args:
    image_path: Path to the image file
    origin: Origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    image = load_image(image_path)
    draw_shifted_grid(image, origin, grid_size)
    label_shifted_grid_vertices(image, origin, grid_size)
    return image
