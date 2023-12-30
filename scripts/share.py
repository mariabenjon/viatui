import pyautogui
import time
import os
from datetime import datetime
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config
from modules.find_text_coordinates import find_text_coordinates

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Make a new browser tab
  pyautogui.hotkey('ctrl', 't')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-1.png')

  # Type in url.
  login_page = get_from_viatuix_config('viatuix.json', 'url2')
  pyautogui.moveTo(200, 75)
  pyautogui.click()
  pyautogui.typewrite(login_page)
  time.sleep(2)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-2.png')

  # Type in username
  username = get_from_viatuix_config('viatuix.json', 'username')
  pyautogui.moveTo(300, 550)
  pyautogui.click()
  pyautogui.typewrite(username)
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-3.png')

  # Type in password
  password = get_from_viatuix_config('viatuix.json', 'password')
  pyautogui.moveTo(300, 600)
  pyautogui.click()
  pyautogui.typewrite(password)
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-4.png')

  # Submit username and password
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-5.png')

  # Don't save password, click 'Never'.
  pyautogui.moveTo(700, 400)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-6.png')

  # Type in other url.
  other_page = get_from_viatuix_config('viatuix.json', 'url3')
  pyautogui.moveTo(200, 75)
  pyautogui.click()
  pyautogui.typewrite(other_page)
  time.sleep(2)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-7.png')

  # Click on your closet
  # Change from 525 to 576 on y due to banner change.
  pyautogui.moveTo(850, 575)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-8.png')

  # Create a no grid image to find coordinates of text using ocr
  find_text_screenshot = 'chromium-nix-screenshots/find-text.png'
  print(find_text_screenshot)
  screenshot_no_grid = create_screenshot_with_grid(1000)
  screenshot_no_grid.save(find_text_screenshot)
  time.sleep(2)

  target_text = 'Followers'
  (target_x, target_y) = find_text_coordinates(find_text_screenshot, target_text)

  if (target_x, target_y):
      print(f"Doing ocr.\nCoordinates of '{target_text}': {target_x} {target_y}")
      # Share to followers button
      pyautogui.moveTo(target_x, target_y)
      pyautogui.click()
      print(f"Clicked coordinates ({target_x}, {target_y}).")
      time.sleep(5)
      screenshot = create_screenshot_with_grid(100)
      screenshot.save('chromium-nix-screenshots/posh-9.png')
      print(f"See screenshot chromium-nix-screenshots/posh-9.png")
  else:
      print(f"Ocr step failed. No '{target_text}' not found in the image\nreverting to hardcoded coordinates.")
      # Share to followers button
      pyautogui.moveTo(800, 450)
      pyautogui.click()
      time.sleep(5)
      screenshot = create_screenshot_with_grid(100)
      screenshot.save('chromium-nix-screenshots/posh-9.png')

  # Share all
  pyautogui.moveTo(375, 375)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-10.png')

  # Share to followers
  pyautogui.moveTo(900, 290)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-11.png')

  # Format the date and time as a string in the format "yyyy-mm-dd-h-m"
  # Get the current date and time
  current_datetime = datetime.now()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")

  # Monitor progress
  time.sleep(10)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save(f"chromium-nix-screenshots/posh-{formatted_datetime}.png")

  # Wait until likely finished
  time.sleep(20)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save(f"chromium-nix-screenshots/posh-{formatted_datetime}.png")

