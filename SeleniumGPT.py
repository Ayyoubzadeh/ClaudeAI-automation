# !pip install selenium
# !pip install requests

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests



#extension_path = BASE_PATH+'Adblocker_5_8_1_0.crx'
chrome_driver_path = 'chromedriver.exe'
service = Service(chrome_driver_path)
chrome_options = [Options(),Options()]
#chrome_options.add_extension(extension_path)
for i in range(len(chrome_options)):
    chrome_options[i].add_argument("--incognito")
    #chrome_options[i].add_argument("--new-window")
    #chrome_options[i].add_argument("user-data-dir="+BASE_PATH+"profile"+str(i))
    #chrome_options[i].add_argument("--disable-cookies")

drivers=[]
waits=[]

def init():
    global drivers,waits
    drivers=[webdriver.Chrome(service=service,options=chrome_options[0]),
             webdriver.Chrome(service=service,options=chrome_options[1])]
    waits=[WebDriverWait(drivers[0], 60),WebDriverWait(drivers[1],60)]
    
        
def restartDriver(i):
    global drivers,waits
    drivers[i].close()
    drivers[i]=webdriver.Chrome(service=service,options=chrome_options[i])
    waits[i]=WebDriverWait(drivers[i], 60)
    
def getElement(xpath,driverIndex=0):
    waits[driverIndex].until(EC.visibility_of_element_located((By.XPATH,xpath)))
    return drivers[driverIndex].find_element(By.XPATH,xpath)
def Type(xpath,text,driverIndex=0):
    element = getElement(xpath,driverIndex)
    element.send_keys(text)
    time.sleep(1)
    element.send_keys(Keys.RETURN)
def getTextFromFirstElement(xpath,driverIndex=0):
    waits[driverIndex].until(EC.visibility_of_element_located((By.XPATH,xpath)))
    elements = drivers[driverIndex].find_elements(By.XPATH,xpath)
    return elements[0].text
def getValueFromFirstElement(xpath,driverIndex=0):
    waits[driverIndex].until(EC.visibility_of_element_located((By.XPATH,xpath)))
    elements = drivers[driverIndex].find_elements(By.XPATH,xpath)
    return elements[0].get_attribute("value")
def getText(xpath,driverIndex=0):
    element = getElement(xpath,driverIndex)
    return element.text
def getValue(xpath,driverIndex=0):
    element = getElement(xpath,driverIndex)
    return element.get_attribute("value")
def Click(xpath,driverIndex=0):
    element = getElement(xpath,driverIndex)
    element.click()
    time.sleep(1)
def Enter(xpath,driverIndex=0):
    element = getElement(xpath,driverIndex)
    element.send_keys(Keys.RETURN)
    time.sleep(1)
def Wait(xpath,driverIndex=0):
    waits[driverIndex].until(EC.visibility_of_element_located((By.XPATH,xpath)))

def getEmailAddress():
    drivers[1].get('https://tempmailo.com/')
    time.sleep(3)
    email=getValue("//input[@id='i-email']",1)
    print(email)
    return email
    
def ClaudeAILogin():
    global email
    try:
        drivers[0].get('https://claude.ai/login')
        Type("//*[@id='email']",getEmailAddress())
        Click("//span[text()='Refresh']",1)
        code=getTextFromFirstElement("//div[contains(text(), 'Your verification code is ')]",1).replace('Your verification code is ','')
        Type("//*[@id='code']",code)
        Type("//*[@id='fullname']",'Researcher')
        Click("//*[@id=':r1:']")
        Click("//*[@id=':r2:']")
        Enter("//button[contains(text(), 'Continue')]")
        Enter("//button[contains(text(), 'Next')]")
        Enter("//button[contains(text(), 'Next')]")
        Enter("//button[contains(text(), 'Next')]")
        Enter("//button[contains(text(), 'Finish')]")
    except Exception as e:
        print("An error occurred:", e)
        return -1
def extractDataFromCaludeAI(prompt):
    try:
        drivers[0].get('https://claude.ai/chats')
        Wait("//div[@contenteditable='true']")
        Type("//div[@contenteditable='true']",prompt.replace('\n',' ')+" don't write anything else result in the output. The output should start with ---RESPONSE--- keyword")
        Wait("//button[contains(text(), 'Copy')]")
        result=getText("//*[starts-with(text(), '---RESPONSE---')]").replace('---RESPONSE---','')
        print(result)
        return result
    except Exception as e:
        print("An error occurred:", e)
        return 'ERR'



prompt='please answer 2+17'
init()
ClaudeAILogin()
while extractDataFromCaludeAI(prompt)=='ERR':
    restartDriver(0)
    restartDriver(1)
    ClaudeAILogin()   
        
