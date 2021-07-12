from bs4 import BeautifulSoup
import requests,random,string,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "https://steamcommunity.com/login"

def generator():
    while True:
        res = ''.join(random.choices(string.ascii_uppercase +  string.digits + "-", k = 3)) 
        url = "https://steamcommunity.com/id/" + res
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(url)
        try:
            body = soup.find(id="message").get_text()  
            if body.__contains__("The specified profile could not be found."):
                print("This ID is Available!")
                return(res)
                break
        except AttributeError:
            continue

def setup():
    url ="https://steamcommunity.com/login"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    user = str(input("Enter you username: "))
    pwd = str(input("Enter your password: "))
    driver.get(url)
    
    driver.find_element_by_id("input_username").send_keys(user)
    driver.find_element_by_id("input_password").send_keys(pwd)
    sumbit = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div[1]/div/div/div/div/div[3]/div[1]/button")
    sumbit.click()
    try:
        auth = str(input("Enter auth code: "))
        driver.find_element_by_id("authcode").send_keys(auth)
        authsubmit = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        continueButton = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]")
        authsubmit.click()
        continueButton.click()
    except Exception:
        pass
    driver.implicitly_wait(5)
    edit_profile = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[1]/div/div/div/div[3]/div[2]/a/span")
    edit_profile.click()
    print("Setup Complete!")

def sniper(id):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[2]/div[3]/label/div[2]/input").clear()
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[2]/div[3]/label/div[2]/input").send_keys(id)
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[7]/button[1]").click()
    except Exception:
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div[2]/div[3]/label/div[2]/input").clear()
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div[2]/div[3]/label/div[2]/input").send_keys(id)
        driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[8]/button[1]")
    time.sleep(1)
    print(id,driver.current_url.split("/")[4])
    if driver.current_url.split("/")[4] == id:
        print("""
        ▄████ ▓█████▄▄▄█████▓     ██████  ███▄    █  ██▓ ██▓███  ▓█████ ▓█████▄ 
        ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▒██▀ ██▌
        ▒██░▄▄▄░▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ░██   █▌
        ░▓█  ██▓▒▓█  ▄░ ▓██▓ ░      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ░▓█▄   ▌
        ░▒▓███▀▒░▒████▒ ▒██▒ ░    ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░▒████▓ 
        ░▒   ▒ ░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░ ▒▒▓  ▒ 
        ░   ░  ░ ░  ░   ░       ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░ ░ ▒  ▒ 
        ░ ░   ░    ░    ░         ░  ░  ░     ░   ░ ░  ▒ ░░░          ░    ░ ░  ░ 
            ░    ░  ░                 ░           ░  ░              ░  ░   ░    
                                                                        ░      \nThe ID is %s.""" %(id))
        return True        
    else:
        print('False Positive')

def main():
    setup()
    while True:
        id = generator()
        #print(id)
        botak = sniper(id)
        if botak == True:
            break
main()