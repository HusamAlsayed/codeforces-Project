from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Mohmal:
  def __init__(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver',options=chrome_options)
    driver.get("https://www.mohmal.com/")
    self.driver = driver

  def refresh_page(self):
    refresh_button = self.driver.find_element_by_id('refresh')
    refresh_button.click()
  
  def get_email(self):
    element = self.driver.find_element_by_id('rand')
    element.click()
    time.sleep(2)
    new_element = self.driver.find_element_by_id('email')
    new_element = new_element.find_elements_by_class_name('email')
    return new_element[0].text

  def get_unseen_messages(self):
    unseen_table = self.driver.find_elements_by_class_name('unseen')
    return unseen_table

  def switch_to_content(self,unseen_data,message_id):
    unseen_data[message_id].click()
    time.sleep(5)
    self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

  


  
