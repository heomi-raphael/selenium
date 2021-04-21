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
driver.implicitly_wait(5)


datain = '29'#// 이후 input 사용하기 
#datec = '{}'.format(datain) // 인풋 사용후 사용 

driver.find_element_by_xpath("//*[@title='예약가능'][contains(text(),"+ datain +")]").click()
driver.implicitly_wait(5)

times = "0708" #// 이후 input 사용하기 

driver.find_element_by_xpath("//*[@id='timeresbtn_1_"+ times +"']").click()

sleep(10)
driver.close()