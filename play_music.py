import time
import datetime
from selenium import webdriver


set_hours = int(input('Set start hours (0-23): '))
set_minutes = int(input('Set start minutes (0-59): '))

while True:
    now_time = datetime.datetime.now()
    hours = now_time.hour
    minutes = now_time.minute
    
    if hours == set_hours and minutes == set_minutes:
        driver = webdriver.Chrome()
        driver.get("https://www.internet-radio.com/stations/soundtracks/")
        elem = driver.find_element_by_xpath("//*[@id='jp_container_3']/div[1]/div/div/i[1]")
        elem.click()
        break

    time.sleep(1)