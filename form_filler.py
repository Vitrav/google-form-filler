from selenium import webdriver
import time
import random
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")

random_text = []


def fill_form():
    # open Chrome 
    driver = webdriver.Chrome( 
    'E:/Git/Drivers/chromedriver_win32 88/chromedriver.exe', options=option) 
    # Open URL 
    # driver.get('https://forms.gle/HwPMv7C74WGZJ7dV8') 
    
    # wait for one second, until page gets fully loaded 
    time.sleep(1) 

    current_checkbox=0
    current_radio = 0
    current_open_answer = 0

    textbox_answers = [
        ["wiskunde", "getallen van 10", "10*10","assenstelsel", "meten", "afstand", "???", "stapjes in maten", "km, hm, dam, m, dm, cm, mm","maten van inhoud", "ezelsbruggetje"],
        ["l x b x h", "lxbxh", "geen idee", "lengte keer breedte keer hoogte", "???", "lengte x breedte x hoogte", "lengte keer breedte"],
        ["l x b", "geen idee", "lengte keer breedte", "lengte x breedte", "???", "lxb", "breedte x hoogte", "lengte keer breedte keer hoogte"]
    ]

    radio_answers= [2,4,0,6,2,3]
    checkbox_answers = [[1,2,3,6], [0,2,4]]


    textboxes_container = driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionTextRoot")
    for element in textboxes_container:
        textbox = element.find_element_by_class_name("quantumWizTextinputPaperinputInput")
        textbox.send_keys([textbox_answers[current_open_answer][random.randint(0,len(textbox_answers[current_open_answer])-1)]])
        current_open_answer += 1 

    #get the container for the checkboxes
    checkboxes_container = driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionCheckboxRoot")
    for element in checkboxes_container:
        checkboxes = element.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
        if current_checkbox == 0:
            if random.randint(0,10) >= 3:
                for answer in checkbox_answers[current_checkbox]:
                    checkboxes[answer].click()
            else:
                for __ in range(0, random.randint(0,len(checkboxes)-1)):
                    checkboxes[random.randint(0, len(checkboxes)-3)].click()
        if current_checkbox == 1:
            if random.randint(0,10) >= 4:
                for answer in checkbox_answers[current_checkbox]:
                    checkboxes[answer].click()
            else:
                for __ in range(0, random.randint(0,len(checkboxes)-1)):
                    checkboxes[random.randint(0, len(checkboxes)-3)].click()

        current_checkbox += 1

    # get the container for the radiobuttons and go through all of them, finding the actual buttons.
    radiobuttons_container = driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoicesContainer")
    for element in radiobuttons_container:
        radiobuttons = element.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")

        if current_radio == 0:
            if random.randint(0,10) >= 2:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()
        
        if current_radio == 1:
            if random.randint(0,10) >= 7:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()

        if current_radio == 2:
            if random.randint(0,10) >= 7:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()

        if current_radio == 3:
            if random.randint(0,10) >= 8:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()
       
        if current_radio == 4:
            if random.randint(0,10) >= 7:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()

        if current_radio == 5:
            if random.randint(0,10) >= 8:
                radiobuttons[ radio_answers [current_radio]].click()
            else:
                radiobuttons[random.randint(0,len(radiobuttons)-1)].click()
        current_radio += 1



    submitbutton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


    # click on submit button 
    submit = driver.find_element_by_xpath( 
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span') 
    submit.click() 


for __ in range(29):
    fill_form()

fill_form()
# time.sleep(20) 


  