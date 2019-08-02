from airtest.core.api import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
device_1=connect_device('android:///10.23.157.44:5555?cap_method=javacap&touch_method=adb')

poco = AndroidUiautomationPoco(device_1, use_airtest_input=True, screenshot_each_action=False)

poco(text='重装战姬').click()
sleep(3)



