import time
import unittest
import pytest
import config
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilities = config.cap
url = config.url


class TestSuite(unittest.TestCase):
    if __name__ == "__main__":
        pytest.main()

    def setUp(self):
        # Establishing of connection with emulator or real device and opening specified application
        self.driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))

    def test_1_search_flights(self):
        # Test to check if error message was correctly displayed after
        # invalid credentials were set, when retrieving booking
        self.driver.implicitly_wait(500)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.FrameLayout[@resource-id="com.ryanair.cheapflights:id/bottom_navigation_container"])[3]')
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value='com.ryanair.cheapflights:id/empty_state_button')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter a number"]')
        el.click()
        el.send_keys('TEST01')
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter an Email"]')
        el.click()
        el.send_keys('TEST01@test.com')
        el = self.driver.find_element(by=AppiumBy.ID, value='com.ryanair.cheapflights:id/view_button_bar_next_btn')
        el.click()
        el = self.driver.find_element(by=AppiumBy.ID, value='com.ryanair.cheapflights:id/title')
        result = el.text
        assert result == "Oops, error!"

    def test_2_forgot_password_error(self):
        # Test to check if error message was correctly displayed when email in
        # incorrect format is entered in field for email in Forgot password menu
        self.driver.implicitly_wait(500)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Forgot password?"]')
        el.click()
        time.sleep(1)
        el = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
        el.click()
        el.send_keys('test')
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Email is incorrect"]')
        el = el.text
        assert el == "Email is incorrect"

    def tearDown(self):
        # After test is completed application will stay open for 2 seconds and then application quits
        time.sleep(2)
        self.driver.quit()
