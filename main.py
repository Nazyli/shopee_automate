from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.page_load_strategy = 'eager'
login_url = 'https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F'
# login_url = 'https://shopee.co.id/'

def nextCheckout(driver):
    buy_XPATH = '//span[contains(text(), "checkout")]'
    try:
        driver.find_element_by_xpath(buy_XPATH).click()
    except NoSuchElementException:
        print("NOT FOUND")
        nextCheckout(driver)

def nextLanjut(driver):
    driver.refresh()
    try:
        buy_XPATH = '//button[contains(text(), "beli sekarang")]'
        driver.find_element_by_xpath(buy_XPATH).click()
        nextCheckout(driver)
        print("IS FOUND")
    except NoSuchElementException:
        print("NOT FOUND")
        nextLanjut(driver)

def purchase():
    phone = '' # isi dengan nomor handphone
    password = '' # isi dengan password
    # url untuk barang yang ingin dibeli
    item_url = 'https://shopee.co.id/Apple-iPhone-11-Pro-512GB-Midnight-Green-i.255563049.6435648695'
    # item_url ='https://shopee.co.id/HEADSET-BLUETOOTH-JBL-ORIGINAL-SPORT-MAGNETIC-i.143671303.2343821913'
    driver = webdriver.Firefox(executable_path = '/Users/nazyli/Downloads/geckodriver', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get(login_url)
    wait.until(presence_of_element_located((By.NAME, 'loginKey')))

    # otomatis mengisi nomor handphone
    driver.find_element_by_name('loginKey').send_keys(phone)
    #otomatis mengisi password
    driver.find_element_by_name('password').send_keys(password + Keys.RETURN)

    otp = str (send_OTP())
    driver.find_element_by_css_selector('input[autocomplete="one-time-code"]').send_keys(otp + Keys.RETURN)
    wait.until(presence_of_element_located((By.CLASS_NAME, 'navbar__username')))

    driver.get(item_url)
    variant_XPATH = "//button[contains(., 'Red')]" # ganti Red dengan nama variant di barang
    buy_XPATH = '//button[contains(text(), "beli sekarang")]'
    
    # wait.until(presence_of_element_located((By.XPATH, variant_XPATH)))
    # driver.find_element_by_xpath(variant_XPATH).click()

    # wait.until(presence_of_element_located((By.CLASS_NAME, 'product-variation--selected')))
    try:
        driver.find_element_by_xpath(buy_XPATH).click()
        print("IS FOUND")
    except NoSuchElementException:
        print("NOT FOUND")
        driver.refresh()
        nextLanjut(driver)

def send_OTP():
    text = str(input ("Enter OTP: "))
    return text

purchase()
