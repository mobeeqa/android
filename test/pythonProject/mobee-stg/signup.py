# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction

# For W3C actions

cap:Dict[str, Any]={
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:app": "/Users/saharany/Downloads/app-staging-debug.apk",
    "appium:udid": "emulator-5554",
    "appium:appWaitActivity": "*",
    "appium:appGrantPermissions": "true",
    "appium:autoGrantPermissions": "true",
    "appium:connectHardwareKeyboard": "true",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))

# Launch the Mobee App
time.sleep(10)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Financial Freedom\nStarts Here\nLogin/Sign Up\nPhone Number")
el1.click()

# Input phone number
el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el2.click()
time.sleep(5)
TouchAction(driver).tap(None, 408, 1875,1).perform() 
TouchAction(driver).tap(None, 147, 1610, 1).perform() 
TouchAction(driver).tap(None, 412, 1606, 1).perform() 
TouchAction(driver).tap(None, 408, 1875, 1).perform() 
TouchAction(driver).tap(None, 145, 1869, 1).perform() 
TouchAction(driver).tap(None, 675, 1751, 1).perform() 
TouchAction(driver).tap(None, 412, 1606, 1).perform() 
TouchAction(driver).tap(None, 675, 1751, 1).perform() 
TouchAction(driver).tap(None, 412, 1739, 1).perform()
time.sleep(5)
# disappear keyboard on screen
driver.hideKeyboard()

time.sleep(3)
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
el4.click()

# Input password
# time.sleep(5)
# el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
# el5.click()
# el5.send_keys("Testing123")
# driver.hideKeyboard()
# time.sleep(3)
# el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log In")
# el7.click()

# # OTP Email
# time.sleep(3)
# el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Verify")
# el8.click()
 
# # Choose one to un/command for using biometrics
# el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Not Now")
# el9.click()
# # el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Enable Biometrics")
# # el9.click()

driver.quit()