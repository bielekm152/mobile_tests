from typing import Dict, Any

# configuration of capabilities
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.ryanair.cheapflights',
    'appActivity': 'com.ryanair.cheapflights.ui.SplashScreenActivity'
}

# URL with port specified in Appium server
url = 'http://localhost:4723/wd/hub'
