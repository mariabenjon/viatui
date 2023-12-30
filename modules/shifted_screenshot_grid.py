from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
    image_path: Path to the image file.
    """
    return Image.open(image_path)

def draw_shifted_grid(image, external_origin, grid_size):
    """
    Draws a grid on the image as if it's part of a larger grid, with the external origin.

    Args:
    image: PIL Image object
    external_origin: External origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size
    origin_x, origin_y = external_origin

    # Draw grid lines based on the external origin
    x = -origin_x % grid_size
    while x < width:
        draw.line(((x, 0), (x, height)), fill=128)
        x += grid_size

    y = -origin_y % grid_size
    while y < height:
        draw.line(((0, y), (width, y)), fill=128)
        y += grid_size

    del draw

def label_shifted_grid_vertices(image, external_origin, grid_size):
    """
    Labels the vertices of the shifted grid on the image, relative to the external origin.

    Args:
    image: PIL Image object
    external_origin: External origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    width, height = image.size
    origin_x, origin_y = external_origin

    x = -origin_x % grid_size
    while x < width:
        y = -origin_y % grid_size
        while y < height:
            label_x = x + origin_x - (-origin_x % grid_size)
            label_y = y + origin_y - (-origin_y % grid_size)
            label = f"({label_x},{label_y})"
            draw.text((x + 5, y + 5), label, fill="red", font=font)
            y += grid_size
        x += grid_size

    del draw

def create_image_with_shifted_grid(image_path, external_origin, grid_size):
    """
    Loads an image and creates a shifted grid with labeled vertices, relative to an external origin.

    Args:
    image_path: Path to the image file
    external_origin: External origin (x, y) of the larger grid
    grid_size: Size of the grid cells
    """
    image = load_image(image_path)
    draw_shifted_grid(image, external_origin, grid_size)
    label_shifted_grid_vertices(image, external_origin, grid_size)
    return image
