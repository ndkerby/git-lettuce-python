from lettuce import *
from selenium import webdriver

 
@before.all  
def setup_browser():  
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX 
    desired_capabilities['version'] = '12'  
    desired_capabilities['platform'] = 'MAC'  
    desired_capabilities['name'] = 'Testing Selenium 2 with Lettuce'  


