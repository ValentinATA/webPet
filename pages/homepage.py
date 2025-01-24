from conftest import driver
from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoblaze.com/")

    def click_galaxy(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
        galaxy_s6.click()