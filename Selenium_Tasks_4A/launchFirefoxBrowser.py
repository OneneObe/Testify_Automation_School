
from time import sleep

from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path=r"C:\WEB_DRIVERS\geckoDriver/geckodriver.exe")
    driver.get("http://www.google.com")
    sleep(3000)
    driver.close()


main()
