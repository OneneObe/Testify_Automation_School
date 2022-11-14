from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com')
    # about_Element = driver.find_element(By.TAG_NAME, "h1")
    # print("About_Element", about_Element, about_Element.text)

    about_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("about_Element:", about_element, about_element.text)

    # links = driver.find_elements(By.TAG_NAME, "a")
    # for link in links:
    #   print("Links:", link.text)


if __name__ == '__main__':
    main()
