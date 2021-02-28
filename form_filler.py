from selenium import webdriver
import time
import random
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")



def fill_form():
    # open Chrome 
    driver = webdriver.Chrome( 
    'E:/Git/Drivers/chromedriver_win32 88/chromedriver.exe', options=option) 
    # Open URL 
    driver.get('https://forms.gle/HwPMv7C74WGZJ7dV8') 
    
    # wait for one second, until page gets fully loaded 
    time.sleep(1) 

    textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

    # get the container for the radiobuttons and go through all of them, finding the actual buttons.
    radiobuttons_container = driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoicesContainer")
    for element in radiobuttons_container:
        radiobuttons = element.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
        radiobuttons[random.randint(0,3)].click()

    checkboxes = driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    submitbutton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


    # click on submit button 
    submit = driver.find_element_by_xpath( 
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span') 
    submit.click() 


for __ in range(100):
    fill_form()

  