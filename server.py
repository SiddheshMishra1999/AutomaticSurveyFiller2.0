import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv



# assert "Python" in driver.title
# find element with a specific id
def find_elem_id(id):
    wait(2)
    elem = driver.find_element(By.ID, id)
    return elem

# find element with a specific id
def find_elem_class(id):
    wait(2)
    elem = driver.find_elements(By.CSS_SELECTOR, "td.c4")
     
    return elem


# wait time to find the element with a specific id
def wait(x):
    #some delay
    time.sleep(x) 


# click the next button
def click_next():
    driver.find_element(By.ID, "NextButton").click()
    

# fill in the element
def fill_text_box(elem):
    # elem.click()
    # Keys you want to send 
    elem.send_keys("true")
    # keys wil be sent and show on the text box
    elem.send_keys(Keys.RETURN)



def fill_auth_part():
    wait(1)
    id = "QR~Authentication-FL_252~0"
    elem = find_elem_id(id)
    fill_text_box(elem)
    click_next()
    wait(2)
    click_next()
    wait(1)
    elem = find_elem_id(id)
    fill_text_box(elem)
    click_next()
    wait(2)
    click_next()

def survey_start(ids):
    wait(2)
    click_next()
    index = 0
    while(index < len(ids)):
        if(ids[index] == "QR~QID45"):
            elem = find_elem_id(ids[index])
            fill_text_box(elem)
            click_next()
        elif (ids[index] == radio1 ):
            radio_fill(radio1)
            # needed wait
            wait(1)
            click_next()
          
        elif (ids[index] == radio2 ):
            radio_fill(radio2)
            

        elif (ids[index] == radio3):
            wait(1)
            radio_fill(radio3)

        elif (ids[index] == nexting):
            wait(1)
            click_next()
        else: 
            elem = find_elem_id(ids[index]).click()
            click_next()
            
        index += 1

def radio_fill(radio):
    elems = find_elem_class(radio)
    actions = ActionChains(driver)
    for i in elems:
        actions.move_to_element(i).click().perform()
    click_next()





'''
    authentication text box id: "QR~Authentication-FL_252~0"
    Yes id: "QID14-1-label"
    Highly Satisfied id: "QID15-4-label"
    enjoyed text box id: "QR~QID45"
    carry out id: "QID18-6-label"
    Frount counter id: "QID19-5-label"
    beverage only id: "QID20-5-label"
    radio button highly satisfied ids:
        accuracy: "QR~QID23~4~1"
        taste: "QR~QID23~6~1"
        speed: "QR~QID23~7~1"
        friendliness: "QR~QID23~8~1"
        in clean: "QR~QID23~10~1"
        out clean: "QR~QID23~11~1"

    visit restaurant radio:
        visit again: "QR~QID44~1~1"
        recommend: "QR~QID44~3~1"
    No problem visit id: "QID37-2-label"
    Cold Beverage id: "QID48-4-label"
    iced coffee id: "QID54-52-label"
    Highly satisfied ice coffee id: "QID57-1-label"
    opinion on ice coffee radio:
        size: "QR~QID59~8~1"
        apprearance: "QR~QID59~9~1"
        package: "QR~QID59~10~1"
        taste: "QR~QID59~1~1"
        temp: "QR~QID59~2~1"
        quality: "QR~QID59~3~1"
        flavor: "QR~QID59~6~1"
        value: "QR~QID59~7~1"
    Highly likely id: "QID74-4-label"
    No recognition id: "QID68-2-label"
''' 




# clear any value in the elem
# elem.clear()


# assert "No results found." not in driver.page_source
# 

if __name__ == '__main__':
    load_dotenv()
    url: str = os.environ.get("URL")
    driver = webdriver.Firefox()
    driver.get(url)
    wait(2)
    radio1 = ["QR~QID23~4~1", "QR~QID23~6~1",
        "QR~QID23~7~1", "QR~QID23~8~1", "QR~QID23~10~1", "QR~QID23~11~1"]
    radio2 = ["QR~QID44~1~1", "QR~QID44~3~1"]
    radio3 = ["QR~QID59~8~1", "QR~QID59~9~1",
            "QR~QID59~10~1","QR~QID59~1~1",
            "QR~QID59~2~1", "QR~QID59~3~1",
            "QR~QID59~6~1", "QR~QID59~7~1"]
    nexting = ""
    ids = ["QID14-1-label", "QID15-4-label", "QR~QID45", "QID18-6-label", 
        "QID19-5-label", "QID20-5-label", radio1, radio2, "QID37-2-label", "QID48-4-label",
        "QID54-52-label", "QID57-1-label", radio3, "QID74-4-label",nexting, "QID68-2-label"]


    # for single use: 
    # fill_auth_part()
    # survey_start(ids)

    # for multi use
    for i in range(20):
        fill_auth_part()
        survey_start(ids)
        # refresh page
        wait(3)
        driver.refresh()


    driver.close()