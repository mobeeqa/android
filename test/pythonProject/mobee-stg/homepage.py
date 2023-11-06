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

# Tab the menu Nav Bar
home = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Home\nTab 1 of 5")
home.click()
trade = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Trade\nTab 2 of 5")
trade.click()
earn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Earn\nTab 3 of 5")
earn.click()
trx = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Transactions\nTab 4 of 5")
trx.click()
wallet = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Wallet\nTab 5 of 5")
wallet.click()

# driver.quit()