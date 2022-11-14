""" Using    the    Chrome    browser    navigate    to https://www.facebook.com/, fill  in  the  email/phone
and password text box then click the Login Button. """

from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_id(driver):
    email = driver.find_element(By.ID, "email")
    print("Id:", email)
    password = driver.find_element(By.ID, "pass")
    print("Id:", password)


def main():
    driver = webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')
    # locate_by_id(driver) used facebook.com

    # locate by name
    locate_by_name(driver)


if __name__ == '__main__':
    main()
