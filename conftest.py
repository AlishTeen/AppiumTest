import pytest
from appium import webdriver

APPIUM_SERVER_PATH = 'http://localhost:4723/wd/hub'
current_device = {
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "platformName": "Android",
    "appPackage": "com.android.dialer"
}


@pytest.fixture(scope="class")
def android_driver():
    driver = webdriver.Remote(APPIUM_SERVER_PATH, current_device)
    yield driver
    driver.quit()
