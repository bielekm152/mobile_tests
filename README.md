# mobile_tests
Technical task #3

Tests were designed to test basic functionalities of Ryanair mobile application on Android devices

APK file can be downloaded from link:
https://www.apkmirror.com/apk/ryanair/ryanair-cheapest-fares/ryanair-cheapest-fares-3-171-0-release/

SW needed to set up environment for tests:
-Android studio (with emulator and
installed com.ryanair.cheapflights_3.171.0-908_minAPI26(arm64-v8a,armeabi,armeabi-v7a,mips,x86,x86_64)(nodpi)_apkmirror.com.apk)
-Appium Server
-platform-tools
-python IDE
-real Android device in case of testing on real device (with "USB debugging" option enabled and
installed com.ryanair.cheapflights_3.171.0-908_minAPI26(arm64-v8a,armeabi,armeabi-v7a,mips,x86,x86_64)(nodpi)_apkmirror.com.apk)

after getting the project run "pip install -r requirements.txt" to install all necessary libraries
to run tests from command line use command "python .\test_mobile_app.py"
to run only a specific test use command "python .\test_mobile_app.py -k {test name}"

port for Appium Server is specified in "config.py" line 13 (in case different port is used, change 4723 to correct port number)

to find appPackage and appActivity use (adb shell dumpsys window | find "mCurrentFocus") when app is running
