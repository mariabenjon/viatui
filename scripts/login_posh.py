import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Make a new browser tab
  pyautogui.hotkey('ctrl', 't')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-1.png')

  # Type in github url into bar
  login_page = get_from_viatuix_config('viatuix.json', 'url2')
  pyautogui.moveTo(200, 75)
  pyautogui.click()
  pyautogui.typewrite(login_page)
  time.sleep(2)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-2.png')

  ## Type in username
  #username = get_from_viatuix_config('viatuix.json', 'username')
  #pyautogui.moveTo(414, 353)
  #pyautogui.click()
  #pyautogui.typewrite(username)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-3.png')

  ## Type in password
  #password = get_from_viatuix_config('viatuix.json', 'password')
  #pyautogui.moveTo(423, 425)
  #pyautogui.click()
  #pyautogui.typewrite(password)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-4.png')

  ## Submit username and password
  #pyautogui.moveTo(502, 477)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-5.png')

  ## Don't save password
  #pyautogui.moveTo(700, 400)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-6.png')
