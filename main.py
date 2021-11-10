from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://login.live.com")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="i0116"]').send_keys("billgates@outlook.com")
browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="i0118"]').send_keys("Micro$oft")
browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()