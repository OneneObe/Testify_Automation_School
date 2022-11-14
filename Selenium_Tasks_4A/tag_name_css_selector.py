from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_tag_name(driver):
    email = driver.find_element(By.ID, "email")
    print("Id:", email)
    password = driver.find_element(By.ID, "pass")
    print("Id:", password)


def locate_by_tag_name(driver):
    pass


def locate_by_css_selector(driver):
    pass


def main():
    driver = webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')

    # locate by tag name
    locate_by_tag_name(driver)

    # locate by CSS Selector
    locate_by_css_selector(driver)


if __name__ == '__main__':
    main()
