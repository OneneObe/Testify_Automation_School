from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_id(driver):
    email = driver.find_element(By.ID, "email")
    print("Id:", email)
    password = driver.find_element(By.ID, "pass")
    print("Id:", password)


def locate_by_name(driver):
    first_name = driver.find_element(By.NAME, "firstname")
    print("FirstName:", first_name)
    last_name = driver.find_element(By.NAME, "lastname")
    print("LastName:", last_name)


def locate_by_class_name(driver):
    class_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("Class_Element:", class_element)
    class_nelements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for class_nelement in class_nelements:
        print("Class_Element:", class_nelements)


def main():
    
    driver = webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')
    # locate_by_id(driver) used facebook.com

    # locate by name
    # locate_by_name(driver)

    # locate by class_name
    locate_by_class_name(driver)


if __name__ == '__main__':
    main()
