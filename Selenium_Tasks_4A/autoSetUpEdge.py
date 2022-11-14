from selenium import webdriver
import selenium.webdriver.edge.service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.ChromiumEdge(service=selenium.webdriver.edge.service.Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.google.com")


if __name__ == '__main__':
    main()
