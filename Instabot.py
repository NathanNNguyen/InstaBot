from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

sleep_time = 3.5


def login(browser):
    browser.get('https://www.instagram.com/')
    time.sleep(sleep_time)

    username = browser.find_element_by_css_selector('[name="username"]')
    password = browser.find_element_by_css_selector('[name="password"]')
    login = browser.find_element_by_css_selector('button')

    username.send_keys('your username')
    password.send_keys('your password')
    login.click()

    time.sleep(sleep_time)


def Explore(browser, url):
    browser.get(url)
    time.sleep(5)

    picture_count = 0

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    for picture in pictures:
        if picture_count >= 10:
            break

        picture.click()
        time.sleep(sleep_time)

        # browser.find_element_by_css_selector("[aria-label='Like']").click()
        heart = browser.find_element_by_css_selector("[aria-label='Like']")
        heart.click()

        follow = browser.find_element_by_css_selector(
            "button[class='sqdOP yWX7d    y3zKF     ']")
        follow.click()

        time.sleep(1.5)

        close = browser.find_element_by_css_selector("[aria-label='Close']")
        close.click()

        picture_count += 1
        time.sleep(sleep_time)


def main():
    browser = webdriver.Chrome()
    login(browser)

    # tags = [
    #     'python',
    #     'webdev',
    #     'webdevelopment',
    #     'coding',
    #     'frontend',
    #     'ui',
    #     'programmers',
    #     'javascript',
    #     'programming',
    #     'softwaredeveloper',
    #     'softwareengineer',
    #     'dropshipping',
    #     'entrepreneur',
    #     'millionaire',
    #     'billionaire'
    # ]

    while True:
        Explore(browser, f'https://www.instagram.com/explore')
        # for tag in tags:
        # Explore(browser, f'https://www.instagram.com/explore/tags/{tag}')
        time.sleep(30)


main()
