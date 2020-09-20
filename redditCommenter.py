"""
redditCommenter is a Selenium based automation to comment in specific posts.

The PRAW API is much more efficient, but I made this as a joke comment in the /r/learnpython subreddit.

This is not acceptable under Reddit's policy, but it works, so use at your own discretion!

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import time

desktop = os.path.expanduser("~/Desktop")
webdriverPath = f'{desktop}\\chromedriver.exe'
# This chunk of code not only launches the webdriver, but also blocks notification popups, which are a pain in the butt!
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=webdriverPath)


postUrl = "https://www.reddit.com/r/learnpython/comments/imjzux/this_is_how_i_learned_python_and_django/"
redditAccount = input("Please provide your Reddit account name: ")
redditPassword = input("Please provide your Reddit account password: ")
congratsComment = input("Please provide the congratulations message you would like to send: ")


def congratulator(redditURL, redditAcct, redditPwd, message):
    browser.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")
    time.sleep(3)
    userName = browser.find_element_by_xpath('//*[@id="loginUsername"]')
    userName.send_keys(redditAccount)
    passWord = browser.find_element_by_xpath('//*[@id="loginPassword"]')
    passWord.send_keys(redditPassword)
    loginButton = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div[1]/fieldset[5]/button')
    loginButton.click()
    time.sleep(3)
    browser.get(postUrl)
    time.sleep(3)
    textBox = browser.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div')
    textBox.send_keys(message)
    sendComment = browser.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[1]/button')
    sendComment.click()

congratulator(postUrl, redditAccount, redditPassword, congratsComment)


