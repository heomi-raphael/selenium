from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import pyautogui


options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url='https://www.jeongsancc.co.kr/login/login.do?redirect=/reservation/real_reservation.do?null')
driver.implicitly_wait(5)

driver.find_element_by_id('usrId').send_keys('125860')
driver.find_element_by_id('usrPwd').send_keys('p6120306j@')
driver.find_element_by_xpath('//*[@id="login"]/div[1]/a').click()

pyautogui.press('enter')



check = driver.find_elements_by_partial_link_text('14')
driver.find_element_by_xpath("//*[@title='마감되었습니다.']").click()
driver.implicitly_wait(5)


#sample = driver.find_elements_by_xpath("//*[@id='timeresbtn_3_0700']")
#sample.click()


#driver.execute_script("arguments[0].click()", sample)


#.find_element_by_xpath("//a[@title='예약가능']") // [@test='26']

sleep(3)
driver.close()