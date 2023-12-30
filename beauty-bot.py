import time
import random
import subprocess
import logging
from datetime import datetime, time as dtime
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set up logging with detailed timestamp
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def is_sleep_time():
    """Check if current time is within sleeping hours."""
    start_sleep = dtime(23, 0)  # 11:00 PM
    end_sleep = dtime(7, 0)     # 7:00 AM
    current_time = datetime.now().time()

    if start_sleep < end_sleep:
        # Normal scenario: Sleeping time does not cross midnight
        return start_sleep <= current_time <= end_sleep
    else:
        # Crossover scenario: Sleeping time crosses midnight
        return current_time >= start_sleep or current_time <= end_sleep

def run_command():
    """Your command to run."""
    command = "docker-compose run -d viatui bash -c 'sleep 20 && /root/.local/bin/poetry run python scripts/share.py'"
    logging.info(f"Sharing your beautiful things\n  {command}\n  Check viatui/chromium-nix-screenshots for progress")
    subprocess.run(command, shell=True)

def main():
    flower_ascii = """
         #       #       #
         #       #       #
         ##     ###     ##
         ###   #####   ###
         #### ####### ####
         #################
         #################
          ###############
            ###########
              #######
                ***
                ***
                ***      ***
                ***   *********
                *****************
                ***   *********
                ***      ***
                ***
   ******      ***
************* ***
   ******    ***
            ***
           ***
          ***
         ***
        ***
       ***
      ***
     ***
    ***
     *
"""
    # Split the ASCII art into lines
    lines = flower_ascii.strip().split('\n')

    # Loop through each line and print it, then wait for a few milliseconds
    first_line = True
    for line in lines:
        # skip and repeat first line due to format issues
        if first_line is not True:
            print(line)
        first_line = False
        time.sleep(0.1)  # Waits for 100 milliseconds. Adjust this value as needed.

    sentence1 = get_from_viatuix_config('viatuix.json', 'sentence1')
    print(sentence1)
    while True:
        if not is_sleep_time():
            run_command()

            # Wait for 10 minutes +/- some random seconds
            wait_time = 600 + random.randint(-60, 60)  # 10 minutes ± 1 minute
            logging.info(f"Sleeping for {wait_time/60} minutes.")
            time.sleep(wait_time)
        else:
            # Sleeping hours
            logging.info("Currently within sleeping hours. Next check in 3 minutes.")
            time.sleep(180)  # Check every 3 minutes

if __name__ == "__main__":
    main()
