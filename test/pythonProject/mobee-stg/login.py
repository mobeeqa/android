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
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
time.sleep(10)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Financial Freedom\nStarts Here\nLogin/Sign Up\nPhone Number")
el1.click()
el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el2.click()
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
driver.hideKeyboard()
# el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login/Sign Up\nPhone Number")
# el3.click()
time.sleep(3)
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
el4.click()
time.sleep(5)
el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el5.click()
el5.send_keys("Testing123")
driver.hideKeyboard()
# el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView")
# el6.click()
time.sleep(3)
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log In")
el7.click()
time.sleep(3)
el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Verify")
el8.click()
el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Not Now")
el9.click()
# el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Enable Biometrics")
# el9.click()

# driver.quit()