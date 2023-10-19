from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_search_button(browser):
    browser.get(link)
    time.sleep(15) #чтобы вы увидели кнопкку
    button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert len(button) > 0, 'button not found'

