from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
    image_path: Path to the image file.
    """
    return Image.open(image_path)

def draw_extended_grid(image, top_left, bottom_right, grid_size):
    """
    Draws a grid on the given image, assuming the image is part of a larger grid.

    Args:
    image: PIL Image object
    top_left: Top left coordinate (x, y) of the assumed larger grid
    bottom_right: Bottom right coordinate (x, y) of the assumed larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size
    start_x, start_y = top_left
    end_x, end_y = bottom_right

    # Adjust start and end points for the lines
    for x in range(start_x, end_x, grid_size):
        line_start_x = max(0, x - start_x)
        line_end_x = min(width, x - start_x)
        draw.line(((line_start_x, 0), (line_end_x, height)), fill=128)

    for y in range(start_y, end_y, grid_size):
        line_start_y = max(0, y - start_y)
        line_end_y = min(height, y - start_y)
        draw.line(((0, line_start_y), (width, line_end_y)), fill=128)

    del draw

def label_extended_grid_vertices(image, top_left, bottom_right, grid_size):
    """
    Labels the vertices of the extended grid on the image.

    Args:
    image: PIL Image object
    top_left: Top left coordinate (x, y) of the assumed larger grid
    bottom_right: Bottom right coordinate (x, y) of the assumed larger grid
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    width, height = image.size
    start_x, start_y = top_left

    for x in range(start_x, bottom_right[0], grid_size):
        for y in range(start_y, bottom_right[1], grid_size):
            grid_x = x - start_x
            grid_y = y - start_y
            if 0 <= grid_x < width and 0 <= grid_y < height:
                label = f"({x},{y})"
                draw.text((grid_x + 5, grid_y + 5), label, fill="red", font=font)

    del draw

def create_image_with_extended_grid(image_path, top_left, bottom_right, grid_size):
    """
    Loads an image and creates an extended grid with labeled vertices.

    Args:
    image_path: Path to the image file
    top_left: Top left coordinate (x, y) of the assumed larger grid
    bottom_right: Bottom right coordinate (x, y) of the assumed larger grid
    grid_size: Size of the grid cells
    """
    image = load_image(image_path)
    draw_extended_grid(image, top_left, bottom_right, grid_size)
    label_extended_grid_vertices(image, top_left, bottom_right, grid_size)
    return image
