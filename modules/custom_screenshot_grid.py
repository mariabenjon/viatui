from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
    image_path: Path to the image file.
    """
    return Image.open(image_path)

def draw_custom_grid(image, top_left, bottom_right, grid_size):
    """
    Draws a grid on the given image within specified coordinates.

    Args:
    image: PIL Image object
    top_left: Top left coordinate (x, y) of the grid area
    bottom_right: Bottom right coordinate (x, y) of the grid area
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    for x in range(top_left[0], bottom_right[0], grid_size):
        draw.line(((x, top_left[1]), (x, bottom_right[1])), fill=128)
    for y in range(top_left[1], bottom_right[1], grid_size):
        draw.line(((top_left[0], y), (bottom_right[0], y)), fill=128)
    del draw

def label_custom_vertices(image, top_left, bottom_right, grid_size):
    """
    Labels the vertices of the grid on the image within specified coordinates.

    Args:
    image: PIL Image object
    top_left: Top left coordinate (x, y) of the grid area
    bottom_right: Bottom right coordinate (x, y) of the grid area
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    for x in range(top_left[0], bottom_right[0], grid_size):
        for y in range(top_left[1], bottom_right[1], grid_size):
            label = f"({x},{y})"
            draw.text((x+5, y+5), label, fill="red", font=font)
    del draw

def create_image_with_custom_grid(image_path, top_left, bottom_right, grid_size):
    """
    Loads an image and creates a custom grid with labeled vertices.

    Args:
    image_path: Path to the image file
    top_left: Top left coordinate (x, y) of the grid area
    bottom_right: Bottom right coordinate (x, y) of the grid area
    grid_size: Size of the grid cells
    """
    image = load_image(image_path)
    draw_custom_grid(image, top_left, bottom_right, grid_size)
    label_custom_vertices(image, top_left, bottom_right, grid_size)
    return image
