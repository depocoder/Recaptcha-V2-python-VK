import os

from python_rucaptcha import ReCaptchaV2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


RUCAPTCHA_KEY = os.getenv("RUCAPTCHA_KEY")
SITE_KEY = '6Le00B8TAAAAACHiybbHy8tMOiJhM5vh88JVtP4c'
PAGE_URL = "https://vk.com/"


def check_captcha(driver):
    try:
        captcha = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_xpath('//iframe[@title="reCAPTCHA"]'))
        user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(
            site_key=SITE_KEY, page_url=PAGE_URL)
        driver.execute_script(f"___grecaptcha_cfg.clients['0']['W']['W']['callback']({user_answer['captchaSolve']})")
    except Exception as E:
        return


def login_vk_via_selenium(driver):
    driver.get('https://vk.com')

    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath('//input[@id="index_email"]')).send_keys('sdjkfhsdjkfs')
    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath('//input[@id="index_pass"]')).send_keys('sdjkfhsdjkfs')
    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath('//button[@id="index_login_button"]')).click()
    check_captcha(driver)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_vk_via_selenium(driver)