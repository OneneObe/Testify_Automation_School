from time import sleep

from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path=r"C:\WEB_DRIVERS\chromeDriver/chromedriver.exe")
    driver.get("http://www.google.com")
    sleep(3000)
    driver.close()


main()
