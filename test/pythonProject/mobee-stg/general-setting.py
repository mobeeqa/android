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
login = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Financial Freedom\nStarts Here\nLogin/Sign Up\nPhone Number")
login.click()

# Input phone number
phone = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
phone.click()
time.sleep(5)
TouchAction(driver).tap(None, 408, 1875,1).perform()
TouchAction(driver).tap(None, 147, 1610, 1).perform()
TouchAction(driver).tap(None, 676, 1886, 1).perform()
TouchAction(driver).tap(None, 408, 2025, 1).perform()
TouchAction(driver).tap(None, 404, 1746, 4).perform()
TouchAction(driver).tap(None, 147, 1610, 1).perform()
TouchAction(driver).tap(None, 408, 2025, 1).perform()
TouchAction(driver).tap(None, 147, 1610, 1).perform()
time.sleep(5)
# disappear keyboard on screen
driver.hide_keyboard()

time.sleep(3)
btn_next = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
btn_next.click()

# Input password
time.sleep(6)
password = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
password.click()
password.send_keys("Testing123")
time.sleep(7)
driver.hide_keyboard()
time.sleep(3)

btn_login = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log In")
btn_login.click()

# OTP Email
time.sleep(3)
otp = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Verify")
otp.click()
 
# Choose one to un/command for using biometrics
bio = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Not Now")
bio.click()
# el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Enable Biometrics")
# el9.click()
time.sleep(5)

#Profile page
# profile_button = driver.find_element_by_android_uiautomator(
#     'new UiSelector().description("Settings")'
# )
profile_button = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.ImageView")
profile_button.click()
TouchAction(driver).tap(None, 996, 175,1).perform()
time.sleep(5)

setting  = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Settings")
setting.click()
time.sleep(5)

# Choose one to switch language 
lang = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Language\nEnglish")
lang.click()
time.sleep(3)
IND = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Bahasa Indonesia")
IND.click()
time.sleep(3)

# el4 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
# el4.click()
# el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Default Mata Uang\nIDR")
# el5.click()
# el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="USD")
# el6.click()
# el7 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
# el7.click()


driver.quit()