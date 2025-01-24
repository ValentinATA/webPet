from selenium.webdriver.common.by import By
from pages.product import ProductPage
from pages.homepage import Homepage


def test_open_s6(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_galaxy()
    product_page = ProductPage(driver)
    product_page.check_title("Samsung galaxy s6")


def test_monitor(driver):
    driver.get("https://demoblaze.com/")
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    assert len(monitors) == 2