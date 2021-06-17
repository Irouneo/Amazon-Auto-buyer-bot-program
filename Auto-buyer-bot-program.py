import time
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome("/Users\Downloads\chromedriver_win32\chromedriver.exe") #Chrome webdriver location

browser.get("https://www.amazon.co.uk/gp/product/B08H95Y452?pf_rd_r=PVZGNSC06XF89ZD2ZCWN&pf_rd_p=6e878984-68d5-4fd2-b7b3-7bc79d9c8b60&pd_rd_r=a57fa674-b176-4535-ac0f-4c09a45728fd&pd_rd_w=DwFGX&pd_rd_wg=w6pZu&ref_=pd_gw_unk") #Url for product

buybutton = False # if buy button is not detected then webpage will refresh
while not buybutton:
    try:
        addToCartbtn = addbutton = browser.find_element_by_id("outOfStockBuyBox_feature_div")
        print("button is not ready")
        time.sleep(2)
        browser.refresh()

    except:
        browser.find_element_by_name("submit.buy-now").click() #click automation for buy button




        print("button was clicked")
        buybutton = True
        email = browser.find_element_by_id("ap_email")
        email.send_keys("enter email") #enter email
        browser.find_element_by_id("continue").click()
        password = browser.find_element_by_id("ap_password")
        pword = "enter password" #enter password
        password.send_keys(pword)
        browser.find_element_by_id("signInSubmit").click()
        browser.find_element_by_id("submitOrderButtonId").click()
