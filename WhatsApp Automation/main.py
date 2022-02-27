from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time
driver.get("https://web.whatsapp.com/")

input("please scan QR code and press any key to continue: ")

T = driver.find_element_by_css_selector('span[title="Test"]')
T.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
time.sleep(12)
testinput.send_keys("HELLO")
testinput.send_keys(Keys.RETURN)