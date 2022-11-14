from time import sleep

from selenium import webdriver


def main():
    driver = webdriver.Edge(executable_path=r"C:\WEB_DRIVERS\edgeDriver/msedgedriver.exe")
    driver.get("http://www.google.com")
    driver.close()


main()
