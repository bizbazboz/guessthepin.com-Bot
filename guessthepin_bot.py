from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import discord

def message(message):
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        user = client.get_user(1234567890) # Place your discord ID here
        await user.send(message)
    client.run("")

def main(lower,upper):
    pin_field = "/html/body/div[2]/form/input[1]"
    submit_button = "/html/body/div[2]/form/input[2]"


    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    options = Options()
    options.binary = binary
    cap = DesiredCapabilities().FIREFOX
    driver = webdriver.Firefox(options=options, capabilities=cap, executable_path="geckodriver.exe path")
    driver.get('https://www.guessthepin.com/')

    for code in range(lower,upper):
        wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, pin_field)))
        code_input = driver.find_element_by_xpath(pin_field)
        code_input.send_keys(str(code).zfill(4))
        time.sleep(1)
        guess_button = driver.find_element_by_xpath(submit_button)
        guess_button.click()
    message(f"{lower} to {upper} has run succesfully!")
    driver.quit()
   

try:
    print("Running program now...")
    threading.Thread(target=main, args=(0,2000)).start()
    threading.Thread(target=main, args=(2000,4000)).start()
    threading.Thread(target=main, args=(4000,6000)).start()
    threading.Thread(target=main, args=(6000,8000)).start()
    threading.Thread(target=main, args=(8000,10000)).start()
    print("Has run successfully!")
    message("Has started successfully!")
except:
    print("Error has occured, please restart")
    message("Error has occured, please restart")
