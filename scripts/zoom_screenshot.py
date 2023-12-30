import pyautogui
import time
import os
import argparse
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.custom_screenshot_grid import create_image_with_custom_grid
from modules.get_from_viatuix_config import get_from_viatuix_config
from modules.zoom_image import zoom_image

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

# Initialize parser
parser = argparse.ArgumentParser(description='Take a screenshot and save it with a given filename.')
# Adding argument
parser.add_argument('filename', type=str, help='Filename to save the screenshot')
# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    dir = 'chromium-nix-screenshots'
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(3)
    screenshot = create_screenshot()
    screenshot_with_grid = create_screenshot_with_grid(100)
    # Use the filename from the command line argument
    filename = os.path.join(dir, args.filename)
    grid_filename = os.path.join(dir, "grid_" + args.filename)
    zoomed_filename = os.path.join(dir, "zoomed_" + args.filename)
    zoomed_with_grid_filename = os.path.join(dir, "zoomed_with_grid" + args.filename)
    screenshot.save(filename)
    screenshot_with_grid.save(grid_filename)

    zoom_image(filename, zoomed_filename, (500, 100), (700, 300))

    screenshot_zoomed_with_grid = create_image_with_custom_grid(filename, (500, 100), (700, 300), 100)

    screenshot_zoomed_with_grid.save(zoomed_with_grid_filename)