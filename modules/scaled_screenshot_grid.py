from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
    image_path: Path to the image file.
    """
    return Image.open(image_path)

def calculate_scale_factor(image, top_left, bottom_right):
    """
    Calculates the scale factor based on the image size and provided coordinates.

    Args:
    image: PIL Image object
    top_left: Top-left coordinates (x, y) in the larger grid
    bottom_right: Bottom-right coordinates (x, y) in the larger grid
    """
    width, height = image.size
    grid_width = bottom_right[0] - top_left[0]
    grid_height = bottom_right[1] - top_left[1]

    scale_factor_x = grid_width / width
    scale_factor_y = grid_height / height

    return scale_factor_x, scale_factor_y

def draw_scaled_grid(image, top_left, bottom_right, scale_factor_x, scale_factor_y, grid_size):
    """
    Draws a scaled grid on the image.

    Args:
    image: PIL Image object
    top_left: Top-left coordinates (x, y) in the larger grid
    bottom_right: Bottom-right coordinates (x, y) in the larger grid
    scale_factor_x: Horizontal scale factor
    scale_factor_y: Vertical scale factor
    grid_size: Size of the grid cells in the larger grid
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Draw scaled grid lines
    x = top_left[0]
    while x <= bottom_right[0]:
        scaled_x = int((x - top_left[0]) / scale_factor_x)
        if scaled_x < width:
            draw.line(((scaled_x, 0), (scaled_x, height)), fill=128)
        x += grid_size

    y = top_left[1]
    while y <= bottom_right[1]:
        scaled_y = int((y - top_left[1]) / scale_factor_y)
        if scaled_y < height:
            draw.line(((0, scaled_y), (width, scaled_y)), fill=128)
        y += grid_size

    del draw

def label_scaled_vertices(image, top_left, bottom_right, scale_factor_x, scale_factor_y, grid_size):
    """
    Labels the vertices of the scaled grid on the image.

    Args:
    image: PIL Image object
    top_left: Top-left coordinates (x, y) in the larger grid
    bottom_right: Bottom-right coordinates (x, y) in the larger grid
    scale_factor_x: Horizontal scale factor
    scale_factor_y: Vertical scale factor
    grid_size: Size of the grid cells in the larger grid
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.load_default()

    x = top_left[0]
    while x <= bottom_right[0]:
        scaled_x = int((x - top_left[0]) / scale_factor_x)
        y = top_left[1]
        while y <= bottom_right[1]:
            scaled_y = int((y - top_left[1]) / scale_factor_y)
            if scaled_x < width and scaled_y < height:
                label = f"({x},{y})"
                draw.text((scaled_x + 5, scaled_y + 5), label, fill="red", font=font)
            y += grid_size
        x += grid_size

    del draw

def create_scaled_grid_image(image_path, top_left, bottom_right, grid_size):
    """
    Creates an image with a scaled grid based on a specified region of a larger grid.

    Args:
    image_path: Path to the image file.
    top_left: Top-left coordinates (x, y) of the specified region in the larger grid.
    bottom_right: Bottom-right coordinates (x, y) of the specified region in the larger grid.
    grid_size: Size of the grid cells in the larger grid.
    """
    image = load_image(image_path)
    scale_factor_x, scale_factor_y = calculate_scale_factor(image, top_left, bottom_right)
    draw_scaled_grid(image, top_left, bottom_right, scale_factor_x, scale_factor_y, grid_size)
    label_scaled_vertices(image, top_left, bottom_right, scale_factor_x, scale_factor_y, grid_size)
    return image
