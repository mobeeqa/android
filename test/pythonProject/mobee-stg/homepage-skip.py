# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time


from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from appium.options.common import AppiumOptions

# For W3C actions

cap:Dict[str, Any]={
      "platformName": "Android",
      "appium:automationName": "UiAutomator2",
      "appium:app": "/Users/saharany/Documents/Mobee/app-staging-debug.apk",
      "appium:udid": "emulator-5554",
      "appium:appWaitActivity": "*",
      "appium:appGrantPermissions": "true",
      "appium:autoGrantPermissions": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
time.sleep(10)

#Launch the Mobee App
homepage = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Financial Freedom\nStarts Here\nLogin/Sign Up\nPhone Number")
homepage.click()
skip_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip")
skip_button.click()
time.sleep(5)
trade = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Trade\nTab 2 of 5")
trade.click()
time.sleep(5)


driver.quit()