from selenium import webdriver
import selenium.webdriver.firefox.service
from webdriver_manager.firefox import GeckoDriverManager


def main():
    driver = webdriver.Firefox(service=selenium.webdriver.firefox.service.Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com")


if __name__ == '__main__':
    main()
