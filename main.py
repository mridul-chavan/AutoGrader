from functools import total_ordering
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://iu.instructure.com/courses/1906966/gradebook/speed_grader?assignment_id=***&student_id=**")
user_name = driver.find_element_by_name("j_username")
user_name.clear()
user_name.send_keys("***********")
pass_phrase = driver.find_element_by_name("j_password")
pass_phrase.send_keys("*************")
login_button = driver.find_element_by_name("_eventId_proceed")
login_button.click()
driver.set_page_load_timeout(5)
driver.switch_to_frame("duo_iframe")
Push_notif = driver.find_element_by_xpath("//*[@id='auth_methods']/fieldset/div[1]/button")
Push_notif.click()
time.sleep(15)
Comments = driver.find_elements_by_xpath("//*[@id='comments']//div[1]/span")
