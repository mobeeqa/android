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
      "appium:autoGrantPermissions": "true",
      "appium:connectHardwareKeyboard": "true"
}
# caps["platformName"] = "android"
# caps["appium:platformVersion"] = "11"
# caps["appium:deviceName"] = "emulator-5554"
# caps["appium:automationName"] = "UiAutomator2"
# caps["appium:appPackage"] = "com.android.chrome"
# caps["appium:appActivity"] = "com.google.android.apps.chrome.Main"
# caps["appium:ensureWebviewsHavePages"] = True
# caps["appium:nativeWebScreenshot"] = True
# caps["appium:newCommandTimeout"] = 3600
# caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
time.sleep(10)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Financial Freedom\nStarts Here\nLogin/Sign Up\nPhone Number")
el1.click()

# Choose one to un/command to switch languange 
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="ID")
el2.click()
time.sleep(10)
# el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="EN")
# el3.click()

driver.quit()