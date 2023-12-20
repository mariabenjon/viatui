import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  ## Make a new browser tab
  #pyautogui.hotkey('ctrl', 't')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-1.png')

  ## Type in github url into bar
  #login_page = get_from_viatuix_config('viatuix.json', 'url2')
  #pyautogui.moveTo(200, 75)
  #pyautogui.click()
  #pyautogui.typewrite(login_page)
  #time.sleep(2)
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-2.png')

  ## Type in username
  #username = get_from_viatuix_config('viatuix.json', 'username')
  #pyautogui.moveTo(300, 550)
  #pyautogui.click()
  #pyautogui.typewrite(username)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-3.png')

  ## Type in password
  #password = get_from_viatuix_config('viatuix.json', 'password')
  #pyautogui.moveTo(300, 600)
  #pyautogui.click()
  #pyautogui.typewrite(password)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-4.png')

  ## Submit username and password
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-5.png')

  ## Don't save password
  #pyautogui.press('esc')
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-6.png')

  #pyautogui.moveTo(700, 400)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-7.png')

  ## Click on your account icon
  #pyautogui.moveTo(950, 150)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-8.png')

  ## Click on your closet
  #pyautogui.moveTo(800, 200)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-9.png')

  ## Click on your closet
  #pyautogui.moveTo(850, 525)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-10.png')

  ## Share to followers button
  #pyautogui.moveTo(800, 400)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-11.png')

  ## Share all
  #pyautogui.moveTo(375, 375)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/posh-12.png')

  # Share to followers
  pyautogui.moveTo(900, 290)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/posh-13.png')
