from selenium import webdriver
import selenium.webdriver.chrome.service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")


if __name__ == '__main__':
    main()

