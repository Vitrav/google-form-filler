import selenium

# open Chrome 
driver = selenium.webdriver.Chrome( 
    'E:/Git/Drivers/chromedriver_win32/chromedriver.exe') 


# Open URL 
driver.get('https://forms.gle/vWVmojtWdfFvEj8V6') 
  
# wait for one second, until page gets fully loaded 
time.sleep(1) 
  